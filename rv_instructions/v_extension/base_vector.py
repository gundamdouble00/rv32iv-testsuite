import random
from abc import ABC, abstractmethod

from rv_instructions.base_instruction import BaseInstruction
from rv_types.registers import ACTIVE_REG


def vector_reg(lmul: float) -> int:
    step: int = int(lmul)
    if step < 1:
        step = 1
    return random.randrange(start=0, stop=32, step=step)


class BaseVectorIns(BaseInstruction, ABC):
    def __init__(self, name: str, index: int) -> None:
        super().__init__(name, index)

    @abstractmethod
    def generate(self) -> str:
        pass


v_sew: list[int] = [8, 16, 32]
v_lmul: list[float] = [1 / 8, 1 / 4, 1 / 2, 1, 2, 4, 8]
v_tail: list[str] = ["ta", "tu"]
v_mask: list[str] = ["ma", "mu"]

LMUL_STRING = {
    1 / 8: "mf8",
    1 / 4: "mf4",
    1 / 2: "mf2",
    1: "m1",
    2: "m2",
    4: "m4",
    8: "m8",
}


class ConfigurationSetting(BaseVectorIns):
    def __init__(self, name: str, index: int) -> None:
        # vsetvl t0, a3, x0
        # vsetvli t0, a3, e32, m1, ta, ma
        # vsetivli t0, 12, e32, m1, ta, ma

        super().__init__(name, index)
        self.des = ""
        self.src1 = ""
        self.src2 = ""
        self.sew = int(0)
        self.lmul = float(0.0)
        self.tail = ""
        self.mask = ""

        self.des = random.choice(ACTIVE_REG)
        if len(name) <= 7:
            # vsetvl, vsetvli
            self.src1 = random.choice(ACTIVE_REG)
        else:
            # vsetivli
            self.src1 = f"{random.randint(0, 31)}"

        if self.name == "vsetvl":
            self.src2 = "x0"
            return

        vtype: list[str] = []
        while True:
            # LMUL >= SEW/ELEN
            self.sew = random.choice(v_sew)
            self.lmul = random.choice(v_lmul)
            if self.lmul * 32 >= float(self.sew):
                break

        self.tail = random.choice(v_tail)
        self.mask = random.choice(v_mask)

        vtype.append(f"e{self.sew}")
        vtype.append(f"{LMUL_STRING[self.lmul]}")
        vtype.append(self.tail)
        vtype.append(self.mask)
        self.src2 = vtype

    def generate(self) -> str:
        ins = f"{self.name} {self.des}, {self.src1}, "
        for i in range(len(self.src2)):
            field = self.src2[i]
            ins += field
            if i < len(self.src2) - 1:
                ins += ", "

        return ins


class LoadsStores(BaseVectorIns):
    def __init__(self, name: str, index: int, lmul: float, sew: int) -> None:
        if lmul < sew / 32:
            raise ValueError("lmul must be smaller than sew/elen (elen = 32)")

        super().__init__(name, index)

        self.des = ""
        self.src3 = ""
        self.src2 = ""
        self.src1 = ""
        self.sew = sew
        self.lmul = lmul
        self.mask = random.choice([True, False])

    def generate(self) -> str:
        return ""


class IntegerArithmeticIns(BaseVectorIns):
    def __init__(self, name: str, index: int, lmul: float, sew: int) -> None:
        if lmul < sew / 32:
            raise ValueError("lmul must be smaller than sew/elen (elen = 32)")

        super().__init__(name, index)

        self.des = f"v{vector_reg(lmul)}"
        self.src2 = f"v{vector_reg(lmul)}"
        self.src1 = ""
        self.sew = sew
        self.lmul = lmul
        self.mask = random.choice([True, False])

    def generate(self) -> str:
        ins: str = ""
        if self.mask:
            ins = ", v0.t"
        ins = f"{self.name} {self.des}, {self.src2}, {self.src1}" + ins
        return ins
