import random

import utils.random_value
from rv_instructions.v_extension.base_vector import IntegerArithmeticIns


class SingleWidthIntegerAddSub(IntegerArithmeticIns):
    def __init__(self, name: str):
        super().__init__(name)


class BitwiseLogical(IntegerArithmeticIns):
    def __init__(self, name: str):
        super().__init__(name)


class SingleWidthShift(IntegerArithmeticIns):
    def __init__(self, name: str):
        super().__init__(name)

        if name[len(name) - 1] == "i":
            self.src1 = f"{random.randint(0, 31)}"


class IntegerCompare(IntegerArithmeticIns):
    def __init__(self, name):
        super().__init__(name)


class MinMax(IntegerArithmeticIns):
    def __init__(self, name):
        super().__init__(name)


class IntegerMerge(IntegerArithmeticIns):
    def __init__(self, name):
        super().__init__(name)

        len_of_name: int = len(name)
        self.src1 = utils.random_value.random_src1(name[len_of_name - 2], -16, 15)

    def generate(self) -> str:
        if self.des == "v0":
            self.des = f"v{random.randint(1, 31)}"
        return f"{self.name} {self.des}, {self.src2}, {self.src1}, v0"


class IntegerMove(IntegerArithmeticIns):
    def __init__(self, name):
        super().__init__(name)

        len_of_name: int = len(name)
        self.src1 = utils.random_value.random_src1(name[len_of_name - 1], -16, 15)

    def generate(self) -> str:
        return f"{self.name} {self.des}, {self.src1}"


class WideningIntegerAddSubtract(IntegerArithmeticIns):
    def __init__(self, name: str):
        super().__init__(name)

        self.random_v_reg = random.randint(0, 31)
        self.des = f"v{self.random_v_reg}"
        self.src2 = f"v{(self.random_v_reg + 1) % 32}"
        self.src1 = f"{name[len(name) - 1]}{(self.random_v_reg + 2) % 32}"

    def generate(self) -> str:
        instruction: str = ""
        if self.mask:
            instruction = ", v0.t"
            if self.des == "v0":
                self.des = f"v{(self.random_v_reg + 3) % 32}"

        instruction = f"{self.name} {self.des}, {self.src2}, {self.src1}" + instruction
        return instruction


class VectorIntegerExtension(IntegerArithmeticIns):
    def __init__(self, name: str):
        super().__init__(name)

    def generate(self) -> str:
        ins: str = ""
        if self.mask:
            ins = ", v0.t"
            if self.des == "v0":
                self.des = f"v{random.randint(1, 31)}"

        ins = f"{self.name} {self.des}, {self.src2}" + ins
        return ins


class NarrowingIntegerRightShift(IntegerArithmeticIns):
    def __init__(self, name: str):
        super().__init__(name)
        self.src1 = utils.random_value.random_src1(name[len(name) - 1], 0, 31)

    def generate(self):
        ins: str = ""
        if self.mask:
            ins = ", v0.t"
            if self.des == "v0":
                self.des = f"v{random.randint(1, 31)}"

        ins = f"{self.name} {self.des}, {self.src2}, {self.src1}" + ins
        return ins


class SingleWidthIntegerMultiply(IntegerArithmeticIns):
    def __init__(self, name: str):
        super().__init__(name)


class IntegerDivide(IntegerArithmeticIns):
    def __init__(self, name: str):
        super().__init__(name)


class WideningIntegerMultiply(IntegerArithmeticIns):
    def __init__(self, name: str):
        super().__init__(name)

        self.random_v_reg = random.randint(0, 31)
        self.des = f"v{self.random_v_reg}"
        self.src2 = f"v{(self.random_v_reg + 1) % 32}"
        self.src1 = f"{name[len(name) - 1]}{(self.random_v_reg + 2) % 32}"

    def generate(self) -> str:
        instruction: str = ""
        if self.mask:
            instruction = ", v0.t"
            if self.des == "v0":
                self.des = f"v{(self.random_v_reg + 3) % 32}"

        instruction = f"{self.name} {self.des}, {self.src2}, {self.src1}" + instruction
        return instruction


class SingleWidthIntegerMultiplyAdd(IntegerArithmeticIns):
    def __init__(self, name: str):
        super().__init__(name)

    def generate(self) -> str:
        ins: str = ""
        if self.mask:
            ins = ", v0.t"
            if self.des == "v0":
                self.des = f"v{random.randint(1, 31)}"

        ins = f"{self.name} {self.des}, {self.src1}, {self.src2}" + ins
        return ins


class WideningIntegerMultiplyAdd(IntegerArithmeticIns):
    def __init__(self, name: str):
        super().__init__(name)

        self.random_v_reg = random.randint(0, 31)
        self.des = f"v{self.random_v_reg}"
        self.src2 = f"v{(self.random_v_reg + 1) % 32}"
        self.src1 = f"{name[len(name) - 1]}{(self.random_v_reg + 2) % 32}"

    def generate(self) -> str:
        instruction: str = ""
        if self.mask:
            instruction = ", v0.t"
            if self.des == "v0":
                self.des = f"v{(self.random_v_reg + 3) % 32}"

        instruction = f"{self.name} {self.des}, {self.src1}, {self.src2}" + instruction
        return instruction
