# x1, x2, x3, x4, x8, x18, x19, x20, x21, x22
ACTIVE_REG: list[str] = ["x0"]

integer_index_ua: set[int] = {1, 2, 3, 4, 8, 18, 19, 20, 21, 22}
integer_index_a: set[int] = {0}
vector_index: set[int] = {24, 25, 26, 27, 28, 29, 30, 31}


def add_active_reg(start: int, end: int) -> None:
    for i in range(start, end + 1):
        ACTIVE_REG.append(f"x{i}")
        integer_index_a.add(i)


add_active_reg(5, 7)
add_active_reg(9, 17)
add_active_reg(23, 31)


BYTE_DATA: str = "byte_data"
HALF_DATA: str = "half_data"
WORD_DATA: str = "word_data"
SAVED_MEM: str = "saved_mem"

MEM_REG = {
    BYTE_DATA: "x18",
    HALF_DATA: "x19",
    WORD_DATA: "x20",
    SAVED_MEM: "x21",
}
