import random

from rv_instructions.integer.base_integer import BaseIntegerIns
from rv_types.instruction_type import type_of_ins
from rv_types.registers import ACTIVE_REG, MEM_REG, BYTE_DATA, HALF_DATA, WORD_DATA
from config import MEM_REGION

immediate_ins = [
    "addi",
    "slti",
    "sltiu",
    "xori",
    "ori",
    "andi",
    "slli",
    "srli",
    "srai",
    "lb",
    "lh",
    "lw",
    "lbu",
    "lhu",
    # "jalr",
    # "ecall",
]


class ITypeIns(BaseIntegerIns):
    def _jalr_ins(self) -> None:
        # jalr rd, offset(rs1)
        # jalr x0, 0(x1)
        self.des = "x0"
        self.src1 = "x1"
        self.src3 = "0"

    def _load_ins(self) -> None:
        # lb/lbu/lh/lhu/lw rd, offset(rs1)
        if self.name in {"lb", "lbu"}:
            rs1 = MEM_REG[BYTE_DATA]
            address: int = MEM_REGION["byte"]["numbers"] * 8
            offset = random.randrange(0, address + 1)
        elif self.name in {"lh", "lhu"}:
            rs1 = MEM_REG[HALF_DATA]
            address: int = MEM_REGION["half"]["numbers"] * 16
            offset = random.randrange(0, address + 1, 2)
        else:
            rs1 = MEM_REG[WORD_DATA]
            address: int = MEM_REGION["word"]["numbers"] * 32
            offset = random.randrange(0, address + 1, 4)

        self.src1 = rs1
        self.src3 = f"{offset}"

    def _alu_ins(self):
        # addi rd, rs1, imm
        # andi rd, rs1, imm
        step: int = 1
        start: int = -2048
        stop: int = 2048

        if self.name in {"addi", "subi"}:
            self.des = random.choice([self.des, "x22"])

        self.src1 = random.choice(ACTIVE_REG)
        if self.des == "x22":
            self.src1 = "x0"
            start = -128
            stop = 128
            step = 4

        if self.name in {"slli", "srli", "srai"}:
            imm = random.randint(0, 31)
        else:
            imm = random.randrange(start, stop, step)
        self.src3 = f"{imm}"

    def __init__(self, name: str, index: int) -> None:
        super().__init__(name, index)
        self.des = random.choice(ACTIVE_REG)
        class_name: str = ITypeIns.__name__
        self.type = type_of_ins[class_name]

        if self.name == "jalr":
            self.name = random.choice(immediate_ins)

        if self.name[0] == "l":
            # lb, lbu, lh, lhu, lw
            self._load_ins()
            return

        # addi, andi, ori, xori, slti, sltiu
        # slli, srli, srai
        self._alu_ins()

    def generate(self) -> str:
        if self.name[0] in {"l", "j"}:
            # instruction rd, offset(rs1)
            return f"{self.name} {self.des}, {self.src3}({self.src1})"
        # instruction rd, rs1, imm
        return f"{self.name} {self.des}, {self.src1}, {self.src3}"
