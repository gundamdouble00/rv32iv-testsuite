import random

import config

rate_of_ins = {}


class Program:
    def __init__(self):
        self.data_processing = []
        self.control_flow = []
        self.union = []

        self.fitness = float(-1)
        self.count_ins = {}

        for key in config.RV32.keys():
            self.count_ins[key] = 0

    def __len__(self):
        return len(self.instructions)

    def update_count_riscv(self):
        for ins in self.instructions:
            self.count_riscv_ins[ins.type] += 1

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
    # rate_of_ins["i_r_type"] = 20%
    # rate_of_ins["i_i_type"] = 40%
    # rate_of_ins["u_i_type"] = 12%
    # ...
    # rate_of_ins["v_single_width_int_add_sub"] = 12%

    sum_of_rates: float = 0
    for key, val in config.RV32.items():
        if key[0] == "i":
            sum_of_rates += val
            continue
        if config.VECTOR_INS:
            sum_of_rates += val

    for key, val in config.RV32.items():
        if key[0] == "i":
            rate_of_ins[key] = rate_value(val, sum_of_rates)
            continue
        if config.VECTOR_INS:
            rate_of_ins[key] = rate_value(val, sum_of_rates)
        else:
            rate_of_ins[key] = 0


def generate_random_instruction(key: str, index: int):
    # Return an object
    name = random.choice(ins_of_type[key])
    class_of_ins = class_of_instructions[name]

    return class_of_ins(name, index)


def generate_random_program(length: int):
    calculate_rate()
    asm_program = Program()

    for key in config.RV32.keys():
        # print(ins_of_type[key])
        if len(asm_program.instructions) == length:
            break

        while True:
            new_ins = generate_random_instruction(
                key, len(asm_program.instructions) + 1
            )
            num_of_ins = asm_program.count_riscv_ins[key] + 1

            if ((num_of_ins / length) * 100) <= rate_of_ins[key]:
                asm_program.instructions.append(new_ins)
                asm_program.count_riscv_ins[key] = num_of_ins

                i: int = len(asm_program.instructions) - 1
                j: int = random.randint(0, max(i - 1, 0))

                asm_program.instructions[i], asm_program.instructions[j] = (
                    asm_program.instructions[j],
                    asm_program.instructions[i],
                )
            else:
                break

    while len(asm_program.instructions) != length:
        name = random.choice(i_instructions)
        class_of_ins = class_of_instructions[name]
        new_ins = class_of_ins(name, len(asm_program.instructions) + 1)
        asm_program.instructions.append(new_ins)
        asm_program.count_riscv_ins[new_ins.type] += 1

    for i in range(len(asm_program.instructions)):
        rv_ins = asm_program.instructions[i]
        if rv_ins.type == "i_b_type":
            asm_program.instructions[i].src3 = random.randrange(
                -4 * i, 4 * (length - i - 1) + 1, 4
            )

    return asm_program
