import random

from rv_instructions.integer.base_integer import BaseIntegerIns


class STypeIns(BaseIntegerIns):
    def __init__(self, name: str):
        # sb/sh/sw x12, 14000(x26)
        # name rs2, offset(rs1)
        # rs3 <=> offset
        super().__init__(name)

        self.src1 = f"x{random.randint(0, 31)}"
        self.src2 = f"x{random.randint(0, 31)}"
        self.src3 = f"{random.randint(-2048, 2047)}"

        self.type = "i_s_type"

    def generate(self) -> str:
        # name rs2, offset(rs1)
        return f"{self.name} {self.src2}, {self.src3}({self.src1})"
