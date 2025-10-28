import random

from testing import test
from ga.main_ga import genetic_algorithm
from program.generator import Program, generate_random_program


def save_to_file(filename: str, final_program: Program):
    with open(filename, "w") as f:
        f.write("initialization:\n")
        for i in range(0, 32):
            f.write(f"    addi x{i}, x0, {random.randint(-2048, 2047)}\n")

        f.write("main:\n")
        for ins in final_program.to_assembly():
            f.write(f"    {ins}\n")


def main():
    # for key, val in config.RV32.items():
    #     print(f"key: {key}, val: {val}")
    # return

    # seed_number = input("Input seed number: ")
    # seed_offset = int(seed_number)
    # random.seed(seed_offset)
    # genetic_algorithm()
    test.check_asm_program()


if __name__ == "__main__":
    main()
