from rv_instructions.v_extension.integer_arithmetic import SingleWidthIntegerAddSub


def main():
    # for key, val in config.RV32.items():
    #     print(f"key: {key}, val: {val}")
    # return

    # seed_number = input("Input seed number: ")
    # seed_offset = int(seed_number)
    # random.seed(seed_offset)
    # genetic_algorithm()

    obj = SingleWidthIntegerAddSub("vadd.vv", 0)
    print(type(obj).__name__)


if __name__ == "__main__":
    main()
