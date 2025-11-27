# khong sử dụng x18, x19, x20, x21
# x5, x6, x7, x31 dùng để lưu "base address" các vùng nhớ

ACTIVE_REG: list[str] = ["x0"]


def add_active_reg(start: int, end: int) -> None:
    for i in range(start, end + 1):
        ACTIVE_REG.append(f"x{i}")


add_active_reg(2, 17)
add_active_reg(22, 31)
