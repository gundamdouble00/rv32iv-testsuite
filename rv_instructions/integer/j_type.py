import random

from rv_instructions.integer.base_integer import BaseIntegerIns
from config import PROGRAM_LEN
from rv_types.riscv_infor import type_of_ins


class JTypeIns(BaseIntegerIns):
    def __init__(self, name: str, index: int) -> None:
        super().__init__(name, index)

        # jal extra_func
        class_name: str = JTypeIns.__name__
        self.type = type_of_ins[class_name]

    def generate(self) -> str:
        return f"{self.name} extra_func"
