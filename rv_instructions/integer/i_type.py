import random

from rv_instructions.integer.base_integer import BaseIntegerIns


class ITypeIns(BaseIntegerIns):
    def __init__(self, name: str):
        super().__init__(name)

        if name != "ecall":
            self.des = f"x{random.randint(0, 31)}"
            self.src1 = f"x{random.randint(0, 31)}"
            if name[0] == "s":
                # immediate of slli, srli, srai
                self.src2 = f"{random.randint(0, 31)}"
            else:
                # immediate of addi, slti, sltiu, xori, ori, andi, lb, lh, lw, lbu, lhu, jalr
                self.src2 = f"{random.randint(-2048, 2047)}"

        self.type = "i_i_type"

    def generate(self) -> str:
        if self.name == "ecall":
            return "ecall"

        if self.name[0] in "lj":
            # instruction rd, offset(rs1)
            ins = f"{self.name} {self.des}, {self.src2}({self.src1})"
        else:
            # instruction rd, rs1, imm
            ins = f"{self.name} {self.des}, {self.src1}, {self.src2}"

        return ins
