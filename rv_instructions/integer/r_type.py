import random

import types.integer_info
from rv_instructions.integer.base_integer import BaseIntegerIns


class RTypeIns(BaseIntegerIns):
    def __init__(self, name: str):
        super().__init__(name)

        self.des = f"x{random.randint(0, 31)}"
        self.src1 = f"x{random.randint(0, 31)}"
        self.src2 = f"x{random.randint(0, 31)}"

        self.type = "i_r_type"

    def generate(self) -> str:
        # instruction rd, rs1, rs2
        return f"{self.name} {self.des}, {self.src1}, {self.src2}"
