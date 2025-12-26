import random

from config import MEM_REGION
from rv_instructions.integer.base_integer import BaseIntegerIns
from rv_types.instruction_type import type_of_ins


class STypeIns(BaseIntegerIns):
    def __init__(self, name: str, index: int) -> None:
        super().__init__(name, index)

        # sb rs2, offset(rs1)
        self.src1 = "x21"
        self.src2 = f"x{random.randint(0, 31)}"

        if self.name == "sb":
            key, step = "byte", 1
        elif self.name == "sh":
            key, step = "half", 2
        else:
            key, step = "word", 4

        last_addr: int = MEM_REGION[key]["numbers"] * MEM_REGION[key]["bits"]
        self.src3 = f"{random.randrange(0, min(2047, last_addr + 1), step)}"

        class_name: str = STypeIns.__name__
        self.type = type_of_ins[class_name]

    def generate(self) -> str:
        # name rs2, offset(rs1)
        return f"{self.name} {self.src2}, {self.src3}({self.src1})"
