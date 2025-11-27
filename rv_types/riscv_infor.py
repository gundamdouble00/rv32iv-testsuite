from rv_types.integer_info import (
    b_type,
    class_of_i_instr,
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
    min_max,
    single_width_integer_add_sub,
    single_width_shift,
    v_instructions,
)

risc_v_instructions = v_instructions + i_instructions  # merge 2 lists
class_of_instructions = class_of_vector | class_of_i_instr  # merge 2 dict

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

type_of_ins = {
    #
    "RTypeIns": "i_r_type",
    "ITypeIns": "i_i_type",
    "STypeIns": "i_s_type",
    "BTypeIns": "i_b_type",
    "UTypeIns": "i_u_type",
    "JTypeIns": "i_j_type",
    #
    "ConfigurationSetting": "v_cfg_configuration_setting",
    #
    "SingleWidthIntegerAddSub": "v_ia_single_width_integer_add_sub",
    "WideningIntegerAddSub": "v_ia_widening_integer_add_sub",
    "IntegerExtension": "v_ia_integer_extension",
    "IntegerAddWCarrySubWBorrow": "v_ia_integer_add_w_carry-sub_w_borrow",
    "BitwiseLogical": "v_ia_bitwise_logical",
    "SingleWidthShift": "v_ia_single_width_shift",
    "NarrowingIntegerRightShift": "v_ia_narrowing_integer_right_shift",
    "IntegerCompare": "v_ia_integer_compare",
    "IntegerMinMax": "v_ia_integer_min_max",
    "SingleWidthIntegerMultiply": "v_ia_single_width_integer_multiply",
    "IntegerDivide": "v_ia_integer_divide",
    "WideningIntegerMultiply": "v_ia_widening_integer_multiply",
    "SingleWidthIntegerMultiplyAdd": "v_ia_single_width_integer_multiply_add",
    "WideningIntegerMultiplyAdd": "v_ia_widening_integer_multiply_add",
    "IntegerMerge": "v_ia_integer_merge",
    "IntegerMove": "v_ia_integer_move",
    #
    "UnitStride": "v_ls_unit_stride",
    "Strided": "v_ls_strided",
    "Indexed": "v_ls_indexed",
    "UnitStrideFaultOnlyFirstLoads": "v_ls_unit_stride_fault_only_first_loads",
    "UnitStrideSegment": "v_ls_unit_stride_segment",
    "StridedSegment": "v_ls_strided_segment",
    "IndexedSegment": "v_ls_indexed_segment",
    "WholeRegister": "v_ls_whole_register",
}
