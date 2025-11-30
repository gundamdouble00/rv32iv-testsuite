import random
from abc import ABC, abstractmethod

import utils.random_value
from rv_instructions.base_instruction import BaseInstruction


class BaseVectorIns(BaseInstruction, ABC):
    def __init__(self, name: str, index: int) -> None:
        super().__init__(name, index)

    @abstractmethod
    def generate(self) -> str:
        pass


class IntegerArithmeticIns(BaseVectorIns):
    def __init__(self, name: str, index: int) -> None:
        super().__init__(name, index)

        self.des = utils.random_value.random_register("v")
        self.src2 = utils.random_value.random_register("v")
        self.src1 = utils.random_value.random_src1(name[len(name) - 1], -16, 15)
        self.mask = random.choice([True, False])

    def generate(self) -> str:
        # instruction: str = ""
        # if self.mask:
        #     instruction = ", v0.t"
        #     if self.name not in types.vector_info.integer_compare and self.des == "v0":
        #         self.des = f"v{random.randint(1, 31)}"

        # instruction = f"{self.name} {self.des}, {self.src2}, {self.src1}" + instruction
        # return instruction
        return ""


class LoadsStores(BaseVectorIns):
    def __init__(self, name: str, index: int) -> None:
        super().__init__(name, index)

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
    def __init__(self, name: str, index: int) -> None:
        super().__init__(name, index)

        self.des = f"x{random.randint(0, 31)}"
        if len(name) <= 7:
            # name == vsetvl
            self.src1 = f"x{random.randint(0, 31)}"
        else:
            self.src1 = f"{random.randint(0, 31)}"

        vtype: list[str] = []
        sew = random.choice(v_sew)
        lmul = random.choice(v_lmul)
        tail = random.choice(v_tail)
        mask = random.choice(v_mask)

        if len(name) == 6:
            # name == vsetvl
            # src3 = register x
            vtype.append(f"x{random.randint(0, 31)}")
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
