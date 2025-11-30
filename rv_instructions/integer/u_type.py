import random

from rv_instructions.integer.base_integer import BaseIntegerIns
from rv_types.registers import ACTIVE_REG
from rv_types.riscv_infor import type_of_ins


class UTypeIns(BaseIntegerIns):
    def __init__(self, name: str, index: int) -> None:
        super().__init__(name, index)

        # lui/auipc rd, imm
        self.des = f"{random.choice(ACTIVE_REG)}"
        self.src3 = f"{random.randint(0, 1048575)}"

        class_name: str = UTypeIns.__name__
        self.type = type_of_ins[class_name]

    def generate(self) -> str:
        # lui/auipc rd, imm
        return f"{self.name} {self.des}, {self.src3}"
