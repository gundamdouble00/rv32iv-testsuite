from rv_instructions.integer.b_type import BTypeIns
from rv_instructions.integer.i_type import ITypeIns
from rv_instructions.integer.j_type import JTypeIns
from rv_instructions.integer.r_type import RTypeIns
from rv_instructions.integer.s_type import STypeIns
from rv_instructions.integer.u_type import UTypeIns

x_registers = []
class_of_integer = {}
i_instructions: list[str] = []

for i in range(0, 32):
    x_registers.append(f"x{i}")

def class_and_list(i_ins: list[str], class_of_ins) -> None:
    for instruction in i_ins:
        class_of_integer[instruction] = class_of_ins

    i_instructions.extend(i_ins)

r_type = [
    "add",
    "sub",
    "sll",
    "slt",
    "sltu",
    "xor",
    "srl",
    "sra",
    "or",
    "and",
]
class_and_list(r_type, RTypeIns)

i_type = [
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
    "jalr",
    # "ecall",
]
class_and_list(i_type, ITypeIns)

s_type = [
    "sb",
    "sh",
    "sw",
]
class_and_list(s_type, STypeIns)

u_type = [
    "lui",
    "auipc",
]
class_and_list(u_type, UTypeIns)

b_type = [
    "beq",
    "bne",
    "blt",
    "bge",
    "bltu",
    "bgeu",
]
class_and_list(b_type, BTypeIns)

j_type = [
    "jal",
]
class_and_list(j_type, JTypeIns)

