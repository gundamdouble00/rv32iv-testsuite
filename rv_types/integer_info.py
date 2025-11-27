from rv_instructions.integer.b_type import BTypeIns
from rv_instructions.integer.i_type import ITypeIns
from rv_instructions.integer.j_type import JTypeIns
from rv_instructions.integer.r_type import RTypeIns
from rv_instructions.integer.s_type import STypeIns
from rv_instructions.integer.u_type import UTypeIns

x_registers = []
for i in range(0, 32):
    x_registers.append(f"x{i}")

r_type = ["add", "sub", "sll", "slt", "sltu", "xor", "srl", "sra", "or", "and"]

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
    "ecall",
]

s_type = ["sb", "sh", "sw"]

u_type = ["lui", "auipc"]

b_type = ["beq", "bne", "blt", "bge", "bltu", "bgeu"]

j_type = ["jal"]

i_instructions = r_type + i_type + s_type + u_type + b_type + j_type

class_of_i_instr = {
    "add": RTypeIns,
    "sub": RTypeIns,
    "sll": RTypeIns,
    "slt": RTypeIns,
    "sltu": RTypeIns,
    "xor": RTypeIns,
    "srl": RTypeIns,
    "sra": RTypeIns,
    "or": RTypeIns,
    "and": RTypeIns,
    #
    "addi": ITypeIns,
    "slti": ITypeIns,
    "sltiu": ITypeIns,
    "xori": ITypeIns,
    "ori": ITypeIns,
    "andi": ITypeIns,
    "slli": ITypeIns,
    "srli": ITypeIns,
    "srai": ITypeIns,
    "lb": ITypeIns,
    "lh": ITypeIns,
    "lw": ITypeIns,
    "lbu": ITypeIns,
    "lhu": ITypeIns,
    "jalr": ITypeIns,
    "ecall": ITypeIns,
    #
    "sb": STypeIns,
    "sh": STypeIns,
    "sw": STypeIns,
    #
    "lui": UTypeIns,
    "auipc": UTypeIns,
    #
    "beq": BTypeIns,
    "bne": BTypeIns,
    "blt": BTypeIns,
    "bge": BTypeIns,
    "bltu": BTypeIns,
    "bgeu": BTypeIns,
    #
    "jal": JTypeIns,
}
