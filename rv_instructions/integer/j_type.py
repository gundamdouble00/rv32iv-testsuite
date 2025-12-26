from rv_instructions.integer.base_integer import BaseIntegerIns
from rv_types.instruction_type import type_of_ins


class JTypeIns(BaseIntegerIns):
    def __init__(self, name: str, index: int) -> None:
        super().__init__(name, index)

        # jal extra_func
        self.des = "x12"
        class_name: str = JTypeIns.__name__
        self.type = type_of_ins[class_name]

    def generate(self) -> str:
        return f"{self.name} {self.des}, extra_func"
