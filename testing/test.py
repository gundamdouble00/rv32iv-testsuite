import random

import config
from program.generator import generate_random_program


def check_asm_program():
    seed_number = input("Input seed number: ")
    seed_offset = int(seed_number)
    random.seed(seed_offset)

    random_program = generate_random_program(32)
    asm_program = random_program.instructions

    # for key in config.RV32.keys():
    #     print(f"{key}: {random_program.count_riscv_ins[key]}")

    has_label = set()
    for index in range(len(asm_program)):
        rv_ins = asm_program[index]
        if rv_ins.type in ("i_b_type", "i_j_type"):
            has_label.add(int(rv_ins.src3) + index * 4)

    # print(random.choice(random.randrange(-120, 0, 4), random.randrange(4, 121, 4)))

    label = {}
    for i in range(len(asm_program)):
        if (i * 4) in has_label:
            label[i * 4] = f"label_{i}"
            # print(i * 4)

    for i in range(len(asm_program)):
        rv_ins = asm_program[i]
        if (i * 4) in has_label:
            print(f"{label[i * 4]}:")

        imm: str = ""
        if rv_ins.type in ("i_b_type", "i_j_type"):
            imm = rv_ins.src3
            rv_ins.src3 = label[int(rv_ins.src3) + i * 4]

        print(f"\t{rv_ins.generate()} (addr: {4 * i}, imm: {imm})")
