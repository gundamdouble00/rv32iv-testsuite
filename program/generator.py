import random

import config
from config import RISCV_INS
from rv_types.integer_info import i_instructions
from rv_types.registers import (
    ACTIVE_REG,
    MEM_REG,
    BYTE_DATA,
    HALF_DATA,
    WORD_DATA,
    SAVED_MEM,
)
from rv_types.riscv_infor import ins_of_type, class_of_instructions
from rv_types.vector_info import configuration_setting

b_ins = [
    "beq",
    "bne",
    "blt",
    "bge",
    "bltu",
    "bgeu",
]


class Program:
    def __init__(self) -> None:
        self.fitness = -1.00
        self.count_ins = {}
        self.lmul = -1
        self.sew = -1

        self.header: list[str] = []
        self.body = []
        self.footer: list[str] = []

        for key in config.RV32.keys():
            self.count_ins[key] = 0

    def __len__(self) -> int:
        return len(self.body)

    def update_numbers_ins(self) -> None:
        for key in config.RV32.keys():
            self.count_ins[key] = 0
        for ins in self.body:
            self.count_ins[ins.type] += 1

    def to_assembly(self):
        assembly_program: list[str] = []
        for rv_ins in self.body:
            assembly_program.append(rv_ins.generate())

        return assembly_program


def random_data() -> None:
    half_data: str = ""
    for _ in range(50):
        num: int = random.randint(-(2**16), 2**16 - 1)
        half_data += hex(num) + ", "

    print(half_data)


def generate_data(type_mem: str, rv32: Program):
    data_string: str = f"{type_mem}_data: .{type_mem} "

    bits: int = config.MEM_REGION[type_mem]["bits"]
    numbers: int = config.MEM_REGION[type_mem]["numbers"]
    for i in range(numbers):
        num: int = random.randint(-(2**bits), 2**bits - 1)
        data_string += hex(num)
        if i + 1 < numbers:
            data_string += ", "

    rv32.header.append(data_string)
    rv32.header.append(".align 4")


def get_base_address(rv32: Program, region: str):
    lui: str = f"lui {MEM_REG[region]}, %hi({region})"
    addi: str = f"addi {MEM_REG[region]}, {MEM_REG[region]}, %lo({region})"

    rv32.header.append(lui)
    rv32.header.append(addi)
    # rv32.header.append("\n")


def generate_header(rv32: Program):
    rv32.header.append(".data")
    rv32.header.append("blank_mem: .space 16384")
    for key in config.MEM_REGION.keys():
        generate_data(key, rv32)

    indexed_offsets: str = "indexed: .word "
    for i in range(140):
        offset: int = random.randrange(0, 256, 4)
        indexed_offsets += hex(offset)
        if i + 1 < 140:
            indexed_offsets += ", "
    rv32.header.append(indexed_offsets)
    rv32.header.append(".align 4")
    rv32.header.append("saved_mem: .space 16384")

    rv32.header.append(".text")
    rv32.header.append(".globl main")
    rv32.header.append("main:")

    for register in ACTIVE_REG:
        imm: int = random.randint(0, 1048575)
        rv32.header.append(f"lui {register}, {imm}")

    get_base_address(rv32, BYTE_DATA)
    get_base_address(rv32, HALF_DATA)
    get_base_address(rv32, WORD_DATA)
    get_base_address(rv32, SAVED_MEM)

    if RISCV_INS["v"]:
        rv32.header.append(f"lui x22, %hi(indexed)")
        rv32.header.append(f"addi x22, x22, %lo(indexed)")
        rv32.header.append(f"vsetvli {random.choice(ACTIVE_REG)}, x1, e32, m8, tu, ma")
        rv32.header.append("vle32.v v24, (x22)")
        rv32.header.append(f"addi x22, x0, {random.randrange(-128, 129, 4)}")

    # return rv32.header


def generate_footer(rv32: Program):
    rv32.footer.append("end:")
    rv32.footer.append("li a7, 93")
    rv32.footer.append("li a0, 0")
    rv32.footer.append("ecall")

    rv32.footer.append("extra_func:")
    reg1: str = random.choice(ACTIVE_REG)
    while reg1 == "x12":
        reg1 = random.choice(ACTIVE_REG)

    reg2: str = random.choice(ACTIVE_REG)
    while reg2 in {"x12", reg1}:
        reg2 = random.choice(ACTIVE_REG)

    imm1: int = random.randint(0, 13)
    imm2: int = random.randint(14, 26)
    rv32.footer.append(f"addi {reg1}, x0, {imm1}")
    rv32.footer.append(f"addi {reg2}, x0, {imm2}")
    rv32.footer.append("loop1:")
    rv32.footer.append(f"add {reg1}, {reg1}, 1")

    rv32.footer.append(f"blt {reg1}, {reg2}, loop1")
    rv32.footer.append("jalr x0, 0(x12)")

    # return rv32.footer


def generate_obj(name: str, index: int, lmul: float, sew: int):
    riscv_class = class_of_instructions[name]
    try:
        if name in i_instructions:
            riscv_obj = riscv_class(name, index)
        else:
            riscv_obj = riscv_class(name, index, lmul, sew)
    except ValueError:
        return None
    else:
        return riscv_obj


def generate_random_program(length: int):
    asm_program = Program()
    generate_header(asm_program)
    generate_footer(asm_program)

    temp_program: list[str] = []
    for key, val in config.RV32.items():
        if val == 0 or (not RISCV_INS[key[0]]):
            continue

        instructions: list[str] = ins_of_type[key]
        ins_list: list[str] = []
        for _ in range(val):
            riscv_ins: str = random.choice(instructions)
            ins_list.append(riscv_ins)
        temp_program.extend(ins_list)

    random.shuffle(temp_program)

    sew_flag: int = 32
    lmul_flag: float = 8.0
    for ins in temp_program:
        body_length = len(asm_program.body)
        riscv_obj = generate_obj(ins, body_length, lmul_flag, sew_flag)
        if riscv_obj is not None:
            asm_program.body.append(riscv_obj)
            if ins in configuration_setting:
                sew_flag = riscv_obj.sew
                lmul_flag = riscv_obj.lmul

    while len(asm_program.body) < length:
        temp_type = random.choice(list(config.RV32.keys()))
        if config.RV32[temp_type] == 0 or (not RISCV_INS[temp_type[0]]):
            continue
        instructions: list[str] = ins_of_type[temp_type]
        riscv_ins: str = random.choice(instructions)

        riscv_obj = generate_obj(riscv_ins, len(asm_program.body), lmul_flag, sew_flag)
        if riscv_obj is not None:
            asm_program.body.append(riscv_obj)
            if riscv_ins in configuration_setting:
                sew_flag = riscv_obj.sew
                lmul_flag = riscv_obj.lmul

    # for ins in asm_program.body:
    #     print(ins.generate())

    return asm_program
