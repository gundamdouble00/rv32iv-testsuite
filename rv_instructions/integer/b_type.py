import random

from rv_instructions.integer.base_integer import BaseIntegerIns
from rv_types.registers import ACTIVE_REG
from rv_types.riscv_infor import type_of_ins


class BTypeIns(BaseIntegerIns):
    def __init__(self, name: str, index: int) -> None:
        # name rs1, rs2, offset/label
        super().__init__(name, index)

        self.src1 = f"{random.choice(ACTIVE_REG)}"
        self.src2 = f"{random.choice(ACTIVE_REG)}"
        class_name: str = BTypeIns.__name__
        self.type = type_of_ins[class_name]

    def generate(self) -> str:
        return f"{self.name} {self.src1}, {self.src2}, {self.src3}"
