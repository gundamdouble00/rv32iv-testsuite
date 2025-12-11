import random

from rv_instructions.v_extension.base_vector import IntegerArithmeticIns
from rv_types.instruction_type import type_of_ins
from rv_types.registers import ACTIVE_REG, integer_index_ua


def get_src1_type(name: str) -> str:
    name_len = len(name)
    src1_para = {"v", "x", "i"}
    v_x_i: str = name[name_len - 1]

    if v_x_i not in src1_para:
        v_x_i = name[name_len - 2]

    return v_x_i


def not_widening(ins, src1_range: tuple = None):
    step: int = max(1, int(ins.lmul))
    start: int = 0 if not ins.mask else step

    des_index = random.randrange(start=start, stop=24, step=step)
    src2_index = random.randrange(start=start, stop=32, step=step)

    ins.des = f"v{des_index}"
    ins.src2 = f"v{src2_index}"

    src1_type = get_src1_type(ins.name)
    if src1_type == "v":
        ins.src1 = f"v{random.randrange(0, 32, step=step)}"
    elif src1_type == "x":
        ins.src1 = random.choice(ACTIVE_REG)
    else:
        ins.src1 = f"{random.randint(src1_range[0], src1_range[1])}"

    ins.type = type_of_ins[type(ins).__name__]


def is_widening(ins):
    step: int = max(1, int(ins.lmul))
    name_len = len(ins.name)
    src2_step: int = step

    # random destination register index
    des_index: int = random.randrange(start=step * 2, stop=24, step=step * 2)

    ins.des = f"v{des_index}"

    if ins.name[name_len - 2] == "w":
        src2_step *= 2
    # random source 2 register index
    while True:
        src2_index = random.randrange(0, 32, src2_step)
        if src2_index < des_index or (des_index + step * 2 - 1) < src2_index:
            break

    # random source 1 register index
    if ins.name[name_len - 1] == "v":
        while True:
            src1_index = random.randrange(0, 32, step)
            if src1_index < des_index or (des_index + step * 2 - 1) < src1_index:
                break
    else:
        while True:
            src1_index = random.randint(0, 31)
            if src1_index not in integer_index_ua:
                break

    ins.des = f"v{des_index}"
    ins.src2 = f"v{src2_index}"
    ins.src1 = f"{ins.name[name_len - 1]}{src1_index}"
    ins.type = type_of_ins[type(ins).__name__]


class SingleWidthIntegerAddSub(IntegerArithmeticIns):
    def __init__(self, name: str, index: int, lmul: float, sew: int) -> None:
        super().__init__(name, index, lmul, sew)
        not_widening(self, src1_range=(-16, 15))


class WideningIntegerAddSub(IntegerArithmeticIns):
    def __init__(self, name: str, index: int, lmul: float, sew: int) -> None:
        if int(lmul) == 8 or sew == 32:
            raise ValueError("lmul cannot be 8 and sew cannot be 32")
        super().__init__(name, index, lmul, sew)
        is_widening(self)


class IntegerExtension(IntegerArithmeticIns):
    def __init__(self, name: str, index: int, lmul: float, sew: int) -> None:
        base_name = name.split(".")[0]

        if sew not in [16, 32]:
            raise ValueError(f"Extension Destination SEW must be 16 or 32. Got {sew}")

        if sew == 16:
            fraction = 2
        else:
            fraction = random.choice([2, 4])  # .vf2 hoặc .vf4

        self.name = f"{base_name}.vf{fraction}"

        super().__init__(self.name, index, lmul, sew)

        self.src_lmul = lmul / fraction
        if self.src_lmul < 0.125:
            pass
        self.des, self.src2 = self.allocate_registers_simple()
        self.type = type_of_ins[IntegerExtension.__name__]

    def allocate_registers_simple(self):
        align = 1 if self.lmul < 1 else int(self.lmul)

        num_dest = 1 if self.lmul < 1 else int(self.lmul)
        num_src = 1 if self.src_lmul < 1 else int(self.src_lmul)

        while True:
            vd_idx = random.randrange(0, 24, align)
            vs2_idx = random.randrange(0, 24, align)

            if self.mask and vd_idx == 0:
                continue

            dest_regs = set(range(vd_idx, vd_idx + num_dest))
            src_regs = set(range(vs2_idx, vs2_idx + num_src))

            if not dest_regs.isdisjoint(src_regs):
                continue

            return f"v{vd_idx}", f"v{vs2_idx}"

    def generate(self) -> str:
        mask_suffix = ", v0.t" if self.mask else ""
        return f"{self.name} {self.des}, {self.src2}{mask_suffix}"


class IntegerAddWCarrySubWBorrow(IntegerArithmeticIns):
    def __init__(self, name: str, index: int, lmul: float, sew: int) -> None:
        super().__init__(name, index, lmul, sew)
        if name[len(name) - 1] == "m":
            self.mask = True
        not_widening(self, src1_range=(-16, 15))

    def generate(self) -> str:
        name_len = len(self.name)
        suffix: str = ", v0" if self.name[name_len - 1] == "m" else ""
        return f"{self.name} {self.des}, {self.src2}, {self.src1}{suffix}"


class BitwiseLogical(IntegerArithmeticIns):
    def __init__(self, name: str, index: int, lmul: float, sew: int) -> None:
        super().__init__(name, index, lmul, sew)
        not_widening(self, src1_range=(-16, 15))


class SingleWidthShift(IntegerArithmeticIns):
    def __init__(self, name: str, index: int, lmul: float, sew: int) -> None:
        super().__init__(name, index, lmul, sew)
        not_widening(self, src1_range=(0, 31))


class NarrowingIntegerRightShift(IntegerArithmeticIns):
    def __init__(self, name: str, index: int, lmul: float, sew: int) -> None:
        if sew == 32 or int(lmul) > 4:
            raise ValueError("sew must be 8 or 16, and lmul must be smaller than 8")

        super().__init__(name, index, lmul, sew)
        step: int = max(1, int(lmul))
        src2_index: int = random.randrange(0, 32, step=step * 2)
        self.src2 = f"v{src2_index}"

        src1_type = name[len(name) - 1]
        if src1_type == "v":
            self.src1 = f"v{random.randrange(0, 32, step)}"
        elif src1_type == "x":
            self.src1 = random.choice(ACTIVE_REG)
        else:
            self.src1 = f"{random.randint(0, 31)}"

        start: int = 0
        if self.mask:
            start = step
        while True:
            des_index = random.randrange(start=start, stop=24, step=step)
            if des_index < src2_index or (src2_index + step * 2 - 1) < des_index:
                self.des = f"v{des_index}"
                break

        self.type = type_of_ins[NarrowingIntegerRightShift.__name__]


class IntegerCompare(IntegerArithmeticIns):
    def __init__(self, name: str, index: int, lmul: float, sew: int) -> None:
        super().__init__(name, index, lmul, sew)
        not_widening(self, src1_range=(-16, 15))


class IntegerMinMax(IntegerArithmeticIns):
    def __init__(self, name: str, index: int, lmul: float, sew: int) -> None:
        super().__init__(name, index, lmul, sew)
        not_widening(self, src1_range=(0, 0))


class SingleWidthIntegerMultiply(IntegerArithmeticIns):
    def __init__(self, name: str, index: int, lmul: float, sew: int) -> None:
        super().__init__(name, index, lmul, sew)
        not_widening(self, src1_range=(0, 0))


class IntegerDivide(IntegerArithmeticIns):
    def __init__(self, name: str, index: int, lmul: float, sew: int) -> None:
        super().__init__(name, index, lmul, sew)
        not_widening(self, src1_range=(0, 0))


class WideningIntegerMultiply(IntegerArithmeticIns):
    def __init__(self, name: str, index: int, lmul: float, sew: int) -> None:
        if int(lmul) == 8 or sew == 32:
            raise ValueError("lmul cannot be 8 and sew cannot be 32")
        super().__init__(name, index, lmul, sew)
        is_widening(self)


class SingleWidthIntegerMultiplyAdd(IntegerArithmeticIns):
    def __init__(self, name: str, index: int, lmul: float, sew: int) -> None:
        super().__init__(name, index, lmul, sew)
        not_widening(self, src1_range=(0, 0))

    def generate(self) -> str:
        suffix: str = ", v0.t" if self.mask else ""
        return f"{self.name} {self.des}, {self.src1}, {self.src2}{suffix}"


class WideningIntegerMultiplyAdd(IntegerArithmeticIns):
    def __init__(self, name: str, index: int, lmul: float, sew: int) -> None:
        if int(lmul) == 8 or sew == 32:
            raise ValueError("lmul cannot be 8 and sew cannot be 32")
        super().__init__(name, index, lmul, sew)
        is_widening(self)

    def generate(self) -> str:
        suffix: str = ", v0.t" if self.mask else ""
        return f"{self.name} {self.des}, {self.src1}, {self.src2}{suffix}"


class IntegerMerge(IntegerArithmeticIns):
    def __init__(self, name: str, index: int, lmul: float, sew: int) -> None:
        super().__init__(name, index, lmul, sew)
        if name[len(name) - 1] == "m":
            self.mask = True
        not_widening(self, src1_range=(-16, 15))

    def generate(self) -> str:
        return f"{self.name} {self.des}, {self.src2}, {self.src1}, v0"


class IntegerMove(IntegerArithmeticIns):
    def __init__(self, name: str, index: int, lmul: float, sew: int) -> None:
        super().__init__(name, index, lmul, sew)
        not_widening(self, src1_range=(-16, 15))

    def generate(self) -> str:
        return f"{self.name} {self.des}, {self.src1}"
