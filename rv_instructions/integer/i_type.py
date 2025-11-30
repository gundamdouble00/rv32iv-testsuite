import random

from rv_instructions.integer.base_integer import BaseIntegerIns
from rv_types.registers import ACTIVE_REG, MEM_REG, BYTE_DATA, HALF_DATA, WORD_DATA
from config import MEM_REGION


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
        self.src1 = random.choice(ACTIVE_REG)
        if self.name[0] in {"slli", "srli", "srai"}:
            imm = random.randint(0, 31)
        else:
            imm = random.randint(-2048, 2047)
        self.src3 = f"{imm}"

    def __init__(self, name: str, index: int) -> None:
        super().__init__(name, index)
        self.des = random.choice(ACTIVE_REG)
        class_name: str = ITypeIns.__name__
        self.type = class_name

        if self.name == "jalr":
            # jalr
            self._jalr_ins()
            return

        if self.name[0] == "l":
            # lb, lbu, lh, lhu, lw
            self._load_ins()
            return

        # addi, andi, ori, xori, slti, sltiu
        # slli, srli, srai
        self._alu_ins()

        # if name != "ecall":
        #     self.des = f"x{random.randint(0, 31)}"
        #     self.src1 = f"x{random.randint(0, 31)}"
        #     if name[0] == "s":
        #         # immediate of slli, srli, srai
        #         self.src2 = f"{random.randint(0, 31)}"
        #     else:
        #         # immediate of addi, slti, sltiu, xori, ori, andi, lb, lh, lw, lbu, lhu, jalr
        #         self.src2 = f"{random.randint(-2048, 2047)}"

    def generate(self) -> str:
        # if self.name == "ecall":
        #     return "ecall"

        if self.name[0] in {"l", "j"}:
            # instruction rd, offset(rs1)
            ins = f"{self.name} {self.des}, {self.src3}({self.src1})"
        else:
            # instruction rd, rs1, imm
            ins = f"{self.name} {self.des}, {self.src1}, {self.src3}"

        return ins
