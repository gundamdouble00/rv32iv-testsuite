import random
import config
from types.integer_info import i_instructions
from types.vector_info import v_instructions
from types.riscv_infor import class_of_instructions, risc_v_instructions

rate_of_integer = {}
rate_of_vector = {}


class Program:
    def __init__(self, instructions):
        self.instructions = instructions
        self.fitness_score = float(-1)

    def __len__(self):
        return len(self.instructions)

    def to_assembly(self):
        assembly_program: list[str] = []
        for rv_ins in self.instructions:
            assembly_program.append(rv_ins.generate())

        return assembly_program


def rate_value(val: float, sum_of_rates: float) -> float:
    if sum_of_rates == 0:
        return 0
    return (val / sum_of_rates) * 100


def calculate_rate():
    # rate_of_integer["i_r_type"] = 20%
    # rate_of_integer["i_i_type"] = 40%
    # rate_of_integer["u_i_type"] = 12%
    # ...

    integer: float = 0
    vector: float = 0
    for key, val in config.RV32.items():
        if key[0] == "i":
            integer += val
        elif key[0] == "v":
            vector += val

    for key, val in config.RV32.items():
        if key[0] == "i":
            rate_of_integer[key] = rate_value(val, integer)
        elif key[0] == "v":
            rate_of_vector[key] = rate_value(val, vector)


def generate_random_instruction():
    # Return an object
    name: str = ""

    # config.INTEGER_INS == True, config.VECTOR_INS == True
    if config.INTEGER_INS and config.VECTOR_INS:
        name = random.choice(risc_v_instructions)

    # config.INTEGER_INS == True, config.VECTOR_INS == False
    if config.INTEGER_INS and config.VECTOR_INS == False:
        name = random.choice(i_instructions)

    # config.INTEGER_INS == False, config.VECTOR_INS == True
    if config.INTEGER_INS == False and config.VECTOR_INS:
        name = random.choice(v_instructions)

    class_of_ins = class_of_instructions[name]

    return class_of_ins(name)


def check_rate_of_ins(riscv_ins, freq: float) -> bool:
    return freq < config.RV32[riscv_ins.type]


def generate_random_program(length: int):
    instructions: list[str] = []

    while len(instructions) <= length:
        frequency: float = random.random()
        new_ins = generate_random_instruction()
        # new_ins is an object

        if check_rate_of_ins(new_ins, frequency):
            instructions.append(new_ins)

    return Program(instructions)
