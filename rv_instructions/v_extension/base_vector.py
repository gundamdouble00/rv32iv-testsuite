import random
from abc import ABC, abstractmethod

from rv_instructions.base_instruction import BaseInstruction
from rv_types.registers import ACTIVE_REG


def vector_reg(lmul: int) -> int:
    return random.randrange(0, 32, lmul)


class BaseVectorIns(BaseInstruction, ABC):
    def __init__(self, name: str, index: int, lmul: int, sew: int) -> None:
        super().__init__(name, index)
        self.lmul = lmul
        self.sew = sew

    @abstractmethod
    def generate(self) -> str:
        pass


class IntegerArithmeticIns(BaseVectorIns):
    def __init__(self, name: str, index: int, lmul: int, sew: int) -> None:
        super().__init__(name, index, lmul, sew)

        self.des = f"v{vector_reg(lmul)}"
        self.src2 = f"v{vector_reg(lmul)}"
        self.src1 = ""
        self.mask = random.choice([True, False])

    def generate(self) -> str:
        ins: str = ""
        if self.mask:
            ins = ", v0.t"
        ins = f"{self.name} {self.des}, {self.src2}, {self.src1}" + ins
        return ins


class LoadsStores(BaseVectorIns):
    def __init__(self, name: str, index: int, lmul: int, sew: int) -> None:
        super().__init__(name, index, lmul, sew)

        self.des = ""
        self.src2 = ""
        self.src1 = ""
        self.mask = random.choice([True, False])

    def generate(self) -> str:
        return ""


v_sew: list[str] = ["e8", "e16", "e32"]
v_lmul: list[str] = ["mf8", "mf4", "mf2", "m1", "m2", "m4", "m8"]
v_tail: list[str] = ["ta", "tu"]
v_mask: list[str] = ["ma", "mu"]


class ConfigurationSetting(BaseVectorIns):
    def __init__(self, name: str, index: int, lmul: int, sew: int) -> None:
        # vsetvl t0, a3, x0
        # vsetvli t0, a3, e32, m1, ta, ma
        # vsetivli t0, 12, e32, m1, ta, ma

        super().__init__(name, index, lmul, sew)

        self.des = f"{random.choice(ACTIVE_REG)}"
        if len(name) <= 7:
            # vsetvl, vsetvli
            self.src1 = f"{random.choice(ACTIVE_REG)}"
        else:
            # vsetivli
            self.src1 = f"{random.randint(0, 31)}"

        vtype: list[str] = []
        sew = random.choice(v_sew)
        lmul = random.choice(v_lmul)
        tail = random.choice(v_tail)
        mask = random.choice(v_mask)

        if len(name) == 6:
            # name == vsetvl
            vtype.append("x0")
        else:
            vtype.append(sew)
            vtype.append(lmul)
            vtype.append(tail)
            vtype.append(mask)
        self.src2 = vtype

    def generate(self) -> str:
        ins = f"{self.name} {self.des}, {self.src1}, "
        for i in range(len(self.src2)):
            field = self.src2[i]
            ins += field
            if i < len(self.src2) - 1:
                ins += ", "

        return ins
