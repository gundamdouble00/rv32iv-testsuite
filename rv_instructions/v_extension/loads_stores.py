import random

from rv_instructions.v_extension.base_vector import LoadsStores
from rv_types.instruction_type import type_of_ins

base_address = {
    8: "x18",
    16: "x19",
    32: "x20",
}


def get_eew(name: str) -> int:
    result: str = ""
    for char in name:
        if "0" <= char <= "9":
            result += char
    return int(result)


def get_index_eew(name: str) -> int:
    if "ei8" in name:
        return 8
    if "ei16" in name:
        return 16
    if "ei32" in name:
        return 32
    if "ei64" in name:
        return 64
    return 0


def stride_ins(ins):
    eew = get_eew(ins.name)
    # print(f"{ins.name} (eew = {eew}, sew = {ins.sew})")
    emul = ins.lmul * (eew / ins.sew)
    if emul > 8.0:
        raise ValueError("emul must smaller than 8")

    load_store: str = ins.name[1]
    if load_store == "l":
        ins.src1 = base_address[eew]
    else:
        ins.src1 = "x21"

    step: int = max(1, int(emul))
    start: int = 0
    if ins.mask and ins.name[1] == "l":
        start = step
    ins.des = f"v{random.randrange(start=start, stop=24, step=step)}"


class UnitStride(LoadsStores):
    def __init__(self, name: str, index: int, lmul: float, sew: int) -> None:
        super().__init__(name, index, lmul, sew)
        self.type = type_of_ins[UnitStride.__name__]

        # vlm.v, vsm.v
        if self.name in {"vlm.v", "vsm.v"}:
            vreg: str = f"v{random.randint(0, 23)}"
            if self.name == "vlm.v":
                self.des = vreg
                self.src1 = random.choice(["x18", "x19", "x20"])
                return
            self.src3 = vreg
            self.src1 = "x21"
            return

        # vle8.v, vle16.v, vle32.v
        # vse8.v, vse16.v, vse32.v
        stride_ins(self)

    def generate(self) -> str:
        if self.name == "vlm.v":
            return f"{self.name} {self.des}, ({self.src1})"
        if self.name == "vsm.v":
            return f"{self.name} {self.src3}, ({self.src1})"

        suffix = ", v0.t" if self.mask else ""
        return f"{self.name} {self.des}, ({self.src1}){suffix}"


class Strided(LoadsStores):
    def __init__(self, name: str, index: int, lmul: float, sew: int) -> None:
        super().__init__(name, index, lmul, sew)

        self.type = type_of_ins[Strided.__name__]
        self.src2 = "x22"
        stride_ins(self)

    def generate(self) -> str:
        suffix: str = ""
        if self.mask:
            suffix = ", v0.t"
        return f"{self.name} {self.des}, ({self.src1}), {self.src2}{suffix}"


class Indexed(LoadsStores):
    def __init__(self, name: str, index: int, lmul: float, sew: int) -> None:
        super().__init__(name, index, lmul, sew)

        self.is_load = name[1] == "l"

        if "ei8" in name:
            eew_index = 8
        elif "ei16" in name:
            eew_index = 16
        else:
            eew_index = 32

        emul_data = lmul
        emul_index = lmul * (eew_index / sew)
        if emul_data > 8.0 or emul_index > 8.0:
            raise ValueError(
                f"Configuration Impossible: EMUL > 8 (Data: {emul_data}, Index: {emul_index})"
            )

        fixed_index_reg = 24

        step_data = int(emul_data) if emul_data >= 1 else 1
        step_index = int(emul_index) if emul_index >= 1 else 1
        size_data = max(1, step_data)
        size_index = max(1, step_index)

        range_index = set(range(fixed_index_reg, fixed_index_reg + size_index))
        valid_data_regs = []

        for reg_data in range(0, 24, step_data):
            if self.mask and self.is_load and reg_data == 0:
                continue

            if self.is_load:
                range_data = set(range(reg_data, reg_data + size_data))
                if not range_data.isdisjoint(range_index):
                    continue

            valid_data_regs.append(reg_data)

        if not valid_data_regs:
            raise ValueError("No valid data register found.")

        final_data_reg = random.choice(valid_data_regs)

        self.src2 = f"v{fixed_index_reg}"

        if self.is_load:
            self.des = f"v{final_data_reg}"
            self.src1 = random.choice(["x18", "x19", "x20"])
        else:
            self.src3 = f"v{final_data_reg}"
            self.des = None
            self.src1 = "x21"  # Store vào vùng nhớ trống

        self.type = type_of_ins[Indexed.__name__]

    def generate(self) -> str:
        suffix = ", v0.t" if self.mask else ""
        if self.is_load:
            return f"{self.name} {self.des}, ({self.src1}), {self.src2}{suffix}"
        else:
            return f"{self.name} {self.src3}, ({self.src1}), {self.src2}{suffix}"


# class UnitStrideFaultOnlyFirstLoads(LoadsStores):
#     def __init__(self, name: str, index: int):
#         super().__init__(name, index)
#
#     def generate(self) -> str:
#         ins: str = ""
#         if self.mask:
#             ins = ", v0.t"
#             if self.des == "v0":
#                 self.des = f"v{random.randint(1, 31)}"
#
#         ins = f"{self.name} {self.des}, ({self.src1})" + ins
#         return ins
#
#
# class UnitStrideSegment(LoadsStores):
#     def __init__(self, name: str, index: int):
#         super().__init__(name, index)
#
#         self.src1 = f"x{random.randint(0, 31)}"
#         self.nf = f"{random.randint(2, 8)}"
#         self.eew = f"{random.choice([8, 16, 32])}"
#
#     def generate(self) -> str:
#         return ""
#         ins: str = ""
#         is_ff: bool = random.choice([True, False])
#
#         if self.mask:
#             ins = ", v0.t"
#             if self.des == "v0":
#                 self.des = f"v{random.randint(1, 31)}"
#
#         if len(self.name) <= 6:
#             # self.name in ["vlseg", "vsseg", "vlsseg", "vssseg"]
#             temp = f"{self.name}{self.nf}e{self.eew}"
#             if is_ff and self.name == "vlseg":
#                 temp += "ff"
#             temp += ".v " + f"{self.des}, ({self.src1})"
#
#             if len(self.name) == 6:
#                 temp += f", x{random.randint(0, 31)}"
#         else:
#             temp = f"{self.name}{self.nf}ei{self.eew}.v {self.des}, ({self.src1}), {self.src2}"
#
#         ins = temp + ins
#         return ins
#
#
# class StridedSegment(LoadsStores):
#     def __init__(self, name: str, index: int) -> None:
#         super().__init__(name, index)
#
#     def generate(self) -> str:
#         return ""
#
#
# class IndexedSegment(LoadsStores):
#     def __init__(self, name: str, index: int) -> None:
#         super().__init__(name, index)
#
#     def generate(self) -> str:
#         return ""
#
#
# class WholeRegister(LoadsStores):
#     def __init__(self, name: str, index: int):
#         super().__init__(name, index)
#
#         self.mew = f"{random.choice([1, 2, 4, 8])}"
#         self.width = f"{random.choice([8, 16, 32, 64])}"
#
#     def generate(self) -> str:
#         if self.name == "vs_r.v":
#             ins = f"vs{self.mew}r.v {self.src2}, ({self.src1})"
#         else:
#             ins = f"vl{self.mew}re{self.width}.v {self.src2}, ({self.src1})"
#         return ins
