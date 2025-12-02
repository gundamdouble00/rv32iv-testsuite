import random


def random_register(register: str) -> str:
    num: int = random.randint(0, 31)
    if register == "v":
        return f"v{num}"
    elif register == "x":
        return f"v{num}"

    return ""


def random_src1(type_of_src1: str, left: int, right: int) -> str:
    num: int = random.randint(0, 31)

    if type_of_src1 == "v":
        src1 = f"v{num}"
    elif type_of_src1 == "x":
        src1 = f"x{num}"
    else:
        src1 = f"{random.randint(left, right)}"

    return src1
