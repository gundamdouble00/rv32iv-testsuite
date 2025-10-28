import random

POPULATION_SIZE: int = 120
NUM_GENERATIONS: int = 140
MUTATION_RATE: float = 0.1
CROSSOVER_RATE: float = 0.7

MIN_PROGRAM_LENGTH = 50
MAX_PROGRAM_LENGTH = 50
PROGRAM_LEN = random.randint(MIN_PROGRAM_LENGTH, MAX_PROGRAM_LENGTH)

MIN_MEM_REGION: int = 0
MAX_MEM_REGION: int = 8000000  # 8000000 bytes

VECTOR_INS: bool = False

RV32 = {
    "i_r_type": 0.0,
    "i_i_type": 0.0,
    "i_s_type": 0.0,
    "i_b_type": 0.32,
    "i_u_type": 0.0,
    "i_j_type": 0.0,
    "v_single_width_integer_add_sub": 0,
    "v_bitwise_logical": 0,
    "v_single_width_shift": 0,
    "v_integer_compare": 0,
    "v_min_max": 0,
    "v_integer_merge": 0,
    "v_integer_move": 0,
}
