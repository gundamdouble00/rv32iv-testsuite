import random

from rv_instructions.integer.base_integer import BaseIntegerIns
from config import PROGRAM_LEN


class BTypeIns(BaseIntegerIns):
    def __init__(self, name: str, index: int):
        # name rs1, rs2, offset
        super().__init__(name, index)

        self.src1 = f"x{random.randint(0, 31)}"
        self.src2 = f"x{random.randint(0, 31)}"

        offset: int = random.randrange(
            -4 * (index - 1), 4 * (PROGRAM_LEN - index) + 1, 4
        )

        self.src3 = f"{offset}"

        self.type = "i_b_type"

    def generate(self) -> str:
        return f"{self.name} {self.src1}, {self.src2}, {self.src3}"
