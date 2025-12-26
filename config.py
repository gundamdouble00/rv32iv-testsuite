POPULATION_SIZE: int = 60
NUM_GENERATIONS: int = 12
MUTATION_RATE: float = 0.1
CROSSOVER_RATE: float = 0.7

MEM_REGION = {
    # bits: Data width (in bits)
    # numbers: Number of memory entries of each width
    "byte": {
        "bits": 8,
        "numbers": 32,
    },
    "half": {
        "bits": 16,
        "numbers": 96,
    },
    "word": {
        "bits": 32,
        "numbers": 64,
    },
}

SAVED_STORE: int = 0
for key in MEM_REGION.keys():
    SAVED_STORE = max(SAVED_STORE, MEM_REGION[key]["numbers"])

RISCV_INS = {
    "i": True,  # Integer
    "v": True,  # Vector
    # "m": False,  # MulDiv
}

# RV32: The minimum number of instructions of each type must be included in the generated program
RV32 = {
    "i_r_type": 12,  # R-type instructions
    "i_i_type": 12,  # I-type instructions
    "i_s_type": 26,  # S-type instructions
    "i_b_type": 0,  # B-type instructions
    "i_u_type": 21,  # U-type instructions
    "i_j_type": 2,  # J-type instructions
    # v_cfg: Configuration-Setting Instructionns
    "v_cfg_configuration_setting": 9,
    # v_ia: Vector Integer Arithmetic Instructions
    "v_ia_single_width_integer_add_sub": 12,
    "v_ia_widening_integer_add_sub": 12,
    "v_ia_integer_extension": 12,
    "v_ia_integer_add_w_carry-sub_w_borrow": 12,
    "v_ia_bitwise_logical": 12,
    "v_ia_single_width_shift": 12,
    "v_ia_narrowing_integer_right_shift": 12,
    "v_ia_integer_compare": 12,
    "v_ia_integer_min_max": 12,
    "v_ia_single_width_integer_multiply": 12,
    "v_ia_integer_divide": 12,
    "v_ia_widening_integer_multiply": 12,
    "v_ia_single_width_integer_multiply_add": 12,
    "v_ia_widening_integer_multiply_add": 12,
    "v_ia_integer_merge": 12,
    "v_ia_integer_move": 12,
    # v_ls: Vector Loads and Stores
    "v_ls_unit_stride": 12,
    "v_ls_strided": 12,
    "v_ls_indexed": 12,
}

PROGRAM_LEN: int = 0
for key, value in RV32.items():
    # ex: key == i_r_type
    # ex: key == v_ia_single_width_integer_add_sub
    if not RISCV_INS[key[0]]:
        continue

    PROGRAM_LEN += value

ADDITION_LEN: int = 120
PROGRAM_LEN += ADDITION_LEN

# # # #
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
