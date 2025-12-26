MASK_BONUS_POINT = 5

PENALTY_PER_MISSING = 200

HAZARD_SCORE = 32

SAME_OPERAND_SCORE = 26

NEGATIVE_IMM_BONUS = 18

INSTRUCTION_SCORES = {
    # --- Scalar ---
    "i_r_type": 12,
    "i_i_type": 14,
    "i_s_type": 16,
    "i_b_type": 16,
    "i_u_type": 18,
    "i_j_type": 18,
    # --- Config ---
    "v_cfg_configuration_setting": 26,
    # --- Basic Arithmetic ---
    "v_ia_single_width_integer_add_sub": 20,
    "v_ia_bitwise_logical": 22,
    "v_ia_single_width_shift": 22,
    "v_ia_integer_min_max": 20,
    "v_ia_integer_move": 20,
    # --- Complex Arithmetic) ---
    "v_ia_single_width_integer_multiply": 26,
    "v_ia_single_width_integer_multiply_add": 26,
    "v_ia_integer_divide": 28,
    "v_ia_integer_merge": 24,
    "v_ia_integer_compare": 24,
    "v_ia_integer_add_w_carry-sub_w_borrow": 26,
    # --- Widening/Narrowing ---
    "v_ia_widening_integer_add_sub": 30,
    "v_ia_integer_extension": 30,
    "v_ia_narrowing_integer_right_shift": 32,
    "v_ia_widening_integer_multiply": 36,
    "v_ia_widening_integer_multiply_add": 38,
    # --- Memory (Load/Store) ---
    "v_ls_unit_stride": 42,
    "v_ls_strided": 48,
    "v_ls_indexed": 50,
}
