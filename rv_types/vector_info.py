from rv_instructions.v_extension.base_vector import ConfigurationSetting
from rv_instructions.v_extension.integer_arithmetic import (
    BitwiseLogical,
    IntegerAddWCarrySubWBorrow,
    IntegerCompare,
    IntegerDivide,
    IntegerExtension,
    IntegerMerge,
    IntegerMinMax,
    IntegerMove,
    NarrowingIntegerRightShift,
    SingleWidthIntegerAddSub,
    SingleWidthIntegerMultiply,
    SingleWidthIntegerMultiplyAdd,
    SingleWidthShift,
    WideningIntegerAddSub,
    WideningIntegerMultiply,
    WideningIntegerMultiplyAdd,
)
from rv_instructions.v_extension.loads_stores import (
    UnitStride,
    Strided,
    Indexed,
    UnitStrideFaultOnlyFirstLoads,
    UnitStrideSegment,
    StridedSegment,
    IndexedSegment,
    WholeRegister,
)

v_registers = []
class_of_vector = {}
configuration_setting: list[str] = []
integer_arithmetic: list[str] = []
loads_stores: list[str] = []

for i in range(0, 32):
    v_registers.append(f"v{i}")


def class_and_list(v_ins: list[str], class_of_ins, ins_type: str) -> None:
    for instruction in v_ins:
        class_of_vector[instruction] = class_of_ins

    if ins_type == "ia":
        integer_arithmetic.extend(v_ins)
    elif ins_type == "cfg":
        configuration_setting.extend(v_ins)
    else:
        loads_stores.extend(v_ins)


SEW = ["e8", "e16", "e32"]
LMUL = ["mf8", "mf4", "mf2", "m1", "m2", "m4", "m8"]
TAIL = ["ta", "tu"]
MASK = ["ma", "mu"]

CONFIGURATION_SETTING: str = "cfg"
INTEGER_ARITHMETIC: str = "ia"
LOADS_STORES: str = "ls"


# # # # # # # # # # # #
configuration_setting = ["vsetvl", "vsetvli", "vsetivli"]
class_and_list(configuration_setting, ConfigurationSetting, CONFIGURATION_SETTING)

# # # # # # # # # # # #
single_width_integer_add_sub = [
    "vadd.vv",
    "vadd.vx",
    "vadd.vi",
    "vsub.vv",
    "vsub.vx",
    "vrsub.vx",
    "vrsub.vi",
]
class_and_list(
    single_width_integer_add_sub, SingleWidthIntegerAddSub, INTEGER_ARITHMETIC
)
#
widening_integer_add_sub = [
    "vwaddu.vv",
    "vwaddu.vx",
    "vwsubu.vv",
    "vwsubu.vx",
    #
    "vwadd.vv",
    "vwadd.vx",
    "vwsub.vv",
    "vwsub.vx",
    #
    "vwaddu.wv",
    "vwaddu.wx",
    "vwsubu.wv",
    "vwsubu.wx",
    #
    "vwadd.wv",
    "vwadd.wx",
    "vwsub.wv",
    "vwsub.wx",
]
class_and_list(widening_integer_add_sub, WideningIntegerAddSub, INTEGER_ARITHMETIC)
#
integer_extension = [
    "vzext.vf2",
    "vsext.vf2",
    "vzext.vf4",
    "vsext.vf4",
    # "vzext.vf8",
    # "vsext.vf8",
]
class_and_list(integer_extension, IntegerExtension, INTEGER_ARITHMETIC)
#
integer_add_w_carry_sub_w_borrow = [
    "vadc.vvm",
    "vadc.vxm",
    "vadc.vim",
    #
    "vmadc.vvm",
    "vmadc.vxm",
    "vmadc.vim",
    #
    "vmadc.vx",
    "vmadc.vi",
    #
    "vsbc.vvm",
    "vsbc.vxm",
    #
    "vmsbc.vvm",
    "vmsbc.vxm",
    #
    "vmsbc.vv",
    "vmsbc.vx",
]
class_and_list(
    integer_add_w_carry_sub_w_borrow, IntegerAddWCarrySubWBorrow, INTEGER_ARITHMETIC
)
#
bitwise_logical = [
    "vand.vv",
    "vand.vx",
    "vand.vi",
    #
    "vor.vv",
    "vor.vx",
    "vor.vi",
    #
    "vxor.vv",
    "vxor.vx",
    "vxor.vi",
]
class_and_list(bitwise_logical, BitwiseLogical, INTEGER_ARITHMETIC)
#
single_width_shift = [
    "vsll.vv",
    "vsll.vx",
    "vsll.vi",
    #
    "vsrl.vv",
    "vsrl.vx",
    "vsrl.vi",
    #
    "vsra.vv",
    "vsra.vx",
    "vsra.vi",
]
class_and_list(single_width_shift, SingleWidthShift, INTEGER_ARITHMETIC)
#
narrowing_integer_right_shift = [
    "vnsrl.wv",
    "vnsrl.wx",
    "vnsrl.wi",
    #
    "vnsra.wv",
    "vnsra.wx",
    "vnsra.wi",
]
class_and_list(
    narrowing_integer_right_shift, NarrowingIntegerRightShift, INTEGER_ARITHMETIC
)
#
integer_compare = [
    "vmseq.vv",
    "vmseq.vx",
    "vmseq.vi",
    #
    "vmsne.vv",
    "vmsne.vx",
    "vmsne.vi",
    #
    "vmsltu.vv",
    "vmsltu.vx",
    #
    "vmslt.vv",
    "vmslt.vx",
    #
    "vmsleu.vv",
    "vmsleu.vx",
    "vmsleu.vi",
    #
    "vmsle.vv",
    "vmsle.vx",
    "vmsle.vi",
    #
    "vmsgtu.vx",
    "vmsgtu.vi",
    #
    "vmsgt.vx",
    "vmsgt.vi",
]
class_and_list(integer_compare, IntegerCompare, INTEGER_ARITHMETIC)
#
integer_min_max = [
    "vmin.vv",
    "vmin.vx",
    #
    "vminu.vv",
    "vminu.vx",
    #
    "vmax.vv",
    "vmax.vx",
    #
    "vmaxu.vv",
    "vmaxu.vx",
]
class_and_list(integer_min_max, IntegerMinMax, INTEGER_ARITHMETIC)
#
single_width_integer_multiply = [
    "vmul.vv",
    "vmul.vx",
    #
    "vmulh.vv",
    "vmulh.vx",
    #
    "vmulhu.vv",
    "vmulhu.vx",
    #
    "vmulhsu.vv",
    "vmulhsu.vx",
]
class_and_list(
    single_width_integer_add_sub, SingleWidthIntegerMultiply, INTEGER_ARITHMETIC
)
#
integer_divide = [
    "vdivu.vv",
    "vdivu.vx",
    #
    "vdiv.vv",
    "vdiv.vx",
    #
    "vremu.vv",
    "vremu.vx",
    #
    "vrem.vv",
    "vrem.vx",
]
class_and_list(integer_divide, IntegerDivide, INTEGER_ARITHMETIC)
#
widening_integer_multiply = [
    "vwmul.vv",
    "vwmul.vx",
    #
    "vwmulu.vv",
    "vwmulu.vx",
    #
    "vwmulsu.vv",
    "vwmulsu.vx",
]
class_and_list(widening_integer_multiply, WideningIntegerMultiply, INTEGER_ARITHMETIC)
#
single_width_integer_multiply_add = [
    "vmacc.vv",
    "vmacc.vx",
    #
    "vnmsac.vv",
    "vnmsac.vx",
    #
    "vmadd.vv",
    "vmadd.vx",
    #
    "vnmsub.vv",
    "vnmsub.vx",
]
class_and_list(
    single_width_integer_multiply_add, SingleWidthIntegerMultiplyAdd, INTEGER_ARITHMETIC
)
#
widening_integer_multiply_add = [
    "vwmaccu.vv",
    "vwmaccu.vx",
    #
    "vwmacc.vv",
    "vwmacc.vx",
    #
    "vwmaccsu.vv",
    "vwmaccsu.vx",
    #
    "vwmaccus.vx",
]
class_and_list(
    widening_integer_multiply, WideningIntegerMultiplyAdd, INTEGER_ARITHMETIC
)
#
integer_merge = [
    "vmerge.vvm",
    "vmerge.vxm",
    "vmerge.vim",
]
class_and_list(integer_merge, IntegerMerge, INTEGER_ARITHMETIC)
#
integer_move = [
    "vmv.v.v",
    "vmv.v.x",
    "vmv.v.i",
]
class_and_list(integer_move, IntegerMove, INTEGER_ARITHMETIC)


# # # # # # # # # # # #
unit_stride = [
    "vle8.v",
    "vle16.v",
    "vle32.v",
    #
    "vse8.v",
    "vse16.v",
    "vse32.v",
    #
    "vlm.v",
    "vsm.v",
]
class_and_list(unit_stride, UnitStride, LOADS_STORES)
#
strided = [
    "vlse8.v",
    "vlse16.v",
    "vlse32.v",
    #
    "vsse8.v",
    "vsse16.v",
    "vsse32.v",
]
class_and_list(strided, Strided, LOADS_STORES)
#
indexed = [
    "vluxei8.v",
    "vluxei16.v",
    "vluxei32.v",
    #
    "vloxei8.v",
    "vloxei16.v",
    "vloxei32.v",
    #
    "vsuxei8.v",
    "vsuxei16.v",
    "vsuxei32.v",
    #
    "vsoxei8.v",
    "vsoxei16.v",
    "vsoxei32.v",
]
class_and_list(indexed, Indexed, LOADS_STORES)
#
unit_stride_fault_only_first_loads = [
    "vle8ff.v",
    "vle16ff.v",
    "vle32ff.v",
]
class_and_list(
    unit_stride_fault_only_first_loads, UnitStrideFaultOnlyFirstLoads, LOADS_STORES
)
#
unit_stride_segment = [
    "vlseg",
    "vsseg",
]
class_and_list(unit_stride_segment, UnitStrideSegment, LOADS_STORES)
#
strided_segment = [
    "vlsseg",
    "vssseg",
]
class_and_list(strided_segment, StridedSegment, LOADS_STORES)
#
indexed_segment = [
    "vluxseg",
    "vloxseg",
    "vsuxseg",
    "vsoxseg",
]
class_and_list(indexed_segment, IndexedSegment, LOADS_STORES)
#
whole_register = ["vl_re_.v", "vs_r.v"]
class_and_list(whole_register, WholeRegister, LOADS_STORES)

# # # # # # # # # # # #
v_instructions: list[str] = []
v_instructions.extend(configuration_setting)
v_instructions.extend(integer_arithmetic)
v_instructions.extend(loads_stores)
