from types.integer_info import class_of_i_instr, i_instructions
from types.vector_info import class_of_v_instr, v_instructions

risc_v_instructions = v_instructions + i_instructions  # merge 2 lists
class_of_instructions = class_of_v_instr | class_of_i_instr  # merge 2 dict
