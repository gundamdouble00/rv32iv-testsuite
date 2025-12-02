import random

import utils.random_value
from rv_instructions.v_extension.base_vector import IntegerArithmeticIns
from rv_types.riscv_infor import type_of_ins


def randrange(start: int, end: int, step: int) -> int:
    return random.randrange(start, end + 1, step)


def vector_des(lmul: int, mask: bool, des_reg: str) -> str:
    # Random destination vector register
    if not mask:
        return des_reg
    return f"v{randrange(2 ** (lmul - 1), 32, lmul)}"


def vector_des_widening(
    lmul: int, mask: bool, des_reg: str, src2: str, src1: str
) -> str:
    # Random destination vector register in "widening" instructions
    src2_src1 = {src2, src1}
    if (not mask) and (des_reg not in src2_src1):
        return des_reg

    start: int = 0
    if mask:
        start = 2 ** (lmul - 1)
    while des_reg in src2_src1:
        des_reg = f"v{random.randrange(start, 32, lmul)}"

    return des_reg


def random_src1(name: str, lmul: int, start: int, end: int) -> str:
    length = len(name)
    parameter = {"v", "x", "i"}
    v_x_i: str = name[length - 1]

    if name[length - 1] not in parameter:
        v_x_i = name[length - 2]

    if v_x_i == "v":
        src1 = f"v{random.randrange(0, 32, lmul)}"
    elif v_x_i == "x":
        src1 = f"x{random.randint(0, 31)}"
    else:
        src1 = f"{random.randint(start, end)}"
    return src1


def configure_instruction(ins, is_widening: bool = False, src1_range: tuple = None):
    ins.type = type_of_ins[type(ins).__name__]
    if is_widening:
        if src1_range is not None:
            ins.src1 = random_src1(ins.name, ins.lmul, *src1_range)
        ins.des = vector_des_widening(ins.lmul, ins.mask, ins.des, ins.src2, ins.src1)
    else:
        ins.des = vector_des(ins.lmul, ins.mask, ins.des)
        if src1_range is not None:
            ins.src1 = random_src1(ins.name, ins.lmul, *src1_range)


class SingleWidthIntegerAddSub(IntegerArithmeticIns):
    def __init__(self, name: str, index: int, lmul: int, sew: int) -> None:
        super().__init__(name, index, lmul, sew)
        configure_instruction(self, is_widening=False, src1_range=(-16, 15))


class WideningIntegerAddSub(IntegerArithmeticIns):
    def __init__(self, name: str, index: int, lmul: int, sew: int) -> None:
        super().__init__(name, index, lmul, sew)
        configure_instruction(self, is_widening=True, src1_range=(0, 0))


class IntegerExtension(IntegerArithmeticIns):
    def __init__(self, name: str, index: int, lmul: int, sew: int) -> None:
        if sew == 8:
            raise ValueError("sew must be 16 or 32")

        super().__init__(name, index, lmul, sew)
        configure_instruction(self, is_widening=False, src1_range=None)

    def generate(self) -> str:
        ins: str = ""
        if self.mask:
            ins = ", v0.t"
        ins = f"{self.name} {self.des}, {self.src2}" + ins
        return ins


class IntegerAddWCarrySubWBorrow(IntegerArithmeticIns):
    def __init__(self, name: str, index: int, lmul: int, sew: int) -> None:
        super().__init__(name, index, lmul, sew)
        configure_instruction(self, is_widening=False, src1_range=(-16, 15))

    def generate(self) -> str:
        ins: str = ""
        length = len(self.name)
        if self.name[length - 1] == "m":
            ins = "v0"

        ins = f"{self.name} {self.des}, {self.src2}, {self.src1}" + ins
        return ins


class BitwiseLogical(IntegerArithmeticIns):
    def __init__(self, name: str, index: int, lmul: int, sew: int) -> None:
        super().__init__(name, index, lmul, sew)
        configure_instruction(self, is_widening=False, src1_range=(-16, 15))


class SingleWidthShift(IntegerArithmeticIns):
    def __init__(self, name: str, index: int, lmul: int, sew: int) -> None:
        super().__init__(name, index, lmul, sew)
        configure_instruction(self, is_widening=False, src1_range=(0, 31))


class NarrowingIntegerRightShift(IntegerArithmeticIns):
    def __init__(self, name: str, index: int, lmul: int, sew: int) -> None:
        super().__init__(name, index, lmul, sew)
        self.src1 = utils.random_value.random_src1(name[len(name) - 1], 0, 31)
        configure_instruction(self, is_widening=False, src1_range=(0, 31))


class IntegerCompare(IntegerArithmeticIns):
    def __init__(self, name: str, index: int, lmul: int, sew: int) -> None:
        super().__init__(name, index, lmul, sew)
        configure_instruction(self, is_widening=False, src1_range=(-16, 15))


class IntegerMinMax(IntegerArithmeticIns):
    def __init__(self, name: str, index: int, lmul: int, sew: int) -> None:
        super().__init__(name, index, lmul, sew)
        configure_instruction(self, is_widening=False, src1_range=(0, 0))


class SingleWidthIntegerMultiply(IntegerArithmeticIns):
    def __init__(self, name: str, index: int, lmul: int, sew: int) -> None:
        super().__init__(name, index, lmul, sew)
        configure_instruction(self, is_widening=False, src1_range=(0, 0))


class IntegerDivide(IntegerArithmeticIns):
    def __init__(self, name: str, index: int, lmul: int, sew: int) -> None:
        super().__init__(name, index, lmul, sew)
        configure_instruction(self, is_widening=False, src1_range=(0, 0))


class WideningIntegerMultiply(IntegerArithmeticIns):
    def __init__(self, name: str, index: int, lmul: int, sew: int) -> None:
        super().__init__(name, index, lmul, sew)
        configure_instruction(self, is_widening=True, src1_range=(0, 0))


class SingleWidthIntegerMultiplyAdd(IntegerArithmeticIns):
    def __init__(self, name: str, index: int, lmul: int, sew: int) -> None:
        super().__init__(name, index, lmul, sew)
        configure_instruction(self, is_widening=False, src1_range=(0, 0))

    def generate(self) -> str:
        ins: str = ""
        if self.mask:
            ins = ", v0.t"

        ins = f"{self.name} {self.des}, {self.src1}, {self.src2}" + ins
        return ins


class WideningIntegerMultiplyAdd(IntegerArithmeticIns):
    def __init__(self, name: str, index: int, lmul: int, sew: int) -> None:
        super().__init__(name, index, lmul, sew)
        configure_instruction(self, is_widening=True, src1_range=(0, 0))

    def generate(self) -> str:
        ins: str = ""
        if self.mask:
            ins = ", v0.t"

        ins = f"{self.name} {self.des}, {self.src1}, {self.src2}" + ins
        return ins


class IntegerMerge(IntegerArithmeticIns):
    def __init__(self, name: str, index: int, lmul: int, sew: int) -> None:
        super().__init__(name, index, lmul, sew)
        configure_instruction(self, is_widening=False, src1_range=(-16, 15))

    def generate(self) -> str:
        return f"{self.name} {self.des}, {self.src2}, {self.src1}, v0"


class IntegerMove(IntegerArithmeticIns):
    def __init__(self, name: str, index: int, lmul: int, sew: int) -> None:
        super().__init__(name, index, lmul, sew)
        configure_instruction(self, is_widening=False, src1_range=(-16, 15))

    def generate(self) -> str:
        return f"{self.name} {self.des}, {self.src1}"
