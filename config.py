POPULATION_SIZE: int = 60
NUM_GENERATIONS: int = 60
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

INTEGER_INS: bool = True
VECTOR_INS: bool = False

# RV32: The minimum number of instructions of each type must be included in the generated program
RV32 = {
    # # # # # # # # # # # # # # # # # # # # # # # # # #
    "i_r_type": 12,  # R-type instructions
    "i_i_type": 12,  # I-type instructions
    "i_s_type": 26,  # S-type instructions
    "i_b_type": 12,  # B-type instructions
    "i_u_type": 21,  # U-type instructions
    "i_j_type": 19,  # J-type instructions
    # # # # # # # # # # # # # # # # # # # # # # # # # #
    # v_cfg: Configuration-Setting Instructionns
    "v_cfg_configuration_setting": 9,
    # # # # # # # # # # # # # # # # # # # # # # # # # #
    # v_ia: Vector Integer Arithmetic Instructions
    "v_ia_single_width_integer_add_sub": 0,
    "v_ia_widening_integer_add_sub": 0,
    "v_ia_integer_extension": 0,
    "v_ia_integer_add_w_carry-sub_w_borrow": 0,
    "v_ia_bitwise_logical": 0,
    "v_ia_single_width_shift": 0,
    "v_ia_narrowing_integer_right_shift": 0,
    "v_ia_integer_compare": 0,
    "v_ia_integer_min_max": 0,
    "v_ia_single_width_integer_multiply": 0,
    "v_ia_integer_divide": 0,
    "v_ia_widening_integer_multiply": 0,
    "v_ia_single_width_integer_multiply_add": 0,
    "v_ia_widening_integer_multiply_add": 0,
    "v_ia_integer_merge": 0,
    "v_ia_integer_move": 0,
    # # # # # # # # # # # # # # # # # # # # # # # # # #
    # v_ls: Vector Loads and Stores
    "v_ls_unit_stride": 12,
    "v_ls_strided": 12,
    "v_ls_indexed": 12,
    "v_ls_unit_stride_fault_only_first_loads": 12,
    "v_ls_unit_stride_segment": 12,
    "v_ls_strided_segment": 12,
    "v_ls_indexed_segment": 12,
    "v_ls_whole_register": 12,
}

PROGRAM_LEN: int = 0
for key, value in RV32.items():
    # ex: key == i_r_type
    # ex: key == v_ia_single_width_integer_add_sub
    if key[0] == "i" and (not INTEGER_INS):
        continue
    if key[0] == "v" and (not VECTOR_INS):
        continue

    PROGRAM_LEN += value

ADDITION_LEN: int = 50
PROGRAM_LEN += ADDITION_LEN
