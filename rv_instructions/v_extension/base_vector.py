from abc import ABC, abstractmethod

import types.vector_info
from rv_instructions.base_instruction import BaseInstruction
import utils.random_value
import random


class BaseVectorIns(BaseInstruction, ABC):
    def __init__(self, name: str, index: int):
        super().__init__(name, index)

    @abstractmethod
    def generate(self) -> str:
        pass


class IntegerArithmeticIns(BaseVectorIns):
    def __init__(self, name: str, index: int):
        super().__init__(name, index)

        self.des = utils.random_value.random_register("v")
        self.src2 = utils.random_value.random_register("v")
        self.src1 = utils.random_value.random_src1(name[len(name) - 1], -16, 15)
        self.mask = random.choice([True, False])

    def generate(self) -> str:
        instruction: str = ""
        if self.mask:
            instruction = ", v0.t"
            if self.name not in types.vector_info.integer_compare and self.des == "v0":
                self.des = f"v{random.randint(1, 31)}"

        instruction = f"{self.name} {self.des}, {self.src2}, {self.src1}" + instruction
        return instruction


class LoadsStores(BaseVectorIns):
    def __init__(self, name: str, index: int):
        super().__init__(name, index)

        self.des = f"v{random.randint(0, 31)}"
        self.src2 = f"v{random.randint(0, 31)}"
        self.src1 = f"x{random.randint(0, 31)}"
        self.mask = random.choice([True, False])

    def generate(self) -> str:
        return ""


class ConfigurationSetting(BaseVectorIns):
    def __init__(self, name: str, index: int):
        super().__init__(name, index)

        self.des = f"x{random.randint(0, 31)}"
        if len(name) <= 7:
            # name == vsetvl
            self.src1 = f"x{random.randint(0, 31)}"
        else:
            self.src1 = f"{random.randint(0, 31)}"

        vtype: list[str] = []
        sew = random.choice(types.vector_info.SEW)
        lmul = random.choice(types.vector_info.LMUL)
        tail = random.choice(types.vector_info.TAIL)
        mask = random.choice(types.vector_info.MASK)

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
