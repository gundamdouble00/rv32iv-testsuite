    vsetvli a3, a3, e16, mf2, ta, ma
    addi x24, x31, -1292
    vmsltu.vv v4, v5, v24, v0.t #(v_ia_integer_compare)
    addi x22, x0, -40
    vnmsub.vx v20, x24, v14 #(v_ia_single_width_integer_multiply_add)
    addi x10, x29, -337
    vrem.vv v0, v21, v11 #(v_ia_integer_divide)
    addi x15, x15, -771
    vmul.vv v10, v1, v26, v0.t #(v_ia_single_width_integer_multiply)
    addi x22, x0, -28
    vwsubu.wx v10, v16, x11 #(v_ia_widening_integer_add_sub)
    addi x5, x15, 853
    vmsltu.vv v9, v5, v19, v0.t #(v_ia_integer_compare)
    addi x22, x0, 20
    vsse32.v v11, (x21), x22, v0.t #(v_ls_strided)
    addi x22, x0, 120
    vmerge.vvm v21, v14, v17, v0 #(v_ia_integer_merge)
    addi x22, x0, 64
    vloxei8.v v17, (x19), v24, v0.t #(v_ls_indexed)
    addi x22, x0, -32
    vse32.v v21, (x21) #(v_ls_unit_stride)
    addi x25, x12, 524
    vmslt.vx v23, v28, x5, v0.t #(v_ia_integer_compare)
    addi x22, x0, 84
    vsext.vf2 v11, v3 #(v_ia_integer_extension)
    addi x9, x10, 561
    vmerge.vim v23, v21, -2, v0 #(v_ia_integer_merge)
    addi x22, x0, 12
    vadc.vxm v18, v25, x23, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x22, x0, 72
    vwmacc.vv v6, v20, v5 #(v_ia_widening_integer_multiply_add)
    addi x27, x14, 1462
    vmseq.vx v13, v29, x23, v0.t #(v_ia_integer_compare)
    addi x13, x16, 567
    vnmsub.vv v2, v27, v29 #(v_ia_single_width_integer_multiply_add)
    addi x22, x0, 100
    vle8.v v16, (x18), v0.t #(v_ls_unit_stride)
    addi x28, x28, -426
    vsra.vi v16, v6, 14, v0.t #(v_ia_single_width_shift)
    addi x22, x0, -76
    vmadd.vv v22, v25, v9, v0.t #(v_ia_single_width_integer_multiply_add)
    addi x16, x28, -852
    vnsra.wx v5, v10, x12 #(v_ia_narrowing_integer_right_shift)
    addi x22, x0, -24
    vwsubu.vv v16, v15, v3 #(v_ia_widening_integer_add_sub)
    addi x12, x13, -1364
    vmulh.vx v6, v25, x31, v0.t #(v_ia_single_width_integer_multiply)
    addi x22, x0, -124
    vwmulsu.vv v12, v11, v15 #(v_ia_widening_integer_multiply)
    addi x22, x0, -116
    vmsne.vv v14, v7, v20 #(v_ia_integer_compare)
    addi x12, x16, 996
    vsoxei8.v v0, (x21), v24 #(v_ls_indexed)
    addi x22, x0, -80
    vmsle.vv v7, v23, v5 #(v_ia_integer_compare)
    addi x22, x0, 40
    vrsub.vi v14, v8, 7 #(v_ia_single_width_integer_add_sub)
    addi x22, x0, -72
    vmv.v.x v6, x16 #(v_ia_integer_move)
    addi x22, x0, -104
    vmul.vv v20, v30, v30 #(v_ia_single_width_integer_multiply)
    addi x22, x0, 16
    vwmaccus.vx v10, x31, v13, v0.t #(v_ia_widening_integer_multiply_add)
    addi x13, x25, 1868
    vwmul.vv v6, v8, v28 #(v_ia_widening_integer_multiply)
    addi x22, x0, -72
    vluxei16.v v8, (x19), v24, v0.t #(v_ls_indexed)
    addi x22, x0, 52
    vor.vi v17, v14, 6, v0.t #(v_ia_bitwise_logical)
    addi x7, x0, 930
    vmulh.vv v15, v28, v8, v0.t #(v_ia_single_width_integer_multiply)
    addi x13, x23, -1802
    vwsubu.wv v6, v12, v9 #(v_ia_widening_integer_add_sub)
    addi x22, x0, -4
    vmv.v.v v21, v24 #(v_ia_integer_move)
    addi x17, x5, 1435
    vmadd.vx v23, x31, v19, v0.t #(v_ia_single_width_integer_multiply_add)
    addi x22, x0, 72
    vsbc.vvm v7, v17, v13, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x14, x28, 240
    vle32.v v5, (x20), v0.t #(v_ls_unit_stride)
    addi x22, x0, -8
    vadc.vim v15, v8, 1, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x6, x31, 1327
    vsra.vx v5, v26, x23 #(v_ia_single_width_shift)
    addi x22, x0, 12
    vnsrl.wx v17, v4, x30, v0.t #(v_ia_narrowing_integer_right_shift)
    addi x22, x0, -12
    vsoxei8.v v16, (x21), v24, v0.t #(v_ls_indexed)
    addi x22, x0, -112
    vmv.v.x v0, x5 #(v_ia_integer_move)
    addi x16, x26, 1811
    vsuxei32.v v23, (x21), v24 #(v_ls_indexed)
    addi x25, x25, -138
    vlm.v v2, (x19) #(v_ls_unit_stride)
    addi x23, x14, 1402
    vadc.vxm v12, v22, x6, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x30, x7, 524
    vmsleu.vx v3, v7, x23, v0.t #(v_ia_integer_compare)
    addi x5, x6, 1282
    vmsle.vi v3, v13, 5, v0.t #(v_ia_integer_compare)
    addi x22, x0, -48
    vwaddu.vv v2, v7, v21, v0.t #(v_ia_widening_integer_add_sub)
    addi x24, x9, 935
    vadc.vvm v21, v30, v3, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x22, x0, -84
    vmsgt.vi v8, v2, -11, v0.t #(v_ia_integer_compare)
    addi x22, x0, 0
    vse8.v v6, (x21) #(v_ls_unit_stride)
    addi x22, x0, -28
    vloxei32.v v9, (x19), v24, v0.t #(v_ls_indexed)
    addi x22, x0, -8
    vnsra.wx v20, v14, x30, v0.t #(v_ia_narrowing_integer_right_shift)
    addi x22, x0, -44
    vsbc.vvm v20, v13, v22, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x29, x0, 1655
    vmv.v.i v17, -2 #(v_ia_integer_move)
    addi x22, x0, 84
    vnsra.wi v15, v20, 0, v0.t #(v_ia_narrowing_integer_right_shift)
    addi x10, x30, 774
    vmadd.vv v8, v26, v2 #(v_ia_single_width_integer_multiply_add)
    addi x31, x25, -918
    vmul.vv v18, v17, v9 #(v_ia_single_width_integer_multiply)
    addi x22, x0, 68
    vnsra.wx v18, v14, x11, v0.t #(v_ia_narrowing_integer_right_shift)
    addi x27, x25, 574
    vmsbc.vvm v10, v23, v13, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x22, x0, -52
    vmsle.vv v6, v25, v11 #(v_ia_integer_compare)
    addi x22, x0, -44
    vnmsac.vv v21, v13, v9 #(v_ia_single_width_integer_multiply_add)
    addi x6, x17, 470
    vdivu.vv v20, v16, v26, v0.t #(v_ia_integer_divide)
    addi x15, x16, 193
    vwmulu.vx v14, v7, x24 #(v_ia_widening_integer_multiply)
    addi x5, x13, -1193
    vadd.vi v7, v1, -11, v0.t #(v_ia_single_width_integer_add_sub)
    addi x22, x0, -84
    vsuxei8.v v16, (x21), v24 #(v_ls_indexed)
    addi x23, x15, -646
    vlse8.v v9, (x18), x22 #(v_ls_strided)
    addi x27, x13, 888
    vsoxei8.v v22, (x21), v24, v0.t #(v_ls_indexed)
    addi x10, x9, 571
    vmulhsu.vv v22, v24, v19, v0.t #(v_ia_single_width_integer_multiply)
    addi x22, x0, -36
    vmerge.vxm v21, v1, x17, v0 #(v_ia_integer_merge)
    addi x30, x15, 765
    vmsltu.vv v14, v3, v19, v0.t #(v_ia_integer_compare)
    addi x12, x0, -54
    vadc.vvm v10, v2, v17, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x7, x16, 605
    vwaddu.vv v2, v30, v23, v0.t #(v_ia_widening_integer_add_sub)
    addi x22, x0, 72
    vle32ff.v v2, (x20), v0.t #(v_ls_unit_stride)
    addi x22, x0, -4
    vmaxu.vx v18, v31, x25 #(v_ia_integer_min_max)
    addi x22, x0, -92
    vsse8.v v18, (x21), x22 #(v_ls_strided)
    addi x15, x28, -748
    vwmacc.vx v22, x0, v9, v0.t #(v_ia_widening_integer_multiply_add)
    addi x22, x0, -128
    vmul.vx v16, v0, x6 #(v_ia_single_width_integer_multiply)
    addi x23, x7, -1005
    vnsrl.wx v2, v12, x25 #(v_ia_narrowing_integer_right_shift)
    addi x14, x25, 1391
    vmsle.vx v20, v21, x30 #(v_ia_integer_compare)
    addi x26, x9, 1521
    vnmsub.vx v15, x5, v2, v0.t #(v_ia_single_width_integer_multiply_add)
    addi x0, x7, -900
    vxor.vv v1, v10, v22 #(v_ia_bitwise_logical)
    addi x14, x5, 417
    vmaxu.vv v7, v6, v16 #(v_ia_integer_min_max)
    addi x22, x0, 104
    vsoxei16.v v14, (x21), v24, v0.t #(v_ls_indexed)
    addi x22, x0, 100
    vluxei32.v v17, (x18), v24, v0.t #(v_ls_indexed)
    addi x22, x0, 8
    vmv.v.i v18, 2 #(v_ia_integer_move)
    addi x22, x0, 24
    vwsubu.wx v6, v14, x13 #(v_ia_widening_integer_add_sub)
    addi x28, x17, 1289
    vadd.vv v20, v20, v16 #(v_ia_single_width_integer_add_sub)
    addi x22, x0, -76
    vsoxei16.v v23, (x21), v24, v0.t #(v_ls_indexed)
    addi x22, x0, -48
    vremu.vx v5, v13, x16 #(v_ia_integer_divide)
    addi x17, x16, -432
    vzext.vf2 v15, v22 #(v_ia_integer_extension)
    addi x22, x0, 112
    vse32.v v21, (x21) #(v_ls_unit_stride)
    addi x22, x0, -52
    vwmul.vv v4, v23, v1, v0.t #(v_ia_widening_integer_multiply)
    addi x14, x11, 1157
    vmsle.vv v20, v8, v17, v0.t #(v_ia_integer_compare)
    addi x30, x30, -1700
    vwadd.vv v18, v12, v8 #(v_ia_widening_integer_add_sub)
    addi x0, x31, -1468
    vmadc.vvm v18, v28, v24, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x15, x11, 976
    vmin.vx v14, v11, x5, v0.t #(v_ia_integer_min_max)
    addi x27, x23, -1814
    vor.vi v16, v31, 4 #(v_ia_bitwise_logical)
    addi x22, x0, -28
    vmadd.vx v10, x23, v16, v0.t #(v_ia_single_width_integer_multiply_add)
    addi x22, x0, -108
    vsll.vv v11, v2, v11, v0.t #(v_ia_single_width_shift)
    addi x14, x9, -1287
    vmul.vv v16, v3, v19, v0.t #(v_ia_single_width_integer_multiply)
    addi x6, x0, -1423
    vnsra.wi v23, v24, 0 #(v_ia_narrowing_integer_right_shift)
    addi x9, x27, 1886
    vse8.v v23, (x21), v0.t #(v_ls_unit_stride)
    addi x22, x0, -100
    vsext.vf2 v15, v0, v0.t #(v_ia_integer_extension)
    addi x14, x29, -1776
    vmulhu.vx v6, v1, x23 #(v_ia_single_width_integer_multiply)
    addi x29, x11, 1052
    vwmaccu.vv v8, v25, v12 #(v_ia_widening_integer_multiply_add)
    addi x22, x0, -72
    vxor.vi v6, v24, 1 #(v_ia_bitwise_logical)
    addi x22, x0, -16
    vlm.v v22, (x18) #(v_ls_unit_stride)
    addi x10, x7, -202
    vluxei8.v v11, (x18), v24, v0.t #(v_ls_indexed)
    addi x22, x0, 96
    vmadd.vx v23, x10, v31, v0.t #(v_ia_single_width_integer_multiply_add)
    addi x12, x31, 1642
    vnsra.wv v13, v24, v5, v0.t #(v_ia_narrowing_integer_right_shift)
    addi x22, x0, -52
    vdivu.vx v2, v15, x17 #(v_ia_integer_divide)
    addi x9, x14, -1383
    vmaxu.vx v19, v1, x15, v0.t #(v_ia_integer_min_max)
    addi x14, x15, 1338
    vmacc.vv v14, v3, v21, v0.t #(v_ia_single_width_integer_multiply_add)
    addi x24, x14, -401
    vwaddu.wv v8, v0, v3 #(v_ia_widening_integer_add_sub)
    addi x7, x24, -1498
    vmulhu.vv v21, v16, v21 #(v_ia_single_width_integer_multiply)
    addi x22, x0, 80
    vsse8.v v16, (x21), x22 #(v_ls_strided)
    addi x14, x17, 447
    vor.vv v3, v4, v1 #(v_ia_bitwise_logical)
    addi x7, x15, 1975
    vmsleu.vv v19, v31, v23, v0.t #(v_ia_integer_compare)
    addi x22, x0, 8
    vmslt.vx v1, v23, x26, v0.t #(v_ia_integer_compare)
    addi x22, x0, -84
    vwmaccu.vv v16, v11, v27, v0.t #(v_ia_widening_integer_multiply_add)
    addi x22, x0, 44
    vse16.v v12, (x21), v0.t #(v_ls_unit_stride)
    addi x13, x27, 1778
    vmsleu.vv v8, v24, v15, v0.t #(v_ia_integer_compare)
    addi x16, x15, -1023
    vloxei16.v v8, (x20), v24, v0.t #(v_ls_indexed)
    addi x22, x0, -68
    vmsle.vv v2, v14, v27 #(v_ia_integer_compare)
    addi x9, x5, -479
    vmulhsu.vv v17, v5, v29, v0.t #(v_ia_single_width_integer_multiply)
    addi x9, x26, 743
    vse32.v v0, (x21) #(v_ls_unit_stride)
    addi x10, x27, -416
    vand.vv v2, v27, v28 #(v_ia_bitwise_logical)
    addi x13, x31, 612
    vmsgtu.vi v20, v23, 7, v0.t #(v_ia_integer_compare)
    addi x28, x16, -1630
    vmslt.vv v3, v24, v18, v0.t #(v_ia_integer_compare)
    addi x22, x0, -96
    vmaxu.vx v14, v8, x23, v0.t #(v_ia_integer_min_max)
    addi x22, x0, -8
    vsuxei16.v v23, (x21), v24 #(v_ls_indexed)
    addi x28, x23, 325
    vdivu.vx v16, v1, x28, v0.t #(v_ia_integer_divide)
    addi x23, x0, -65
    vwsubu.wv v4, v0, v13, v0.t #(v_ia_widening_integer_add_sub)
    addi x9, x17, 801
    vmsgtu.vi v5, v5, 9, v0.t #(v_ia_integer_compare)
    addi x6, x12, -359
    vnsra.wx v23, v0, x11, v0.t #(v_ia_narrowing_integer_right_shift)
    addi x22, x0, 24
    vmsne.vx v18, v25, x16, v0.t #(v_ia_integer_compare)
    addi x9, x31, 1653
    vminu.vv v5, v10, v5, v0.t #(v_ia_integer_min_max)
    addi x22, x0, -68
    vrsub.vx v15, v9, x14 #(v_ia_single_width_integer_add_sub)
    addi x27, x5, 601
    vmseq.vv v19, v2, v6, v0.t #(v_ia_integer_compare)
    addi x9, x25, 239
    vmadd.vx v5, x13, v4 #(v_ia_single_width_integer_multiply_add)
    addi x22, x0, 52
    vsm.v v2, (x21) #(v_ls_unit_stride)
    addi x7, x0, 714
    vwadd.wv v16, v6, v8 #(v_ia_widening_integer_add_sub)
    addi x22, x0, -56
    vmulhu.vv v1, v24, v24 #(v_ia_single_width_integer_multiply)
    addi x12, x31, -1931
    vrem.vv v23, v2, v27 #(v_ia_integer_divide)
    addi x22, x0, -88
    vsuxei32.v v9, (x21), v24, v0.t #(v_ls_indexed)
    addi x22, x0, -96
    vwadd.wv v22, v28, v5, v0.t #(v_ia_widening_integer_add_sub)
    addi x11, x13, -1226
    vwaddu.wx v10, v14, x12 #(v_ia_widening_integer_add_sub)
    addi x24, x26, 849
    vmulh.vx v23, v3, x10, v0.t #(v_ia_single_width_integer_multiply)
    addi x17, x26, -308
    vmsne.vx v23, v15, x13 #(v_ia_integer_compare)
    addi x11, x25, -1675
    vnmsac.vv v19, v25, v15, v0.t #(v_ia_single_width_integer_multiply_add)
    addi x26, x5, -1537
    vmul.vx v3, v6, x10 #(v_ia_single_width_integer_multiply)
    addi x15, x6, -1290
    vnsrl.wx v4, v10, x24, v0.t #(v_ia_narrowing_integer_right_shift)
    addi x14, x28, 83
    vle8ff.v v3, (x18) #(v_ls_unit_stride)
    addi x22, x0, 56
    vmsltu.vv v23, v10, v26, v0.t #(v_ia_integer_compare)
    addi x22, x0, 124
    vmadc.vxm v11, v9, x6, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x16, x14, 652
    vmadc.vvm v15, v6, v7, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x29, x7, 1525
    vle16ff.v v4, (x19) #(v_ls_unit_stride)
    addi x22, x0, 108
    vrsub.vi v14, v14, -7, v0.t #(v_ia_single_width_integer_add_sub)
    addi x29, x28, -1765
    vlse16.v v4, (x19), x22 #(v_ls_strided)
    addi x22, x0, -100
    vsm.v v9, (x21) #(v_ls_unit_stride)
    addi x0, x10, 939
    vremu.vv v0, v5, v5 #(v_ia_integer_divide)
    addi x22, x0, 48
    vmsne.vx v23, v2, x7, v0.t #(v_ia_integer_compare)
    addi x12, x0, -672
    vwmulsu.vx v14, v5, x12, v0.t #(v_ia_widening_integer_multiply)
    addi x22, x0, -52
    vremu.vv v4, v7, v13, v0.t #(v_ia_integer_divide)
    addi x10, x30, -1870
    vsbc.vvm v4, v15, v15, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x22, x0, 4
    vlse16.v v1, (x19), x22, v0.t #(v_ls_strided)
    addi x22, x0, 108
    vsbc.vxm v13, v21, x13, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x28, x5, 1407
    vsll.vv v21, v5, v4, v0.t #(v_ia_single_width_shift)
    addi x22, x0, 112
    vwaddu.vx v14, v3, x14, v0.t #(v_ia_widening_integer_add_sub)
    addi x16, x13, 1009
    vwmaccus.vx v14, x13, v17 #(v_ia_widening_integer_multiply_add)
    addi x26, x7, 1531
    vsll.vv v16, v20, v0 #(v_ia_single_width_shift)
    addi x28, x27, 1792
    vmseq.vv v1, v12, v14 #(v_ia_integer_compare)
    addi x5, x6, -93
    vmax.vv v17, v29, v30 #(v_ia_integer_min_max)
    addi x22, x0, -40
    vsse8.v v19, (x21), x22 #(v_ls_strided)
    addi x14, x11, 1373
    vmsle.vv v7, v30, v8, v0.t #(v_ia_integer_compare)
    addi x17, x12, -375
    vdivu.vx v14, v9, x23, v0.t #(v_ia_integer_divide)
    addi x28, x9, 32
    vsuxei16.v v12, (x21), v24, v0.t #(v_ls_indexed)
    addi x22, x0, -56
    vmseq.vx v2, v3, x11 #(v_ia_integer_compare)
    addi x28, x30, 1753
    vwmul.vv v18, v29, v5 #(v_ia_widening_integer_multiply)
    addi x22, x0, -96
    vminu.vx v4, v12, x7, v0.t #(v_ia_integer_min_max)
    addi x22, x0, 100
    vmsleu.vx v6, v20, x16 #(v_ia_integer_compare)
    addi x16, x14, 1863
    vsra.vv v1, v9, v15 #(v_ia_single_width_shift)
    addi x23, x23, -1180
    vsll.vx v20, v30, x5 #(v_ia_single_width_shift)
    addi x22, x0, -108
    vand.vv v3, v20, v25 #(v_ia_bitwise_logical)
    addi x6, x11, 232
    vmsle.vi v9, v13, -7, v0.t #(v_ia_integer_compare)
    addi x23, x30, -7
    vlm.v v2, (x20) #(v_ls_unit_stride)
    addi x22, x0, 12
    vwmulu.vx v16, v27, x23, v0.t #(v_ia_widening_integer_multiply)
    addi x22, x0, 44
    vmseq.vx v13, v25, x17 #(v_ia_integer_compare)
    addi x0, x14, -270
    vwsubu.wv v16, v24, v19, v0.t #(v_ia_widening_integer_add_sub)
    addi x23, x30, -1551
    vwmaccsu.vx v14, x13, v1 #(v_ia_widening_integer_multiply_add)
    addi x0, x13, -2036
    vse16.v v23, (x21) #(v_ls_unit_stride)
    addi x11, x26, 416
    vmacc.vx v7, x28, v24, v0.t #(v_ia_single_width_integer_multiply_add)
    addi x22, x0, -76
    vwmaccu.vx v8, x28, v30, v0.t #(v_ia_widening_integer_multiply_add)
    addi x5, x10, 1398
    vsext.vf2 v5, v10, v0.t #(v_ia_integer_extension)
    addi x22, x0, -28
    vmax.vv v9, v8, v11, v0.t #(v_ia_integer_min_max)
    addi x23, x14, -895
    vmslt.vv v12, v13, v20 #(v_ia_integer_compare)
    addi x10, x17, -673
    vmadc.vi v4, v18, -5 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x22, x0, 112
    vle8.v v5, (x18), v0.t #(v_ls_unit_stride)
    addi x22, x0, -12
    vnsrl.wx v4, v18, x15 #(v_ia_narrowing_integer_right_shift)
    addi x9, x31, 395
    vlse8.v v9, (x18), x22 #(v_ls_strided)
    addi x22, x0, -116
    vzext.vf2 v20, v12, v0.t #(v_ia_integer_extension)
    addi x26, x31, 752
    vmslt.vv v5, v22, v24, v0.t #(v_ia_integer_compare)
    addi x26, x29, -981
    vmadc.vx v20, v30, x13 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x7, x23, 1034
    vmerge.vxm v15, v30, x12, v0 #(v_ia_integer_merge)
    addi x22, x0, -28
    vwmacc.vx v8, x23, v20 #(v_ia_widening_integer_multiply_add)
    addi x11, x9, 628
    vmadc.vx v9, v30, x27 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x15, x31, 1184
    vwmulu.vv v8, v12, v22 #(v_ia_widening_integer_multiply)
    addi x14, x10, 1483
    vse16.v v17, (x21) #(v_ls_unit_stride)
    addi x22, x0, 44
    vmsgt.vi v14, v14, -10, v0.t #(v_ia_integer_compare)
    addi x22, x0, 108
    vmerge.vim v5, v30, 10, v0 #(v_ia_integer_merge)
    addi x24, x28, -1983
    vmadc.vvm v5, v27, v24, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x22, x0, -48
    vwmulu.vv v14, v3, v4, v0.t #(v_ia_widening_integer_multiply)
    addi x22, x0, -112
    vwmul.vx v18, v3, x16 #(v_ia_widening_integer_multiply)
    addi x22, x0, -52
    vsrl.vx v12, v14, x0, v0.t #(v_ia_single_width_shift)
    addi x10, x29, 546
    vmsbc.vv v13, v31, v26 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x7, x13, 619
    vmsleu.vv v21, v9, v12 #(v_ia_integer_compare)
    addi x22, x0, 28
    vnsrl.wi v12, v24, 29 #(v_ia_narrowing_integer_right_shift)
    addi x22, x0, 72
    vnsra.wv v17, v8, v6, v0.t #(v_ia_narrowing_integer_right_shift)
    addi x22, x0, 120
    vloxei8.v v2, (x19), v24 #(v_ls_indexed)
    addi x0, x31, -1377
    vmsne.vv v11, v9, v6 #(v_ia_integer_compare)
    addi x14, x28, -1789
    vmsgt.vx v15, v24, x5, v0.t #(v_ia_integer_compare)
    addi x22, x0, -8
    vdiv.vv v10, v21, v11, v0.t #(v_ia_integer_divide)
    addi x23, x13, -1687
    vzext.vf2 v23, v17 #(v_ia_integer_extension)
    addi x12, x7, -61
    vnmsac.vv v9, v31, v1, v0.t #(v_ia_single_width_integer_multiply_add)
    addi x22, x0, -96
    vmerge.vxm v21, v30, x10, v0 #(v_ia_integer_merge)
    addi x13, x30, -1125
    vmv.v.v v1, v1 #(v_ia_integer_move)
    addi x14, x28, 1201
    vmsbc.vv v19, v7, v17 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x22, x0, 108
    vsra.vv v17, v20, v22 #(v_ia_single_width_shift)
    addi x22, x0, -124
    vwaddu.vx v6, v26, x12 #(v_ia_widening_integer_add_sub)
    addi x26, x31, -1055
    vle16.v v19, (x19) #(v_ls_unit_stride)
    addi x22, x0, -96
    vmslt.vx v5, v16, x5 #(v_ia_integer_compare)
    addi x22, x0, 76
    vsrl.vv v21, v9, v6, v0.t #(v_ia_single_width_shift)
    addi x22, x0, -32
    vand.vv v21, v6, v15, v0.t #(v_ia_bitwise_logical)
    addi x0, x7, -146
    vwmul.vx v6, v10, x31, v0.t #(v_ia_widening_integer_multiply)
    addi x0, x28, -330
    vmulhsu.vv v13, v23, v2, v0.t #(v_ia_single_width_integer_multiply)
    addi x12, x27, 1962
    vsse16.v v11, (x21), x22 #(v_ls_strided)
    addi x23, x16, 485
    vmsgt.vx v3, v10, x28, v0.t #(v_ia_integer_compare)
    addi x24, x16, 1390
    vsbc.vvm v3, v24, v6, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x14, x15, -514
    vmseq.vv v6, v20, v26 #(v_ia_integer_compare)
    addi x9, x9, -799
    vmsne.vv v10, v3, v23, v0.t #(v_ia_integer_compare)
    addi x22, x0, -92
    vwmul.vx v4, v12, x17 #(v_ia_widening_integer_multiply)
    addi x29, x29, -1428
    vsse16.v v18, (x21), x22 #(v_ls_strided)
    addi x22, x0, -44
    vnsrl.wv v8, v20, v27, v0.t #(v_ia_narrowing_integer_right_shift)
    addi x22, x0, 36
    vmadc.vvm v16, v3, v9, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x16, x17, 1789
    vle32ff.v v4, (x20) #(v_ls_unit_stride)
    addi x13, x30, -1738
    vremu.vv v1, v30, v21 #(v_ia_integer_divide)
    addi x17, x26, -189
    vand.vi v17, v24, -10, v0.t #(v_ia_bitwise_logical)
    addi x17, x12, 1113
    vmerge.vim v12, v2, 0, v0 #(v_ia_integer_merge)
    addi x24, x13, -1712
    vluxei8.v v18, (x18), v24 #(v_ls_indexed)
    addi x22, x0, -104
    vsra.vi v9, v15, 19, v0.t #(v_ia_single_width_shift)
    addi x30, x6, -2004
    vwmulsu.vv v20, v28, v10 #(v_ia_widening_integer_multiply)
    addi x22, x0, -48
    vmul.vx v4, v10, x15 #(v_ia_single_width_integer_multiply)
    addi x29, x9, 1425
    vsoxei32.v v17, (x21), v24, v0.t #(v_ls_indexed)
    addi x14, x30, 1386
    vsoxei32.v v16, (x21), v24 #(v_ls_indexed)
    addi x22, x0, 8
    vwsub.wv v10, v20, v3, v0.t #(v_ia_widening_integer_add_sub)
    addi x22, x0, -20
    vwsub.wv v14, v10, v9 #(v_ia_widening_integer_add_sub)
    addi x22, x0, 116
    vwadd.wv v10, v8, v31 #(v_ia_widening_integer_add_sub)
    addi x25, x13, -1269
    vor.vx v3, v1, x5 #(v_ia_bitwise_logical)
    addi x14, x24, -1123
    vloxei8.v v5, (x20), v24 #(v_ls_indexed)
    addi x22, x0, -4
    vmulhu.vv v1, v20, v25, v0.t #(v_ia_single_width_integer_multiply)
    addi x22, x0, 48
    vwsubu.vx v16, v15, x6, v0.t #(v_ia_widening_integer_add_sub)
    addi x22, x0, 56
    vzext.vf2 v20, v10, v0.t #(v_ia_integer_extension)
    addi x22, x0, -8
    vwsub.wv v14, v28, v7 #(v_ia_widening_integer_add_sub)
    addi x22, x0, -32
    vmin.vx v4, v28, x24 #(v_ia_integer_min_max)
    addi x22, x0, 0
    vmulhu.vv v17, v29, v17, v0.t #(v_ia_single_width_integer_multiply)
    addi x22, x0, -12
    vmv.v.v v12, v22 #(v_ia_integer_move)
    addi x22, x0, 44
    vsuxei8.v v4, (x21), v24, v0.t #(v_ls_indexed)
    addi x10, x16, -262
    vremu.vx v13, v6, x23, v0.t #(v_ia_integer_divide)
    addi x30, x25, 142
    vminu.vv v23, v16, v5, v0.t #(v_ia_integer_min_max)
    addi x22, x0, 64
    vmulhu.vx v19, v3, x15, v0.t #(v_ia_single_width_integer_multiply)
    addi x23, x23, 228
    vwadd.vx v22, v28, x5, v0.t #(v_ia_widening_integer_add_sub)
    addi x22, x0, 12
    vand.vv v8, v4, v11, v0.t #(v_ia_bitwise_logical)
    addi x25, x7, -318
    vmsleu.vi v14, v12, 14, v0.t #(v_ia_integer_compare)
    addi x22, x0, -92
    vse16.v v2, (x21), v0.t #(v_ls_unit_stride)
    addi x22, x0, -80
    vmulhu.vx v22, v12, x12, v0.t #(v_ia_single_width_integer_multiply)
    addi x22, x0, 120
    vwmulsu.vv v14, v1, v1 #(v_ia_widening_integer_multiply)
    addi x13, x24, 420
    vmerge.vxm v4, v1, x15, v0 #(v_ia_integer_merge)
    addi x31, x31, -1424
    vwsubu.wv v2, v18, v20, v0.t #(v_ia_widening_integer_add_sub)
    addi x22, x0, -116
    vmv.v.i v7, 5 #(v_ia_integer_move)
    addi x22, x0, -68
    vsra.vv v13, v12, v5 #(v_ia_single_width_shift)
    addi x22, x0, -100
    vsll.vx v1, v4, x23, v0.t #(v_ia_single_width_shift)
    addi x17, x24, -306
    vmsle.vi v14, v11, -4, v0.t #(v_ia_integer_compare)
    addi x22, x0, -68
    vloxei16.v v9, (x20), v24 #(v_ls_indexed)
    addi x22, x0, 80
    vsuxei16.v v1, (x21), v24, v0.t #(v_ls_indexed)
    addi x23, x6, -975
    vmulh.vx v4, v11, x28 #(v_ia_single_width_integer_multiply)
    addi x31, x17, -2016
    vwsub.wv v8, v24, v25, v0.t #(v_ia_widening_integer_add_sub)
    addi x7, x16, -1378
    vle16.v v8, (x19), v0.t #(v_ls_unit_stride)
    addi x22, x0, 0
    vnsra.wi v4, v16, 31 #(v_ia_narrowing_integer_right_shift)
    addi x22, x0, 120
    vwadd.wx v6, v10, x7 #(v_ia_widening_integer_add_sub)
    addi x22, x0, -4
    vsext.vf2 v10, v6, v0.t #(v_ia_integer_extension)
    addi x22, x0, 108
    vadc.vxm v2, v5, x0, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x12, x26, -1712
    vmsgt.vx v5, v18, x10 #(v_ia_integer_compare)
    addi x26, x11, -852
    vmseq.vi v20, v27, 0, v0.t #(v_ia_integer_compare)
    addi x17, x5, 1743
    vwmacc.vx v12, x27, v25 #(v_ia_widening_integer_multiply_add)
    addi x22, x0, 52
    vmsne.vv v4, v30, v17, v0.t #(v_ia_integer_compare)
    addi x22, x0, -112
    vmsbc.vv v5, v30, v9 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x22, x0, 52
    vwadd.vv v2, v27, v30, v0.t #(v_ia_widening_integer_add_sub)
    addi x30, x0, -1272
    vsoxei16.v v20, (x21), v24 #(v_ls_indexed)
    addi x7, x23, -1942
    vluxei8.v v3, (x19), v24, v0.t #(v_ls_indexed)
    addi x6, x24, 1683
    vsra.vi v1, v20, 22, v0.t #(v_ia_single_width_shift)
    addi x16, x31, -1244
    vnmsac.vx v1, x10, v10, v0.t #(v_ia_single_width_integer_multiply_add)
    addi x22, x0, 80
    vlse32.v v16, (x20), x22 #(v_ls_strided)
    addi x13, x25, 153
    vwsubu.wv v14, v2, v31 #(v_ia_widening_integer_add_sub)
    addi x22, x0, 12
    vwsub.vx v22, v2, x5, v0.t #(v_ia_widening_integer_add_sub)
    addi x30, x30, 226
    vremu.vv v19, v5, v15 #(v_ia_integer_divide)
    addi x16, x26, 630
    vlm.v v14, (x20) #(v_ls_unit_stride)
    addi x22, x0, 112
    vmul.vx v1, v22, x31 #(v_ia_single_width_integer_multiply)
    addi x22, x0, -76
    vwadd.vx v8, v0, x13, v0.t #(v_ia_widening_integer_add_sub)
    addi x5, x10, -1532
    vsext.vf2 v4, v17 #(v_ia_integer_extension)
    addi x22, x0, 52
    vmsltu.vv v17, v11, v25 #(v_ia_integer_compare)
    addi x5, x23, -1577
    vmerge.vim v17, v5, -16, v0 #(v_ia_integer_merge)
    addi x27, x28, -1012
    vmseq.vx v22, v27, x9 #(v_ia_integer_compare)
    addi x22, x0, 28
    vsll.vv v9, v2, v2, v0.t #(v_ia_single_width_shift)
    addi x11, x17, -1195
    vsll.vv v14, v2, v30, v0.t #(v_ia_single_width_shift)
    addi x24, x0, -331
    vwadd.vx v4, v25, x30, v0.t #(v_ia_widening_integer_add_sub)
    addi x22, x0, -84
    vwsub.vx v8, v4, x15 #(v_ia_widening_integer_add_sub)
    addi x22, x0, -96
    vwmaccsu.vv v10, v27, v22 #(v_ia_widening_integer_multiply_add)
    addi x12, x9, 574
    vle8ff.v v10, (x18) #(v_ls_unit_stride)
    addi x22, x0, -100
    vse32.v v6, (x21) #(v_ls_unit_stride)
    addi x22, x0, 64
    vsll.vi v6, v1, 18, v0.t #(v_ia_single_width_shift)
    addi x22, x0, -128
    vrsub.vi v9, v7, 9, v0.t #(v_ia_single_width_integer_add_sub)
    addi x22, x0, -76
    vwaddu.vv v8, v19, v27, v0.t #(v_ia_widening_integer_add_sub)
    addi x25, x5, -770
    vwaddu.wx v20, v6, x0, v0.t #(v_ia_widening_integer_add_sub)
    addi x22, x0, 28
    vand.vv v12, v23, v13 #(v_ia_bitwise_logical)
    addi x15, x6, -1558
    vsoxei8.v v0, (x21), v24 #(v_ls_indexed)
    addi x10, x9, 922
    vsll.vi v5, v4, 21, v0.t #(v_ia_single_width_shift)
    addi x22, x0, -12
    vluxei32.v v16, (x18), v24 #(v_ls_indexed)
    addi x22, x0, 76
    vsbc.vvm v20, v24, v23, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x22, x0, 96
    vmacc.vx v6, x23, v20, v0.t #(v_ia_single_width_integer_multiply_add)
    addi x22, x0, -28
    vmsgtu.vx v15, v2, x24 #(v_ia_integer_compare)
    addi x26, x6, 396
    vmsltu.vx v4, v18, x27, v0.t #(v_ia_integer_compare)
    addi x23, x31, 1802
    vlse32.v v19, (x20), x22 #(v_ls_strided)
    addi x16, x7, 555
    vmsgt.vi v17, v29, 7, v0.t #(v_ia_integer_compare)
    addi x22, x0, 32
    vrsub.vx v23, v13, x30 #(v_ia_single_width_integer_add_sub)
    addi x22, x0, 80
    vxor.vx v4, v1, x12 #(v_ia_bitwise_logical)
    addi x22, x0, -28
    vluxei16.v v5, (x20), v24 #(v_ls_indexed)
    addi x31, x25, -120
    vmulh.vv v0, v2, v17 #(v_ia_single_width_integer_multiply)
    addi x22, x0, 56
    vzext.vf2 v14, v7 #(v_ia_integer_extension)
    addi x22, x0, -8
    vsra.vv v0, v4, v8 #(v_ia_single_width_shift)
    addi x27, x23, -56
    vsext.vf2 v9, v8 #(v_ia_integer_extension)
    addi x22, x0, -48
    vluxei8.v v23, (x19), v24, v0.t #(v_ls_indexed)
    addi x22, x0, 56
    vmulhsu.vx v21, v7, x6, v0.t #(v_ia_single_width_integer_multiply)
    addi x15, x12, -611
    vmsle.vi v7, v22, -9, v0.t #(v_ia_integer_compare)
    addi x22, x0, 124
    vsuxei16.v v9, (x21), v24, v0.t #(v_ls_indexed)
    addi x22, x0, -108
    vloxei32.v v20, (x18), v24 #(v_ls_indexed)
    addi x22, x0, 12
    vwmaccsu.vx v2, x28, v29, v0.t #(v_ia_widening_integer_multiply_add)
    addi x22, x0, -112
    vnsrl.wx v4, v16, x23 #(v_ia_narrowing_integer_right_shift)
    addi x7, x24, -67
    vor.vx v16, v6, x27 #(v_ia_bitwise_logical)
    addi x22, x0, -60
    vmv.v.x v23, x24 #(v_ia_integer_move)
    addi x6, x5, 609
    vmsltu.vv v16, v28, v22, v0.t #(v_ia_integer_compare)
    addi x22, x0, -24
    vmaxu.vx v10, v5, x17, v0.t #(v_ia_integer_min_max)
    addi x24, x13, 1485
    vsra.vv v10, v6, v13, v0.t #(v_ia_single_width_shift)
    addi x22, x0, -124
    vmulhsu.vx v12, v21, x6, v0.t #(v_ia_single_width_integer_multiply)
    addi x26, x7, -1037
    vnsrl.wx v2, v16, x25, v0.t #(v_ia_narrowing_integer_right_shift)
    addi x16, x9, -1749
    vmsbc.vvm v23, v21, v12, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x22, x0, -108
    vand.vi v15, v19, -3, v0.t #(v_ia_bitwise_logical)
    addi x16, x26, -1583
    vmsleu.vi v11, v22, 8 #(v_ia_integer_compare)
    addi x22, x0, 56
    vmsbc.vvm v2, v9, v29, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x22, x0, -52
    vmseq.vv v4, v24, v29, v0.t #(v_ia_integer_compare)
    addi x10, x12, -1226
    vnsrl.wv v8, v6, v22 #(v_ia_narrowing_integer_right_shift)
    addi x22, x0, 88
    vsrl.vi v6, v27, 18, v0.t #(v_ia_single_width_shift)
    addi x25, x7, -290
    vnsra.wv v7, v14, v5 #(v_ia_narrowing_integer_right_shift)
    addi x11, x30, 708
    vremu.vv v4, v27, v11, v0.t #(v_ia_integer_divide)
    addi x16, x13, 1056
    vlm.v v3, (x20) #(v_ls_unit_stride)
    addi x24, x11, -432
    vsra.vv v11, v26, v7, v0.t #(v_ia_single_width_shift)
    addi x10, x13, 274
    vwadd.wv v2, v12, v9, v0.t #(v_ia_widening_integer_add_sub)
    addi x22, x0, 0
    vwsubu.vv v18, v3, v12, v0.t #(v_ia_widening_integer_add_sub)
    addi x22, x0, 112
    vwmulsu.vv v4, v0, v10, v0.t #(v_ia_widening_integer_multiply)
    addi x22, x0, -44
    vrsub.vi v13, v29, -9 #(v_ia_single_width_integer_add_sub)
    addi x22, x0, 92
    vmul.vv v10, v8, v2 #(v_ia_single_width_integer_multiply)
    addi x15, x13, -392
    vwadd.wx v16, v20, x7 #(v_ia_widening_integer_add_sub)
    addi x22, x0, -120
    vmerge.vvm v7, v23, v16, v0 #(v_ia_integer_merge)
    addi x22, x0, -4
    vloxei32.v v2, (x18), v24 #(v_ls_indexed)
    addi x22, x0, 8
    vmsle.vx v18, v15, x5, v0.t #(v_ia_integer_compare)
    addi x27, x30, -1099
    vdiv.vx v10, v3, x10, v0.t #(v_ia_integer_divide)
    addi x22, x0, -96
    vmsbc.vxm v13, v10, x14, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x22, x0, 40
    vmin.vv v13, v14, v24, v0.t #(v_ia_integer_min_max)
    addi x10, x7, -31
    vsbc.vxm v16, v17, x10, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x22, x0, 68
    vse32.v v18, (x21) #(v_ls_unit_stride)
    addi x31, x28, 784
    vand.vx v8, v15, x15, v0.t #(v_ia_bitwise_logical)
    addi x27, x13, 1501
    vwsubu.vv v22, v27, v19, v0.t #(v_ia_widening_integer_add_sub)
    addi x22, x0, -124
    vdivu.vx v2, v29, x30, v0.t #(v_ia_integer_divide)
    addi x7, x16, -607
    vle16.v v17, (x19) #(v_ls_unit_stride)
    addi x22, x0, -124
    vwmulu.vv v12, v26, v30 #(v_ia_widening_integer_multiply)
    addi x29, x31, -1936
    vnsrl.wx v8, v2, x26, v0.t #(v_ia_narrowing_integer_right_shift)
    addi x22, x0, 24
    vse8.v v15, (x21), v0.t #(v_ls_unit_stride)
    addi x22, x0, 92
    vse8.v v0, (x21) #(v_ls_unit_stride)
    addi x16, x0, -1702
    vwmacc.vv v4, v17, v13, v0.t #(v_ia_widening_integer_multiply_add)
    addi x27, x15, 128
    vmsbc.vx v9, v28, x10 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x22, x0, 32
    vwmulsu.vv v4, v12, v3, v0.t #(v_ia_widening_integer_multiply)
    addi x22, x0, -12
    vmin.vv v18, v11, v12, v0.t #(v_ia_integer_min_max)
    addi x22, x0, 112
    vnmsac.vv v15, v3, v24, v0.t #(v_ia_single_width_integer_multiply_add)
    addi x15, x12, 666
    vwmul.vx v8, v10, x17 #(v_ia_widening_integer_multiply)
    addi x0, x11, -1442
    vmseq.vi v4, v25, 1, v0.t #(v_ia_integer_compare)
    addi x5, x31, -377
    vnsra.wi v11, v8, 13 #(v_ia_narrowing_integer_right_shift)
    addi x28, x26, 1610
    vor.vi v14, v19, -16 #(v_ia_bitwise_logical)
    addi x22, x0, -56
    vwmulu.vv v6, v31, v30 #(v_ia_widening_integer_multiply)
    addi x7, x25, 1733
    vmsbc.vvm v10, v23, v31, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x30, x31, -1183
    vmulh.vx v14, v1, x7 #(v_ia_single_width_integer_multiply)
    addi x22, x0, -72
    vmulh.vv v2, v4, v3 #(v_ia_single_width_integer_multiply)
    addi x9, x14, -1439
    vmsne.vv v21, v16, v29 #(v_ia_integer_compare)
    addi x9, x9, -686
    vwsubu.vx v22, v5, x10 #(v_ia_widening_integer_add_sub)
    addi x22, x0, -4
    vmulhu.vv v2, v10, v12 #(v_ia_single_width_integer_multiply)
    addi x7, x0, 1575
    vnsrl.wx v6, v4, x16, v0.t #(v_ia_narrowing_integer_right_shift)
    addi x10, x30, -309
    vmsleu.vx v8, v14, x23 #(v_ia_integer_compare)
    addi x25, x31, 83
    vxor.vx v2, v12, x27, v0.t #(v_ia_bitwise_logical)
    addi x22, x0, 112
    vsrl.vx v1, v15, x28, v0.t #(v_ia_single_width_shift)
    addi x31, x29, 1941
    vmsbc.vv v4, v1, v31 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x22, x0, -104
    vluxei8.v v14, (x19), v24, v0.t #(v_ls_indexed)
    addi x6, x5, -1362
    vxor.vv v3, v21, v16 #(v_ia_bitwise_logical)
    addi x22, x0, -8
    vwsub.vx v18, v20, x7, v0.t #(v_ia_widening_integer_add_sub)
    addi x22, x0, -16
    vor.vi v8, v8, 10 #(v_ia_bitwise_logical)
    addi x7, x6, 1703
    vmadd.vv v18, v17, v23, v0.t #(v_ia_single_width_integer_multiply_add)
    addi x30, x29, -2000
    vsub.vx v11, v6, x30 #(v_ia_single_width_integer_add_sub)
    addi x0, x26, 1701
    vsrl.vv v8, v25, v15, v0.t #(v_ia_single_width_shift)
    addi x28, x5, 638
    vnmsac.vx v7, x27, v19 #(v_ia_single_width_integer_multiply_add)
    addi x30, x13, 775
    vmulhu.vx v3, v22, x12 #(v_ia_single_width_integer_multiply)
    addi x22, x0, -76
    vnmsac.vv v7, v11, v2 #(v_ia_single_width_integer_multiply_add)
    addi x27, x14, 105
    vwadd.wv v16, v28, v20 #(v_ia_widening_integer_add_sub)
    addi x22, x0, 44
    vmsltu.vv v11, v30, v16, v0.t #(v_ia_integer_compare)
    addi x22, x0, 8
    vsrl.vx v14, v27, x12 #(v_ia_single_width_shift)
    addi x26, x6, 1217
    vwadd.wx v16, v24, x17 #(v_ia_widening_integer_add_sub)
    addi x22, x0, 76
    vsoxei16.v v10, (x21), v24 #(v_ls_indexed)
    addi x30, x5, 799
    vwmacc.vx v8, x25, v28, v0.t #(v_ia_widening_integer_multiply_add)
    addi x22, x0, -28
    vwadd.vx v2, v0, x0, v0.t #(v_ia_widening_integer_add_sub)
    addi x22, x0, 92
    vmulh.vx v14, v13, x5 #(v_ia_single_width_integer_multiply)
    addi x10, x14, 325
    vrsub.vi v17, v17, 2 #(v_ia_single_width_integer_add_sub)
    addi x22, x0, 32
    vwsub.wx v22, v18, x29, v0.t #(v_ia_widening_integer_add_sub)
    addi x22, x0, 20
    vand.vi v2, v4, -4, v0.t #(v_ia_bitwise_logical)
    addi x22, x0, 12
    vsm.v v0, (x21) #(v_ls_unit_stride)
    addi x7, x16, 1450
    vle8.v v15, (x18), v0.t #(v_ls_unit_stride)
    addi x27, x28, 6
    vmv.v.x v7, x13 #(v_ia_integer_move)
    addi x22, x0, -56
    vrem.vx v1, v14, x11, v0.t #(v_ia_integer_divide)
    addi x24, x29, 1550
    vwadd.wx v4, v10, x12, v0.t #(v_ia_widening_integer_add_sub)
    addi x22, x0, -20
    vmadd.vx v2, x11, v5 #(v_ia_single_width_integer_multiply_add)
    addi x7, x10, 1963
    vmsbc.vvm v14, v3, v12, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x22, x0, -108
    vmslt.vx v18, v4, x14 #(v_ia_integer_compare)
    addi x22, x0, -96
    vor.vx v5, v23, x27, v0.t #(v_ia_bitwise_logical)
    addi x22, x0, -32
    vwsubu.vv v18, v7, v29 #(v_ia_widening_integer_add_sub)
    addi x22, x0, -24
    vadd.vx v22, v2, x0 #(v_ia_single_width_integer_add_sub)
    addi x22, x0, 44
    vmadd.vv v14, v28, v2 #(v_ia_single_width_integer_multiply_add)
    addi x22, x0, 48
    vmax.vv v18, v5, v24, v0.t #(v_ia_integer_min_max)
    addi x22, x0, 64
    vsra.vv v19, v1, v7, v0.t #(v_ia_single_width_shift)
    addi x5, x0, 50
    vwmul.vx v2, v30, x30, v0.t #(v_ia_widening_integer_multiply)
    addi x6, x31, -660
    vwsub.wx v22, v14, x9, v0.t #(v_ia_widening_integer_add_sub)
    addi x25, x16, -1126
    vadc.vxm v21, v16, x9, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x11, x15, -2031
    vzext.vf2 v0, v19 #(v_ia_integer_extension)
    addi x22, x0, -36
    vlse8.v v10, (x18), x22, v0.t #(v_ls_strided)
    addi x22, x0, 72
    vmulhu.vx v16, v5, x17, v0.t #(v_ia_single_width_integer_multiply)
    addi x27, x24, -758
    vmadc.vxm v22, v18, x10, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x31, x23, -621
    vwsub.vv v6, v13, v23, v0.t #(v_ia_widening_integer_add_sub)
    addi x31, x5, 860
    vloxei8.v v16, (x19), v24, v0.t #(v_ls_indexed)
    addi x10, x24, 1665
    vwsub.vx v12, v8, x24 #(v_ia_widening_integer_add_sub)
    addi x30, x28, 859
    vmsne.vi v16, v22, -10, v0.t #(v_ia_integer_compare)
    addi x17, x5, -231
    vmsltu.vv v2, v10, v3, v0.t #(v_ia_integer_compare)
    addi x25, x24, 1439
    vsoxei8.v v19, (x21), v24, v0.t #(v_ls_indexed)
    addi x10, x11, 2035
    vsbc.vvm v1, v25, v29, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x0, x27, -835
    vmslt.vx v0, v5, x15 #(v_ia_integer_compare)
    addi x7, x5, -187
    vwmacc.vv v16, v29, v0 #(v_ia_widening_integer_multiply_add)
    addi x11, x26, 375
    vsll.vv v23, v3, v16 #(v_ia_single_width_shift)
    addi x17, x15, -1321
    vmseq.vi v11, v14, -3 #(v_ia_integer_compare)
    addi x0, x15, 1124
    vsbc.vvm v18, v16, v25, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x22, x0, -76
    vadc.vim v1, v26, -5, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x5, x31, 1071
    vluxei16.v v1, (x19), v24 #(v_ls_indexed)
    addi x6, x6, -1505
    vminu.vv v5, v3, v22 #(v_ia_integer_min_max)
    addi x22, x0, 96
    vlse16.v v6, (x19), x22, v0.t #(v_ls_strided)
    addi x22, x0, 96
    vzext.vf2 v12, v17 #(v_ia_integer_extension)
    addi x30, x17, 1280
    vnmsac.vx v21, x7, v28, v0.t #(v_ia_single_width_integer_multiply_add)
    addi x22, x0, 76
    vsbc.vvm v6, v15, v21, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x13, x10, 1973
    vmsleu.vx v7, v29, x25, v0.t #(v_ia_integer_compare)
    addi x22, x0, -68
    vmsbc.vxm v19, v17, x5, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x30, x26, -883
    vor.vx v21, v27, x16, v0.t #(v_ia_bitwise_logical)
    addi x22, x0, 20
    vwaddu.wv v4, v16, v24, v0.t #(v_ia_widening_integer_add_sub)
    addi x22, x0, -92
    vor.vx v5, v27, x13, v0.t #(v_ia_bitwise_logical)
    addi x15, x7, -1728
    vnsra.wx v7, v26, x30 #(v_ia_narrowing_integer_right_shift)
    addi x22, x0, -44
    vmsle.vv v5, v29, v14, v0.t #(v_ia_integer_compare)
    addi x14, x14, -732
    vmsne.vx v2, v20, x30, v0.t #(v_ia_integer_compare)
    addi x22, x0, -84
    vrsub.vx v1, v1, x29 #(v_ia_single_width_integer_add_sub)
    addi x17, x25, 417
    vadd.vi v22, v1, -3 #(v_ia_single_width_integer_add_sub)
    addi x22, x0, -12
    vmslt.vx v7, v10, x25, v0.t #(v_ia_integer_compare)
    addi x22, x0, 16
    vluxei32.v v18, (x20), v24, v0.t #(v_ls_indexed)
    addi x22, x0, -104
    vmsltu.vv v2, v23, v22 #(v_ia_integer_compare)
    addi x22, x0, -40
    vmulhsu.vx v18, v5, x10, v0.t #(v_ia_single_width_integer_multiply)
    addi x22, x0, -120
    vlse16.v v15, (x19), x22, v0.t #(v_ls_strided)
    addi x13, x7, -1399
    vnsra.wi v0, v16, 10 #(v_ia_narrowing_integer_right_shift)
    addi x22, x0, 116
    vwsubu.vx v12, v28, x11, v0.t #(v_ia_widening_integer_add_sub)
    addi x30, x26, 2038
    vwmul.vv v16, v28, v9 #(v_ia_widening_integer_multiply)
    addi x22, x0, -116
    vwadd.vv v6, v5, v26 #(v_ia_widening_integer_add_sub)
    addi x22, x0, -16
    vmerge.vim v18, v14, 15, v0 #(v_ia_integer_merge)
    addi x7, x15, 1353
    vmaxu.vv v8, v12, v15 #(v_ia_integer_min_max)
    addi x22, x0, 88
    vmseq.vv v7, v0, v0 #(v_ia_integer_compare)
    addi x29, x6, -695
    vnmsub.vx v7, x9, v4, v0.t #(v_ia_single_width_integer_multiply_add)
    addi x28, x27, 484
    vdiv.vv v20, v16, v31, v0.t #(v_ia_integer_divide)
    addi x22, x0, 36
    vnsra.wi v18, v8, 13, v0.t #(v_ia_narrowing_integer_right_shift)
    addi x13, x12, 1304
    vand.vi v6, v31, 1, v0.t #(v_ia_bitwise_logical)
    addi x12, x25, -1067
    vmacc.vx v17, x17, v25 #(v_ia_single_width_integer_multiply_add)
    addi x13, x30, 1272
    vsext.vf2 v8, v19, v0.t #(v_ia_integer_extension)
    addi x22, x0, -32
    vluxei32.v v5, (x18), v24, v0.t #(v_ls_indexed)
    addi x25, x0, 93
    vwmaccsu.vv v10, v13, v1 #(v_ia_widening_integer_multiply_add)
    addi x28, x23, 1848
    vwsub.vv v6, v23, v17, v0.t #(v_ia_widening_integer_add_sub)
    addi x22, x0, -72
    vloxei16.v v10, (x19), v24 #(v_ls_indexed)
    addi x22, x0, -96
    vsoxei8.v v7, (x21), v24 #(v_ls_indexed)
    addi x23, x17, -1129
    vnmsub.vx v22, x6, v5 #(v_ia_single_width_integer_multiply_add)
    addi x24, x27, 774
    vsext.vf2 v12, v0, v0.t #(v_ia_integer_extension)
    addi x7, x13, 1830
    vmsleu.vx v12, v19, x13 #(v_ia_integer_compare)
    addi x22, x0, 72
    vwmaccsu.vv v22, v11, v11, v0.t #(v_ia_widening_integer_multiply_add)
    addi x16, x28, -463
    vsbc.vvm v4, v12, v18, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x22, x0, 96
    vmsleu.vv v8, v17, v28 #(v_ia_integer_compare)
    addi x22, x0, 28
    vmseq.vi v11, v20, 2 #(v_ia_integer_compare)
    addi x9, x24, -650
    vmsltu.vv v20, v14, v28, v0.t #(v_ia_integer_compare)
    addi x13, x13, 346
    vwmacc.vv v8, v0, v3, v0.t #(v_ia_widening_integer_multiply_add)
    addi x22, x0, -60
    vle32.v v2, (x20) #(v_ls_unit_stride)
    addi x28, x7, -623
    vwadd.vv v18, v6, v20, v0.t #(v_ia_widening_integer_add_sub)
    addi x16, x31, -732
    vwsubu.vv v4, v21, v21, v0.t #(v_ia_widening_integer_add_sub)
    addi x31, x9, 411
    vmsleu.vi v4, v18, -9 #(v_ia_integer_compare)
    addi x26, x15, 573
    vsext.vf2 v8, v6, v0.t #(v_ia_integer_extension)
    addi x22, x0, -48
    vremu.vv v9, v15, v31, v0.t #(v_ia_integer_divide)
    addi x22, x0, 80
    vminu.vv v3, v2, v1, v0.t #(v_ia_integer_min_max)
    addi x0, x13, -234
    vsra.vx v4, v11, x7, v0.t #(v_ia_single_width_shift)
    addi x11, x31, 974
    vmslt.vx v11, v20, x25 #(v_ia_integer_compare)
    addi x6, x6, -1836
    vsoxei8.v v9, (x21), v24 #(v_ls_indexed)
    addi x16, x16, 1522
    vsrl.vv v14, v0, v12 #(v_ia_single_width_shift)
    addi x27, x0, -733
    vmsltu.vv v9, v19, v26, v0.t #(v_ia_integer_compare)
    addi x22, x0, 68
    vnsra.wx v8, v10, x31 #(v_ia_narrowing_integer_right_shift)
    addi x22, x0, -120
    vmaxu.vv v23, v2, v11, v0.t #(v_ia_integer_min_max)
    addi x22, x0, -96
    vloxei32.v v5, (x19), v24 #(v_ls_indexed)
    addi x22, x0, -104
    vmsbc.vx v16, v31, x15 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x22, x0, -8
    vmsne.vi v3, v15, -2, v0.t #(v_ia_integer_compare)
    addi x22, x0, 96
    vle16ff.v v23, (x19) #(v_ls_unit_stride)
    addi x29, x0, 1915
    vzext.vf2 v10, v23 #(v_ia_integer_extension)
    addi x22, x0, 100
    vnsrl.wi v15, v18, 29, v0.t #(v_ia_narrowing_integer_right_shift)
    addi x25, x0, 1911
    vse16.v v13, (x21) #(v_ls_unit_stride)
    addi x9, x10, 1655
    vnmsac.vx v6, x23, v12, v0.t #(v_ia_single_width_integer_multiply_add)
    addi x22, x0, 80
    vluxei32.v v13, (x20), v24, v0.t #(v_ls_indexed)
    addi x22, x0, 52
    vrsub.vi v2, v8, -11 #(v_ia_single_width_integer_add_sub)
    addi x29, x9, -1815
    vwsubu.wx v4, v28, x6, v0.t #(v_ia_widening_integer_add_sub)
    addi x22, x0, 72
    vsrl.vx v11, v23, x11 #(v_ia_single_width_shift)
    addi x22, x0, 124
    vwmulu.vx v2, v31, x26 #(v_ia_widening_integer_multiply)
    addi x25, x31, -683
    vwmaccsu.vx v8, x12, v31, v0.t #(v_ia_widening_integer_multiply_add)
    addi x30, x5, 1645
    vmerge.vvm v11, v10, v8, v0 #(v_ia_integer_merge)
    addi x25, x29, 1709
    vwadd.wx v6, v28, x0 #(v_ia_widening_integer_add_sub)
    addi x25, x7, 179
    vxor.vv v23, v15, v24, v0.t #(v_ia_bitwise_logical)
    addi x27, x29, -1316
    vwadd.vv v4, v12, v27, v0.t #(v_ia_widening_integer_add_sub)
    addi x15, x16, -1336
    vmv.v.i v17, 6 #(v_ia_integer_move)
    addi x22, x0, -40
    vsoxei8.v v1, (x21), v24, v0.t #(v_ls_indexed)
    addi x22, x0, 100
    vnsra.wi v7, v30, 18 #(v_ia_narrowing_integer_right_shift)
    addi x14, x15, 1298
    vmsbc.vv v7, v24, v9 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x15, x27, -421
    vle16ff.v v2, (x19), v0.t #(v_ls_unit_stride)
    addi x22, x0, 52
    vor.vi v19, v16, -5 #(v_ia_bitwise_logical)
    addi x22, x0, -8
    vmadd.vx v17, x11, v24 #(v_ia_single_width_integer_multiply_add)
    addi x23, x24, 706
    vmadc.vi v4, v9, 14 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x22, x0, -120
    vmax.vv v22, v23, v18, v0.t #(v_ia_integer_min_max)
    addi x22, x0, -12
    vnmsub.vx v3, x6, v24 #(v_ia_single_width_integer_multiply_add)
    addi x0, x29, -1566
    vor.vx v21, v21, x27, v0.t #(v_ia_bitwise_logical)
    addi x22, x0, 12
    vmslt.vx v7, v18, x31, v0.t #(v_ia_integer_compare)
    addi x29, x13, -1498
    vle8.v v21, (x18), v0.t #(v_ls_unit_stride)
    addi x29, x5, 943
    vwmaccu.vv v20, v8, v29, v0.t #(v_ia_widening_integer_multiply_add)
    addi x22, x0, -40
    vmsleu.vv v22, v28, v7 #(v_ia_integer_compare)
    addi x22, x0, -60
    vwaddu.vx v12, v5, x15, v0.t #(v_ia_widening_integer_add_sub)
    addi x14, x15, -773
    vadc.vxm v13, v7, x5, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x7, x6, 1206
    vadd.vv v17, v20, v29 #(v_ia_single_width_integer_add_sub)
    addi x22, x0, 56
    vmadc.vim v18, v27, -1, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x22, x0, 56
    vwsubu.wx v12, v2, x27 #(v_ia_widening_integer_add_sub)
    addi x14, x16, -345
    vmsbc.vvm v4, v21, v19, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x22, x0, -112
    vadc.vvm v16, v31, v19, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x6, x29, -983
    vor.vi v0, v27, -2 #(v_ia_bitwise_logical)
    addi x16, x23, 21
    vnsra.wv v22, v8, v17, v0.t #(v_ia_narrowing_integer_right_shift)
    addi x22, x0, 100
    vor.vx v3, v21, x10 #(v_ia_bitwise_logical)
    addi x0, x11, -388
    vnsrl.wi v19, v26, 8, v0.t #(v_ia_narrowing_integer_right_shift)
    addi x12, x29, -86
    vmax.vv v20, v8, v23 #(v_ia_integer_min_max)
    addi x14, x0, 360
    vmseq.vi v8, v24, -1, v0.t #(v_ia_integer_compare)
    addi x16, x30, -1917
    vwmaccu.vx v22, x16, v16 #(v_ia_widening_integer_multiply_add)
    addi x22, x0, -120
    vzext.vf2 v17, v9 #(v_ia_integer_extension)
    addi x25, x0, 605
    vxor.vi v17, v0, 4 #(v_ia_bitwise_logical)
    addi x22, x0, -88
    vmv.v.x v7, x23 #(v_ia_integer_move)
    addi x22, x0, 52
    vlse8.v v21, (x18), x22 #(v_ls_strided)
    addi x22, x0, -124
    vsm.v v17, (x21) #(v_ls_unit_stride)
    addi x13, x17, -41
    vor.vx v1, v13, x7 #(v_ia_bitwise_logical)
    addi x5, x6, 1232
    vsoxei8.v v1, (x21), v24, v0.t #(v_ls_indexed)
    addi x22, x0, 88
    vnsrl.wv v4, v18, v2 #(v_ia_narrowing_integer_right_shift)
    addi x14, x28, -55
    vluxei32.v v19, (x19), v24, v0.t #(v_ls_indexed)
    addi x11, x17, 995
    vxor.vv v19, v20, v18 #(v_ia_bitwise_logical)
    addi x22, x0, 84
    vnmsub.vx v9, x11, v16, v0.t #(v_ia_single_width_integer_multiply_add)
    addi x27, x7, 1882
    vle8.v v23, (x18), v0.t #(v_ls_unit_stride)
    addi x12, x26, -1319
    vmsne.vv v0, v6, v9 #(v_ia_integer_compare)
    addi x17, x9, -121
    vmul.vv v5, v7, v13 #(v_ia_single_width_integer_multiply)
    addi x6, x10, -1109
    vnsrl.wi v18, v14, 23 #(v_ia_narrowing_integer_right_shift)
    addi x22, x0, 32
    vloxei32.v v22, (x18), v24 #(v_ls_indexed)
    addi x22, x0, 20
    vsrl.vi v20, v20, 2, v0.t #(v_ia_single_width_shift)
    addi x12, x10, 1389
    vloxei32.v v13, (x19), v24, v0.t #(v_ls_indexed)
    addi x31, x28, 633
    vsub.vv v4, v30, v10, v0.t #(v_ia_single_width_integer_add_sub)
    addi x22, x0, 24
    vwmaccus.vx v8, x9, v13, v0.t #(v_ia_widening_integer_multiply_add)
    addi x22, x0, -120
    vmv.v.x v2, x9 #(v_ia_integer_move)
    addi x16, x12, -23
    vor.vv v4, v10, v3, v0.t #(v_ia_bitwise_logical)
    addi x22, x0, 64
    vrem.vv v20, v22, v10 #(v_ia_integer_divide)
    addi x5, x13, -1154
    vwmacc.vx v4, x5, v14, v0.t #(v_ia_widening_integer_multiply_add)
    addi x10, x29, 945
    vnmsac.vx v5, x6, v10, v0.t #(v_ia_single_width_integer_multiply_add)
    addi x22, x0, -32
    vrem.vv v19, v31, v18, v0.t #(v_ia_integer_divide)
    addi x22, x0, 24
    vmacc.vv v5, v26, v22, v0.t #(v_ia_single_width_integer_multiply_add)
    addi x9, x27, 796
    vnmsac.vv v22, v15, v4 #(v_ia_single_width_integer_multiply_add)
    addi x22, x0, -52
    vwmulu.vv v14, v12, v9, v0.t #(v_ia_widening_integer_multiply)
    addi x31, x12, 674
    vle16ff.v v5, (x19) #(v_ls_unit_stride)
    addi x25, x13, 1767
    vsra.vv v17, v16, v29 #(v_ia_single_width_shift)
    addi x27, x29, -458
    vle32.v v2, (x20) #(v_ls_unit_stride)
    addi x14, x0, -596
    vwmaccus.vx v14, x15, v25, v0.t #(v_ia_widening_integer_multiply_add)
    addi x22, x0, 40
    vwmul.vx v20, v15, x12 #(v_ia_widening_integer_multiply)
    addi x22, x0, 16
    vadd.vi v8, v30, 7 #(v_ia_single_width_integer_add_sub)
    addi x22, x0, 60
    vnsra.wx v14, v8, x23, v0.t #(v_ia_narrowing_integer_right_shift)
    addi x22, x0, -84
    vwsub.wv v10, v14, v17, v0.t #(v_ia_widening_integer_add_sub)
    addi x22, x0, -84
    vmulhsu.vx v7, v24, x25 #(v_ia_single_width_integer_multiply)
    addi x30, x17, -409
    vloxei16.v v12, (x18), v24, v0.t #(v_ls_indexed)
    addi x22, x0, 116
    vmsne.vi v7, v24, 9 #(v_ia_integer_compare)
    addi x22, x0, 32
    vmsltu.vv v8, v11, v1, v0.t #(v_ia_integer_compare)
    addi x22, x0, 104
    vwmulu.vv v18, v24, v27, v0.t #(v_ia_widening_integer_multiply)
    addi x22, x0, -68
    vmseq.vx v13, v25, x17 #(v_ia_integer_compare)
    addi x22, x0, 124
    vmulh.vv v18, v7, v16 #(v_ia_single_width_integer_multiply)
    addi x22, x0, 92
    vle8ff.v v15, (x18), v0.t #(v_ls_unit_stride)
    addi x22, x0, -116
    vwsub.vv v16, v8, v31 #(v_ia_widening_integer_add_sub)
    addi x0, x6, -758
    vmul.vv v9, v20, v21, v0.t #(v_ia_single_width_integer_multiply)
    addi x22, x0, -40
    vmsgtu.vi v13, v10, 0 #(v_ia_integer_compare)
    addi x30, x26, 2022
    vsuxei16.v v11, (x21), v24, v0.t #(v_ls_indexed)
    addi x22, x0, 0
    vluxei32.v v17, (x20), v24, v0.t #(v_ls_indexed)
    addi x13, x11, 730
    vdivu.vx v21, v15, x25 #(v_ia_integer_divide)
    addi x22, x0, -124
    vmv.v.x v12, x29 #(v_ia_integer_move)
    addi x10, x25, 155
    vwsubu.wx v6, v0, x0, v0.t #(v_ia_widening_integer_add_sub)
    addi x22, x0, 8
    vmax.vv v3, v0, v12 #(v_ia_integer_min_max)
    addi x22, x0, -68
    vnsra.wi v22, v8, 10, v0.t #(v_ia_narrowing_integer_right_shift)
    addi x27, x13, -897
    vwsubu.wx v22, v28, x9 #(v_ia_widening_integer_add_sub)
    addi x17, x23, -1922
    vwaddu.wx v4, v26, x12, v0.t #(v_ia_widening_integer_add_sub)
    addi x22, x0, 36
    vloxei32.v v10, (x19), v24, v0.t #(v_ls_indexed)
    addi x22, x0, 116
    vadd.vi v9, v7, 9 #(v_ia_single_width_integer_add_sub)
    addi x13, x14, 395
    vwsub.vv v16, v20, v27 #(v_ia_widening_integer_add_sub)
    addi x10, x28, 1148
    vsll.vi v18, v13, 17 #(v_ia_single_width_shift)
    addi x22, x0, -40
    vmsbc.vxm v9, v13, x23, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x31, x29, 1829
    vmv.v.v v13, v4 #(v_ia_integer_move)
    addi x22, x0, -100
    vnsra.wi v15, v30, 5, v0.t #(v_ia_narrowing_integer_right_shift)
    addi x30, x10, -1059
    vmulh.vx v9, v16, x25 #(v_ia_single_width_integer_multiply)
    addi x16, x30, 1155
    vmv.v.v v20, v24 #(v_ia_integer_move)
    addi x16, x28, 2008
    vmsbc.vv v21, v17, v19 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x22, x0, -84
    vsoxei16.v v23, (x21), v24 #(v_ls_indexed)
    addi x17, x28, -1208
    vzext.vf2 v23, v18, v0.t #(v_ia_integer_extension)
    addi x27, x29, -924
    vwsub.wv v2, v14, v10, v0.t #(v_ia_widening_integer_add_sub)
    addi x0, x28, -698
    vrem.vx v18, v6, x6 #(v_ia_integer_divide)
    addi x13, x17, 1530
    vmsltu.vx v5, v16, x16 #(v_ia_integer_compare)
    addi x22, x0, 40
    vwmul.vx v4, v8, x24 #(v_ia_widening_integer_multiply)
    addi x29, x29, 1914
    vwadd.wx v8, v6, x12 #(v_ia_widening_integer_add_sub)
    addi x27, x31, 1823
    vle16ff.v v19, (x19) #(v_ls_unit_stride)
    addi x22, x0, -80
    vwadd.vx v6, v19, x10 #(v_ia_widening_integer_add_sub)
    addi x11, x16, 125
    vadd.vv v5, v18, v0, v0.t #(v_ia_single_width_integer_add_sub)
    addi x22, x0, -52
    vmv.v.i v7, -9 #(v_ia_integer_move)
    addi x10, x17, 1389
    vmadd.vv v14, v3, v10, v0.t #(v_ia_single_width_integer_multiply_add)
    addi x23, x17, 1129
    vnmsub.vx v15, x6, v7, v0.t #(v_ia_single_width_integer_multiply_add)
    addi x22, x0, -120
    vwaddu.wv v20, v16, v17 #(v_ia_widening_integer_add_sub)
    addi x24, x13, 1051
    vsoxei8.v v3, (x21), v24 #(v_ls_indexed)
    addi x22, x0, 120
    vsra.vv v19, v3, v25, v0.t #(v_ia_single_width_shift)
    addi x22, x0, 52
    vle16ff.v v1, (x19), v0.t #(v_ls_unit_stride)
    addi x22, x0, -104
    vmacc.vv v9, v11, v21 #(v_ia_single_width_integer_multiply_add)
    addi x16, x13, -1687
    vmulhu.vv v11, v6, v0, v0.t #(v_ia_single_width_integer_multiply)
    addi x22, x0, 52
    vse8.v v1, (x21), v0.t #(v_ls_unit_stride)
    addi x22, x0, -128
    vmsgtu.vi v11, v27, -3, v0.t #(v_ia_integer_compare)
    addi x22, x0, 16
    vwaddu.wv v16, v2, v25, v0.t #(v_ia_widening_integer_add_sub)
    addi x22, x0, 60
    vadc.vxm v12, v11, x31, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x12, x27, 454
    vnmsac.vx v17, x11, v9, v0.t #(v_ia_single_width_integer_multiply_add)
    addi x9, x29, 994
    vwmulu.vx v10, v2, x29 #(v_ia_widening_integer_multiply)
    addi x25, x9, 576
    vwsubu.vv v2, v19, v10, v0.t #(v_ia_widening_integer_add_sub)
    addi x0, x25, 1935
    vwmulsu.vx v18, v24, x25 #(v_ia_widening_integer_multiply)
    addi x27, x31, 566
    vsbc.vxm v1, v24, x28, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x22, x0, -88
    vmacc.vx v20, x12, v6 #(v_ia_single_width_integer_multiply_add)
    addi x9, x24, -607
    vsra.vv v16, v2, v28, v0.t #(v_ia_single_width_shift)
    addi x22, x0, 4
    vmsbc.vxm v2, v10, x13, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x16, x6, -524
    vrem.vx v23, v29, x26 #(v_ia_integer_divide)
    addi x29, x10, 578
    vmulhu.vx v3, v17, x5 #(v_ia_single_width_integer_multiply)
    addi x22, x0, -84
    vloxei8.v v13, (x20), v24, v0.t #(v_ls_indexed)
    addi x0, x31, 769
    vmulhu.vx v14, v27, x24, v0.t #(v_ia_single_width_integer_multiply)
    addi x22, x0, 112
    vlse32.v v13, (x20), x22, v0.t #(v_ls_strided)
    addi x22, x0, 64
    vnmsub.vx v15, x0, v25, v0.t #(v_ia_single_width_integer_multiply_add)
    addi x22, x0, -24
    vle16.v v18, (x19) #(v_ls_unit_stride)
    addi x22, x0, 52
    vsse8.v v16, (x21), x22 #(v_ls_strided)
    addi x22, x0, -44
    vmadc.vim v8, v7, -9, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x22, x0, 52
    vremu.vx v3, v6, x23 #(v_ia_integer_divide)
    addi x22, x0, -24
    vmadd.vx v12, x0, v26 #(v_ia_single_width_integer_multiply_add)
    addi x9, x15, 1400
    vmsbc.vvm v3, v8, v20, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x26, x0, 580
    vminu.vv v7, v14, v25 #(v_ia_integer_min_max)
    addi x12, x6, -1596
    vmadc.vim v19, v7, 13, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x22, x0, 84
    vnsrl.wv v22, v28, v12, v0.t #(v_ia_narrowing_integer_right_shift)
    addi x13, x12, 623
    vmsne.vv v4, v2, v24 #(v_ia_integer_compare)
    addi x22, x0, -76
    vsuxei8.v v22, (x21), v24, v0.t #(v_ls_indexed)
    addi x22, x0, -96
    vsuxei16.v v21, (x21), v24 #(v_ls_indexed)
    addi x22, x0, -56
    vmulhsu.vv v23, v22, v19, v0.t #(v_ia_single_width_integer_multiply)
    addi x14, x11, -1437
    vwmulsu.vv v8, v28, v30 #(v_ia_widening_integer_multiply)
    addi x22, x0, -128
    vrsub.vi v14, v24, 10, v0.t #(v_ia_single_width_integer_add_sub)
    addi x22, x0, 100
    vmsltu.vx v10, v26, x16 #(v_ia_integer_compare)
    addi x22, x0, -28
    vadc.vxm v22, v21, x16, v0 #(v_ia_integer_add_w_carry-sub_w_borrow)
    addi x29, x15, 47
    vsuxei32.v v17, (x21), v24, v0.t #(v_ls_indexed)
    addi x5, x27, -655
    vdiv.vv v8, v25, v23, v0.t #(v_ia_integer_divide)
    addi x7, x15, -101
    vwmaccu.vx v22, x9, v5, v0.t #(v_ia_widening_integer_multiply_add)
