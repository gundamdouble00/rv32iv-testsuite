import random
from program.generator import (
    Program,
)


def save_to_file(filename: str, final_program: Program):
    with open(filename, "w") as f:
        f.write("initialization:\n")
        for i in range(0, 32):
            f.write(f"    addi x{i}, x0, {random.randint(-2048, 2047)}\n")

        f.write("main:\n")
        for ins in final_program.to_assembly():
            f.write(f"    {ins}\n")


def save_to_file_test(filename: str, programs: list[Program]):
    with open(filename, "w") as f:
        for individual in programs:
            for ins in individual.to_assembly():
                f.write(f"{ins}\n")
            f.write("\n")
