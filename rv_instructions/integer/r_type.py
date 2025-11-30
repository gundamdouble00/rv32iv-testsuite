import random

from rv_instructions.integer.base_integer import BaseIntegerIns
from rv_types.registers import ACTIVE_REG
from rv_types.riscv_infor import type_of_ins


class RTypeIns(BaseIntegerIns):
    def __init__(self, name: str, index: int) -> None:
        super().__init__(name, index)

        self.des = f"{random.choice(ACTIVE_REG)}"
        self.src1 = f"x{random.choice(ACTIVE_REG)}"
        self.src2 = f"x{random.choice(ACTIVE_REG)}"

        class_name: str = RTypeIns.__name__
        self.type = type_of_ins[class_name]

    def generate(self) -> str:
        # instruction rd, rs1, rs2
        return f"{self.name} {self.des}, {self.src1}, {self.src2}"
