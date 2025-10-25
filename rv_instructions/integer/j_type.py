import random

from rv_instructions.integer.base_integer import BaseIntegerIns


class JTypeIns(BaseIntegerIns):
    def __init__(self, name):
        super().__init__(name)

        # jal rd, offset
        self.des = f"x{random.randint(0, 31)}"
        offset = random.randint(-1048576, 1048574)
        offset += offset % 2
        self.src3 = f"{offset}"

        self.type = "i_j_type"

    def generate(self) -> str:
        return f"{self.name} {self.des}, {self.src3}"
