import random

from rv_instructions.integer.base_integer import BaseIntegerIns


class BTypeIns(BaseIntegerIns):
    def __init__(self, name):
        # name rs1, rs2, offset
        super().__init__(name)

        self.src1 = f"x{random.randint(0, 31)}"
        self.src2 = f"x{random.randint(0, 31)}"

        offset: int = random.randint(-4096, 4094)
        offset += offset % 2
        self.src3 = f"{offset}"

        self.type = "i_b_type"

    def generate(self) -> str:
        return f"{self.name} {self.src1}, {self.src2}, {self.src3}"
