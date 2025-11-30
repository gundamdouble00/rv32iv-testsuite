ACTIVE_REG: list[str] = ["x0"]


def add_active_reg(start: int, end: int) -> None:
    for i in range(start, end + 1):
        ACTIVE_REG.append(f"x{i}")


add_active_reg(2, 17)
add_active_reg(22, 31)

BYTE_DATA: str = "byte_date"
HALF_DATA: str = "half_date"
WORD_DATA: str = "word_data"
SAVED_MEM: str = "saved_mem"

MEM_REG = {
    BYTE_DATA: "x18",
    HALF_DATA: "x19",
    WORD_DATA: "x20",
    SAVED_MEM: "x21",
}
