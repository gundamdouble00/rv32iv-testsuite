from rv_types.integer_info import (
    b_type,
    class_of_integer,
    i_instructions,
    i_type,
    j_type,
    r_type,
    s_type,
    u_type,
)
from rv_types.vector_info import (
    bitwise_logical,
    class_of_vector,
    integer_compare,
    integer_merge,
    integer_move,
    integer_min_max,
    single_width_integer_add_sub,
    single_width_shift,
    v_instructions,
    widening_integer_add_sub,
    integer_extension,
    integer_add_w_carry_sub_w_borrow,
    narrowing_integer_right_shift,
    single_width_integer_multiply,
    integer_divide,
    widening_integer_multiply,
    single_width_integer_multiply_add,
    widening_integer_multiply_add,
    unit_stride,
    indexed,
    strided,
    configuration_setting,
)

risc_v_instructions = v_instructions + i_instructions  # merge 2 lists
class_of_instructions = class_of_vector | class_of_integer  # merge 2 dict

ins_of_type = {
    "i_r_type": r_type,
    "i_i_type": i_type,
    "i_s_type": s_type,
    "i_b_type": b_type,
    "i_u_type": u_type,
    "i_j_type": j_type,
    #
    "v_cfg_configuration_setting": configuration_setting,
    #
    "v_ia_single_width_integer_add_sub": single_width_integer_add_sub,
    "v_ia_widening_integer_add_sub": widening_integer_add_sub,
    "v_ia_integer_extension": integer_extension,
    "v_ia_integer_add_w_carry-sub_w_borrow": integer_add_w_carry_sub_w_borrow,
    "v_ia_bitwise_logical": bitwise_logical,
    "v_ia_single_width_shift": single_width_shift,
    "v_ia_narrowing_integer_right_shift": narrowing_integer_right_shift,
    "v_ia_integer_compare": integer_compare,
    "v_ia_integer_min_max": integer_min_max,
    "v_ia_single_width_integer_multiply": single_width_integer_multiply,
    "v_ia_integer_divide": integer_divide,
    "v_ia_widening_integer_multiply": widening_integer_multiply,
    "v_ia_single_width_integer_multiply_add": single_width_integer_multiply_add,
    "v_ia_widening_integer_multiply_add": widening_integer_multiply_add,
    "v_ia_integer_merge": integer_merge,
    "v_ia_integer_move": integer_move,
    #
    "v_ls_unit_stride": unit_stride,
    "v_ls_strided": strided,
    "v_ls_indexed": indexed,
}
