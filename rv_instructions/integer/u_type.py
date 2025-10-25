import random

from rv_instructions.integer.base_integer import BaseIntegerIns


class UTypeIns(BaseIntegerIns):
    def __init__(self, name):
        super().__init__(name)

        # lui/auipc rd, imm
        self.des = f"x{random.randint(0, 31)}"
        self.src3 = f"{random.randint(0, 1048575)}"

        self.type = "i_u_type"

    def generate(self) -> str:
        # auipc rd, imm
        # lui rd, imm
        return f"{self.name} {self.des}, {self.src3}"
