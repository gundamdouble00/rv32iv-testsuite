from abc import ABC, abstractmethod

from rv_instructions.base_instruction import BaseInstruction


class BaseIntegerIns(BaseInstruction, ABC):
    def __init__(self, name: str, index: int) -> None:
        super().__init__(name, index)

        self.des = ""  # Destination register
        self.src1 = ""  # Register source 1
        self.src2 = ""  # Register source 2
        self.src3 = ""  # Offset or immediate

    @abstractmethod
    def generate(self) -> str:
        pass
