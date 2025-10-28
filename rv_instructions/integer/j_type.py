import random

from rv_instructions.integer.base_integer import BaseIntegerIns
from config import PROGRAM_LEN


class JTypeIns(BaseIntegerIns):
    def __init__(self, name: str, index: int):
        super().__init__(name, index)

        # jal rd, offset
        self.des = f"x{random.randint(0, 31)}"
        offset = random.randrange(4, 4 * (PROGRAM_LEN - index) + 1, 4)
        self.src3 = f"{offset}"

        self.type = "i_j_type"

    def generate(self) -> str:
        return f"{self.name} {self.des}, {self.src3}"
