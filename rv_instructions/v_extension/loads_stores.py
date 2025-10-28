import random
from operator import truediv

import types.vector_info
from rv_instructions.v_extension.base_vector import LoadsStores


class UnitStride(LoadsStores):
    def __init__(self, name: str, index: int):
        super().__init__(name, index)

    def generate(self) -> str:
        ins: str = ""
        if self.mask and self.name not in ("vlm.v", "vsm.v"):
            ins = ", v0.t"
            if self.des == "v0":
                self.des = f"v{random.randint(1, 31)}"

        ins = f"{self.name} {self.des}, ({self.src1})" + ins
        return ins


class Strided(LoadsStores):
    def __init__(self, name: str, index: int):
        super().__init__(name, index)

        self.src2 = f"x{random.randint(0, 31)}"

    def generate(self) -> str:
        ins: str = ""
        if self.mask:
            ins = ", v0.t"
            if self.des == "v0":
                self.des = f"v{random.randint(1, 31)}"
        ins = f"{self.name} {self.des}, ({self.src1}), {self.src2}" + ins
        return ins


class Indexed(LoadsStores):
    def __init__(self, name: str, index: int):
        super().__init__(name, index)

        # self.src2 = f"v{random.randint(0, 31)}"

    def generate(self) -> str:
        ins: str = ""
        if self.mask:
            ins = ", v0.t"
            if self.des == "v0":
                self.des = f"v{random.randint(1, 31)}"
        ins = f"{self.name} {self.des}, ({self.src1}), {self.src2}" + ins
        return ins


class UnitStrideFaultOnlyFirstLoads(LoadsStores):
    def __init__(self, name: str, index: int):
        super().__init__(name, index)

    def generate(self) -> str:
        ins: str = ""
        if self.mask:
            ins = ", v0.t"
            if self.des == "v0":
                self.des = f"v{random.randint(1, 31)}"

        ins = f"{self.name} {self.des}, ({self.src1})" + ins
        return ins


class LoadStoreSegment(LoadsStores):
    def __init__(self, name: str, index: int):
        super().__init__(name, index)

        self.src1 = f"x{random.randint(0, 31)}"
        self.nf = f"{random.randint(2, 8)}"
        self.eew = f"{random.choice([8, 16, 32])}"

    def generate(self) -> str:
        # vlseg<nf>e<eew>.v vd, (rs1), vm (Unit-stride segment load template)
        # vsseg<nf>e<eew>.v vs3, (rs1), vm  (Unit-stride segment store template)
        # vlseg<nf>e<eew>ff.v vd, (rs1), vm  (Unit-stride fault-only-first segment loads)

        # vlsseg<nf>e<eew>.v vd, (rs1), rs2, vm (Strided segment loads)
        # vssseg<nf>e<eew>.v vs3, (rs1), rs2, vm  (Strided segment stores)

        # vluxseg<nf>ei<eew>.v vd, (rs1), vs2, vm (Indexed-unordered segment loads)
        # vloxseg<nf>ei<eew>.v vd, (rs1), vs2, vm  (Indexed-ordered segment loads)
        # vsuxseg<nf>ei<eew>.v vs3, (rs1), vs2, vm  (Indexed-unordered segment stores)
        # vsoxseg<nf>ei<eew>.v vs3, (rs1), vs2, vm  (Indexed-ordered segment stores)

        ins: str = ""
        is_ff: bool = random.choice([True, False])

        if self.mask:
            ins = ", v0.t"
            if self.des == "v0":
                self.des = f"v{random.randint(1, 31)}"

        if len(self.name) <= 6:
            # self.name in ["vlseg", "vsseg", "vlsseg", "vssseg"]
            temp = f"{self.name}{self.nf}e{self.eew}"
            if is_ff and self.name == "vlseg":
                temp += "ff"
            temp += ".v " + f"{self.des}, ({self.src1})"

            if len(self.name) == 6:
                temp += f", x{random.randint(0, 31)}"
        else:
            temp = f"{self.name}{self.nf}ei{self.eew}.v {self.des}, ({self.src1}), {self.src2}"

        ins = temp + ins
        return ins


class LoadStoreWholeRegister(LoadsStores):
    def __init__(self, name: str, index: int):
        super().__init__(name, index)

        self.mew = f"{random.choice([1, 2, 4, 8])}"
        self.width = f"{random.choice([8, 16, 32, 64])}"

    def generate(self) -> str:
        if self.name == "vs_r.v":
            ins = f"vs{self.mew}r.v {self.src2}, ({self.src1})"
        else:
            ins = f"vl{self.mew}re{self.width}.v {self.src2}, ({self.src1})"
        return ins
