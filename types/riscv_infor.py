import random

from types.integer_info import (
    class_of_i_instr,
    i_instructions,
    r_type,
    i_type,
    s_type,
    b_type,
    u_type,
    j_type,
)
from types.vector_info import (
    class_of_v_instr,
    v_instructions,
    single_width_integer_add_sub,
    bitwise_logical,
    single_width_shift,
    integer_compare,
    min_max,
    integer_merge,
    integer_move,
)

risc_v_instructions = v_instructions + i_instructions  # merge 2 lists
class_of_instructions = class_of_v_instr | class_of_i_instr  # merge 2 dict

ins_of_type = {
    "i_r_type": r_type,
    "i_i_type": i_type,
    "i_s_type": s_type,
    "i_b_type": b_type,
    "i_u_type": u_type,
    "i_j_type": j_type,
    "v_single_width_integer_add_sub": single_width_integer_add_sub,
    "v_bitwise_logical": bitwise_logical,
    "v_single_width_shift": single_width_shift,
    "v_integer_compare": integer_compare,
    "v_min_max": min_max,
    "v_integer_merge": integer_merge,
    "v_integer_move": integer_move,
}
