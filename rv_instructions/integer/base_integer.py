from abc import ABC, abstractmethod

from rv_instructions.base_instruction import BaseInstruction


class BaseIntegerIns(BaseInstruction, ABC):
    def __init__(self, name: str):
        super().__init__(name)

        self.des = ""
        self.src1 = ""
        self.src2 = ""
        self.src3 = ""

    @abstractmethod
    def generate(self) -> str:
        pass
