from rv_instructions.v_extension.base_vector import ConfigurationSetting
from rv_instructions.v_extension.integer_arithmetic import (
    SingleWidthIntegerAddSub,
    BitwiseLogical,
    SingleWidthShift,
    IntegerCompare,
    MinMax,
    IntegerMerge,
    IntegerMove,
    WideningIntegerAddSubtract,
    VectorIntegerExtension,
    NarrowingIntegerRightShift,
    SingleWidthIntegerMultiply,
    IntegerDivide,
    WideningIntegerMultiply,
    SingleWidthIntegerMultiplyAdd,
    WideningIntegerMultiplyAdd,
)
from rv_instructions.v_extension.loads_stores import (
    UnitStride,
    Strided,
    Indexed,
    UnitStrideFaultOnlyFirstLoads,
    LoadStoreSegment,
    LoadStoreWholeRegister,
)

v_registers = []
for i in range(0, 32):
    v_registers.append(f"v{i}")

SEW = ["e8", "e16", "e32", "e64"]
LMUL = ["mf8", "mf4", "mf2", "m1", "m2", "m4", "m8"]
TAIL = ["ta", "tu"]
MASK = ["ma", "mu"]

# # # # # # # # # # # #
configuration_setting = ["vsetvl", "vsetvli", "vsetivli"]

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
bitwise_logical = [
    "vand.vv",
    "vand.vx",
    "vand.vi",
    "vor.vv",
    "vor.vx",
    "vor.vi",
    "vxor.vv",
    "vxor.vx",
    "vxor.vi",
]
single_width_shift = [
    "vsll.vv",
    "vsll.vx",
    "vsll.vi",
    "vsrl.vv",
    "vsrl.vx",
    "vsrl.vi",
    "vsra.vv",
    "vsra.vx",
    "vsra.vi",
]
integer_compare = [
    "vmseq.vv",
    "vmseq.vx",
    "vmseq.vi",
    "vmsne.vv",
    "vmsne.vx",
    "vmsne.vi",
    "vmsltu.vv",
    "vmsltu.vx",
    "vmslt.vv",
    "vmslt.vx",
    "vmsleu.vv",
    "vmsleu.vx",
    "vmsleu.vi",
    "vmsle.vv",
    "vmsle.vx",
    "vmsle.vi",
    "vmsgtu.vx",
    "vmsgtu.vi",
    "vmsgt.vx",
    "vmsgt.vi",
]
min_max = [
    "vmin.vv",
    "vmin.vx",
    "vminu.vv",
    "vminu.vx",
    "vmax.vv",
    "vmax.vx",
    "vmaxu.vv",
    "vmaxu.vx",
]
integer_merge = [
    "vmerge.vvm",
    "vmerge.vxm",
    "vmerge.vim",
]
integer_move = [
    "vmv.v.v",
    "vmv.v.x",
    "vmv.v.i",
]
widening_integer_add_subtract = [
    "vwaddu.vv",
    "vwaddu.vx",
    "vwsubu.vv",
    "vwsubu.vx",
    "vwadd.vv",
    "vwadd.vx",
    "vwsub.vv",
    "vwsub.vx",
    "vwaddu.wv",
    "vwaddu.wx",
    "vwsubu.wv",
    "vwsubu.wx",
    "vwadd.wv",
    "vwadd.wx",
    "vwsub.wv",
    "vwsub.wx",
]
vector_integer_extension = [
    "vzext.vf2",
    "vsext.vf2",
    "vzext.vf4",
    "vsext.vf4",
    "vzext.vf8",
    "vsext.vf8",
]
narrowing_integer_right_shift = [
    "vnsrl.wv",
    "vnsrl.wx",
    "vnsrl.wi",
    "vnsra.wv",
    "vnsra.wx",
    "vnsra.wi",
]
single_width_integer_multiply = [
    "vmul.vv",
    "vmul.vx",
    "vmulh.vv",
    "vmulh.vx",
    "vmulhu.vv",
    "vmulhu.vx",
    "vmulhsu.vv",
    "vmulhsu.vx",
]
integer_divide = [
    "vdivu.vv",
    "vdivu.vx",
    "vdiv.vv",
    "vdiv.vx",
    "vremu.vv",
    "vremu.vx",
    "vrem.vv",
    "vrem.vx",
]
widening_integer_multiply = [
    "vwmul.vv",
    "vwmul.vx",
    "vwmulu.vv",
    "vwmulu.vx",
    "vwmulsu.vv",
    "vwmulsu.vx",
]
single_width_integer_multiply_add = [
    "vmacc.vv",
    "vmacc.vx",
    "vnmsac.vv",
    "vnmsac.vx",
    "vmadd.vv",
    "vmadd.vx",
    "vnmsub.vv",
    "vnmsub.vx",
]
widening_integer_multiply_add = [
    "vwmaccu.vv",
    "vwmaccu.vx",
    "vwmacc.vv",
    "vwmacc.vx",
    "vwmaccsu.vv",
    "vwmaccsu.vx",
    "vwmaccus.vx",
]

integer_arithmetic_instr = (
    single_width_integer_add_sub
    + bitwise_logical
    + single_width_shift
    + integer_compare
    + min_max
    + integer_merge
    + integer_move
    + widening_integer_add_subtract
    + vector_integer_extension
    + narrowing_integer_right_shift
    + single_width_integer_multiply
    + integer_divide
    + widening_integer_multiply
    + single_width_integer_multiply_add
    + widening_integer_multiply_add
)

# # # # # # # # # # # #
unit_stride = [
    "vle8.v",
    "vle16.v",
    "vle32.v",
    "vle64.v",
    "vse8.v",
    "vse16.v",
    "vse32.v",
    "vse64.v",
    "vlm.v",
    "vsm.v",
]
strided = [
    "vlse8.v",
    "vlse16.v",
    "vlse32.v",
    "vlse64.v",
    "vsse8.v",
    "vsse16.v",
    "vsse32.v",
    "vsse64.v",
]
indexed = [
    "vluxei8.v",
    "vluxei16.v",
    "vluxei32.v",
    "vloxei8.v",
    "vloxei16.v",
    "vloxei32.v",
    "vsuxei8.v",
    "vsuxei16.v",
    "vsuxei32.v",
    "vsoxei8.v",
    "vsoxei16.v",
    "vsoxei32.v",
]
unit_stride_fault_only_first_loads = [
    "vle8ff.v",
    "vle16ff.v",
    "vle32ff.v",
    "vle64ff.v",
]
load_store_segment = [
    "vlseg",
    "vsseg",
    "vlsseg",
    "vssseg",
    "vluxseg",
    "vloxseg",
    "vsuxseg",
    "vsoxseg",
]
load_store_whole_register = ["vl_re_.v", "vs_r.v"]

loads_stores_instr = (
    unit_stride
    + strided
    + indexed
    + unit_stride_fault_only_first_loads
    + load_store_segment
    # + load_store_whole_register
)

# # # # # # # # # # # #
v_instructions = configuration_setting + integer_arithmetic_instr + loads_stores_instr

class_of_v_instr = {
    "vsetvl": ConfigurationSetting,
    "vsetvli": ConfigurationSetting,
    "vsetivli": ConfigurationSetting,
    #
    "vle8.v": UnitStride,
    "vle16.v": UnitStride,
    "vle32.v": UnitStride,
    "vle64.v": UnitStride,
    "vse8.v": UnitStride,
    "vse16.v": UnitStride,
    "vse32.v": UnitStride,
    "vse64.v": UnitStride,
    "vlm.v": UnitStride,
    "vsm.v": UnitStride,
    #
    "vlse8.v": Strided,
    "vlse16.v": Strided,
    "vlse32.v": Strided,
    "vlse64.v": Strided,
    "vsse8.v": Strided,
    "vsse16.v": Strided,
    "vsse32.v": Strided,
    "vsse64.v": Strided,
    #
    "vluxei8.v": Indexed,
    "vluxei16.v": Indexed,
    "vluxei32.v": Indexed,
    "vloxei8.v": Indexed,
    "vloxei16.v": Indexed,
    "vloxei32.v": Indexed,
    "vsuxei8.v": Indexed,
    "vsuxei16.v": Indexed,
    "vsuxei32.v": Indexed,
    "vsoxei8.v": Indexed,
    "vsoxei16.v": Indexed,
    "vsoxei32.v": Indexed,
    #
    "vle8ff.v": UnitStrideFaultOnlyFirstLoads,
    "vle16ff.v": UnitStrideFaultOnlyFirstLoads,
    "vle32ff.v": UnitStrideFaultOnlyFirstLoads,
    "vle64ff.v": UnitStrideFaultOnlyFirstLoads,
    #
    "vlseg": LoadStoreSegment,
    "vsseg": LoadStoreSegment,
    "vlsseg": LoadStoreSegment,
    "vssseg": LoadStoreSegment,
    "vluxseg": LoadStoreSegment,
    "vloxseg": LoadStoreSegment,
    "vsuxseg": LoadStoreSegment,
    "vsoxseg": LoadStoreSegment,
    #
    "vl_re_.v": LoadStoreWholeRegister,
    "vs_r.v": LoadStoreWholeRegister,
    #
    "vadd.vv": SingleWidthIntegerAddSub,
    "vadd.vx": SingleWidthIntegerAddSub,
    "vadd.vi": SingleWidthIntegerAddSub,
    "vsub.vv": SingleWidthIntegerAddSub,
    "vsub.vx": SingleWidthIntegerAddSub,
    "vrsub.vx": SingleWidthIntegerAddSub,
    "vrsub.vi": SingleWidthIntegerAddSub,
    #
    "vand.vv": BitwiseLogical,
    "vand.vx": BitwiseLogical,
    "vand.vi": BitwiseLogical,
    "vor.vv": BitwiseLogical,
    "vor.vx": BitwiseLogical,
    "vor.vi": BitwiseLogical,
    "vxor.vv": BitwiseLogical,
    "vxor.vx": BitwiseLogical,
    "vxor.vi": BitwiseLogical,
    #
    "vsll.vv": SingleWidthShift,
    "vsll.vx": SingleWidthShift,
    "vsll.vi": SingleWidthShift,
    "vsrl.vv": SingleWidthShift,
    "vsrl.vx": SingleWidthShift,
    "vsrl.vi": SingleWidthShift,
    "vsra.vv": SingleWidthShift,
    "vsra.vx": SingleWidthShift,
    "vsra.vi": SingleWidthShift,
    #
    "vmseq.vv": IntegerCompare,
    "vmseq.vx": IntegerCompare,
    "vmseq.vi": IntegerCompare,
    "vmsne.vv": IntegerCompare,
    "vmsne.vx": IntegerCompare,
    "vmsne.vi": IntegerCompare,
    "vmsltu.vv": IntegerCompare,
    "vmsltu.vx": IntegerCompare,
    "vmslt.vv": IntegerCompare,
    "vmslt.vx": IntegerCompare,
    "vmsleu.vv": IntegerCompare,
    "vmsleu.vx": IntegerCompare,
    "vmsleu.vi": IntegerCompare,
    "vmsle.vv": IntegerCompare,
    "vmsle.vx": IntegerCompare,
    "vmsle.vi": IntegerCompare,
    "vmsgtu.vx": IntegerCompare,
    "vmsgtu.vi": IntegerCompare,
    "vmsgt.vx": IntegerCompare,
    "vmsgt.vi": IntegerCompare,
    #
    "vmin.vv": MinMax,
    "vmin.vx": MinMax,
    "vminu.vv": MinMax,
    "vminu.vx": MinMax,
    "vmax.vv": MinMax,
    "vmax.vx": MinMax,
    "vmaxu.vv": MinMax,
    "vmaxu.vx": MinMax,
    #
    "vmerge.vvm": IntegerMerge,
    "vmerge.vxm": IntegerMerge,
    "vmerge.vim": IntegerMerge,
    #
    "vmv.v.v": IntegerMove,
    "vmv.v.x": IntegerMove,
    "vmv.v.i": IntegerMove,
    #
    "vwaddu.vv": WideningIntegerAddSubtract,
    "vwaddu.vx": WideningIntegerAddSubtract,
    "vwsubu.vv": WideningIntegerAddSubtract,
    "vwsubu.vx": WideningIntegerAddSubtract,
    "vwadd.vv": WideningIntegerAddSubtract,
    "vwadd.vx": WideningIntegerAddSubtract,
    "vwsub.vv": WideningIntegerAddSubtract,
    "vwsub.vx": WideningIntegerAddSubtract,
    "vwaddu.wv": WideningIntegerAddSubtract,
    "vwaddu.wx": WideningIntegerAddSubtract,
    "vwsubu.wv": WideningIntegerAddSubtract,
    "vwsubu.wx": WideningIntegerAddSubtract,
    "vwadd.wv": WideningIntegerAddSubtract,
    "vwadd.wx": WideningIntegerAddSubtract,
    "vwsub.wv": WideningIntegerAddSubtract,
    "vwsub.wx": WideningIntegerAddSubtract,
    #
    "vzext.vf2": VectorIntegerExtension,
    "vsext.vf2": VectorIntegerExtension,
    "vzext.vf4": VectorIntegerExtension,
    "vsext.vf4": VectorIntegerExtension,
    "vzext.vf8": VectorIntegerExtension,
    "vsext.vf8": VectorIntegerExtension,
    #
    "vnsrl.wv": NarrowingIntegerRightShift,
    "vnsrl.wx": NarrowingIntegerRightShift,
    "vnsrl.wi": NarrowingIntegerRightShift,
    "vnsra.wv": NarrowingIntegerRightShift,
    "vnsra.wx": NarrowingIntegerRightShift,
    "vnsra.wi": NarrowingIntegerRightShift,
    #
    "vmul.vv": SingleWidthIntegerMultiply,
    "vmul.vx": SingleWidthIntegerMultiply,
    "vmulh.vv": SingleWidthIntegerMultiply,
    "vmulh.vx": SingleWidthIntegerMultiply,
    "vmulhu.vv": SingleWidthIntegerMultiply,
    "vmulhu.vx": SingleWidthIntegerMultiply,
    "vmulhsu.vv": SingleWidthIntegerMultiply,
    "vmulhsu.vx": SingleWidthIntegerMultiply,
    #
    "vdivu.vv": IntegerDivide,
    "vdivu.vx": IntegerDivide,
    "vdiv.vv": IntegerDivide,
    "vdiv.vx": IntegerDivide,
    "vremu.vv": IntegerDivide,
    "vremu.vx": IntegerDivide,
    "vrem.vv": IntegerDivide,
    "vrem.vx": IntegerDivide,
    #
    "vwmul.vv": WideningIntegerMultiply,
    "vwmul.vx": WideningIntegerMultiply,
    "vwmulu.vv": WideningIntegerMultiply,
    "vwmulu.vx": WideningIntegerMultiply,
    "vwmulsu.vv": WideningIntegerMultiply,
    "vwmulsu.vx": WideningIntegerMultiply,
    #
    "vmacc.vv": SingleWidthIntegerMultiplyAdd,
    "vmacc.vx": SingleWidthIntegerMultiplyAdd,
    "vnmsac.vv": SingleWidthIntegerMultiplyAdd,
    "vnmsac.vx": SingleWidthIntegerMultiplyAdd,
    "vmadd.vv": SingleWidthIntegerMultiplyAdd,
    "vmadd.vx": SingleWidthIntegerMultiplyAdd,
    "vnmsub.vv": SingleWidthIntegerMultiplyAdd,
    "vnmsub.vx": SingleWidthIntegerMultiplyAdd,
    #
    "vwmaccu.vv": WideningIntegerMultiplyAdd,
    "vwmaccu.vx": WideningIntegerMultiplyAdd,
    "vwmacc.vv": WideningIntegerMultiplyAdd,
    "vwmacc.vx": WideningIntegerMultiplyAdd,
    "vwmaccsu.vv": WideningIntegerMultiplyAdd,
    "vwmaccsu.vx": WideningIntegerMultiplyAdd,
    "vwmaccus.vx": WideningIntegerMultiplyAdd,
    #
}
