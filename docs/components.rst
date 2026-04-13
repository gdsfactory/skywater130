Cells
=====

Fixed (GDS-backed) cells available in the PDK, grouped by function.

Digital standard cells (sky130_fd_sc_hd)
----------------------------------------

High-density digital standard-cell library.  Cells are grouped by
logical function.  The trailing ``_N`` in each name encodes the
drive strength.

Inverters
^^^^^^^^^

.. currentmodule:: sky130.components

.. autosummary::
   :toctree: _autosummary/

   sky130_fd_sc_hd__einvn_0
   sky130_fd_sc_hd__einvn_1
   sky130_fd_sc_hd__einvn_2
   sky130_fd_sc_hd__einvn_4
   sky130_fd_sc_hd__einvn_8
   sky130_fd_sc_hd__einvp_1
   sky130_fd_sc_hd__einvp_2
   sky130_fd_sc_hd__einvp_4
   sky130_fd_sc_hd__einvp_8
   sky130_fd_sc_hd__inv_1
   sky130_fd_sc_hd__inv_12
   sky130_fd_sc_hd__inv_16
   sky130_fd_sc_hd__inv_2
   sky130_fd_sc_hd__inv_4
   sky130_fd_sc_hd__inv_6
   sky130_fd_sc_hd__inv_8

Buffers
^^^^^^^

.. currentmodule:: sky130.components

.. autosummary::
   :toctree: _autosummary/

   sky130_fd_sc_hd__buf_1
   sky130_fd_sc_hd__buf_12
   sky130_fd_sc_hd__buf_16
   sky130_fd_sc_hd__buf_2
   sky130_fd_sc_hd__buf_4
   sky130_fd_sc_hd__buf_6
   sky130_fd_sc_hd__buf_8
   sky130_fd_sc_hd__bufbuf_16
   sky130_fd_sc_hd__bufbuf_8
   sky130_fd_sc_hd__bufinv_16
   sky130_fd_sc_hd__bufinv_8
   sky130_fd_sc_hd__ebufn_1
   sky130_fd_sc_hd__ebufn_2
   sky130_fd_sc_hd__ebufn_4
   sky130_fd_sc_hd__ebufn_8

Clock
^^^^^

.. currentmodule:: sky130.components

.. autosummary::
   :toctree: _autosummary/

   sky130_fd_sc_hd__clkbuf_1
   sky130_fd_sc_hd__clkbuf_16
   sky130_fd_sc_hd__clkbuf_2
   sky130_fd_sc_hd__clkbuf_4
   sky130_fd_sc_hd__clkbuf_8
   sky130_fd_sc_hd__clkdlybuf4s15_1
   sky130_fd_sc_hd__clkdlybuf4s15_2
   sky130_fd_sc_hd__clkdlybuf4s18_1
   sky130_fd_sc_hd__clkdlybuf4s18_2
   sky130_fd_sc_hd__clkdlybuf4s25_1
   sky130_fd_sc_hd__clkdlybuf4s25_2
   sky130_fd_sc_hd__clkdlybuf4s50_1
   sky130_fd_sc_hd__clkdlybuf4s50_2
   sky130_fd_sc_hd__clkinv_1
   sky130_fd_sc_hd__clkinv_16
   sky130_fd_sc_hd__clkinv_2
   sky130_fd_sc_hd__clkinv_4
   sky130_fd_sc_hd__clkinv_8
   sky130_fd_sc_hd__clkinvlp_2
   sky130_fd_sc_hd__clkinvlp_4

AND / NAND
^^^^^^^^^^

.. currentmodule:: sky130.components

.. autosummary::
   :toctree: _autosummary/

   sky130_fd_sc_hd__and2_0
   sky130_fd_sc_hd__and2_1
   sky130_fd_sc_hd__and2_2
   sky130_fd_sc_hd__and2_4
   sky130_fd_sc_hd__and2b_1
   sky130_fd_sc_hd__and2b_2
   sky130_fd_sc_hd__and2b_4
   sky130_fd_sc_hd__and3_1
   sky130_fd_sc_hd__and3_2
   sky130_fd_sc_hd__and3_4
   sky130_fd_sc_hd__and3b_1
   sky130_fd_sc_hd__and3b_2
   sky130_fd_sc_hd__and3b_4
   sky130_fd_sc_hd__and4_1
   sky130_fd_sc_hd__and4_2
   sky130_fd_sc_hd__and4_4
   sky130_fd_sc_hd__and4b_1
   sky130_fd_sc_hd__and4b_2
   sky130_fd_sc_hd__and4b_4
   sky130_fd_sc_hd__and4bb_1
   sky130_fd_sc_hd__and4bb_2
   sky130_fd_sc_hd__and4bb_4
   sky130_fd_sc_hd__nand2_1
   sky130_fd_sc_hd__nand2_2
   sky130_fd_sc_hd__nand2_4
   sky130_fd_sc_hd__nand2_8
   sky130_fd_sc_hd__nand2b_1
   sky130_fd_sc_hd__nand2b_2
   sky130_fd_sc_hd__nand2b_4
   sky130_fd_sc_hd__nand3_1
   sky130_fd_sc_hd__nand3_2
   sky130_fd_sc_hd__nand3_4
   sky130_fd_sc_hd__nand3b_1
   sky130_fd_sc_hd__nand3b_2
   sky130_fd_sc_hd__nand3b_4
   sky130_fd_sc_hd__nand4_1
   sky130_fd_sc_hd__nand4_2
   sky130_fd_sc_hd__nand4_4
   sky130_fd_sc_hd__nand4b_1
   sky130_fd_sc_hd__nand4b_2
   sky130_fd_sc_hd__nand4b_4
   sky130_fd_sc_hd__nand4bb_1
   sky130_fd_sc_hd__nand4bb_2
   sky130_fd_sc_hd__nand4bb_4

OR / NOR
^^^^^^^^

.. currentmodule:: sky130.components

.. autosummary::
   :toctree: _autosummary/

   sky130_fd_sc_hd__nor2_1
   sky130_fd_sc_hd__nor2_2
   sky130_fd_sc_hd__nor2_4
   sky130_fd_sc_hd__nor2_8
   sky130_fd_sc_hd__nor2b_1
   sky130_fd_sc_hd__nor2b_2
   sky130_fd_sc_hd__nor2b_4
   sky130_fd_sc_hd__nor3_1
   sky130_fd_sc_hd__nor3_2
   sky130_fd_sc_hd__nor3_4
   sky130_fd_sc_hd__nor3b_1
   sky130_fd_sc_hd__nor3b_2
   sky130_fd_sc_hd__nor3b_4
   sky130_fd_sc_hd__nor4_1
   sky130_fd_sc_hd__nor4_2
   sky130_fd_sc_hd__nor4_4
   sky130_fd_sc_hd__nor4b_1
   sky130_fd_sc_hd__nor4b_2
   sky130_fd_sc_hd__nor4b_4
   sky130_fd_sc_hd__nor4bb_1
   sky130_fd_sc_hd__nor4bb_2
   sky130_fd_sc_hd__nor4bb_4
   sky130_fd_sc_hd__or2_0
   sky130_fd_sc_hd__or2_1
   sky130_fd_sc_hd__or2_2
   sky130_fd_sc_hd__or2_4
   sky130_fd_sc_hd__or2b_1
   sky130_fd_sc_hd__or2b_2
   sky130_fd_sc_hd__or2b_4
   sky130_fd_sc_hd__or3_1
   sky130_fd_sc_hd__or3_2
   sky130_fd_sc_hd__or3_4
   sky130_fd_sc_hd__or3b_1
   sky130_fd_sc_hd__or3b_2
   sky130_fd_sc_hd__or3b_4
   sky130_fd_sc_hd__or4_1
   sky130_fd_sc_hd__or4_2
   sky130_fd_sc_hd__or4_4
   sky130_fd_sc_hd__or4b_1
   sky130_fd_sc_hd__or4b_2
   sky130_fd_sc_hd__or4b_4
   sky130_fd_sc_hd__or4bb_1
   sky130_fd_sc_hd__or4bb_2
   sky130_fd_sc_hd__or4bb_4

XOR / XNOR
^^^^^^^^^^

.. currentmodule:: sky130.components

.. autosummary::
   :toctree: _autosummary/

   sky130_fd_sc_hd__xnor2_1
   sky130_fd_sc_hd__xnor2_2
   sky130_fd_sc_hd__xnor2_4
   sky130_fd_sc_hd__xnor3_1
   sky130_fd_sc_hd__xnor3_2
   sky130_fd_sc_hd__xnor3_4
   sky130_fd_sc_hd__xor2_1
   sky130_fd_sc_hd__xor2_2
   sky130_fd_sc_hd__xor2_4
   sky130_fd_sc_hd__xor3_1
   sky130_fd_sc_hd__xor3_2
   sky130_fd_sc_hd__xor3_4

Multiplexers
^^^^^^^^^^^^

.. currentmodule:: sky130.components

.. autosummary::
   :toctree: _autosummary/

   sky130_fd_sc_hd__mux2_1
   sky130_fd_sc_hd__mux2_2
   sky130_fd_sc_hd__mux2_4
   sky130_fd_sc_hd__mux2_8
   sky130_fd_sc_hd__mux2i_1
   sky130_fd_sc_hd__mux2i_2
   sky130_fd_sc_hd__mux2i_4
   sky130_fd_sc_hd__mux4_1
   sky130_fd_sc_hd__mux4_2
   sky130_fd_sc_hd__mux4_4

Arithmetic (adders / majority)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. currentmodule:: sky130.components

.. autosummary::
   :toctree: _autosummary/

   sky130_fd_sc_hd__fa_1
   sky130_fd_sc_hd__fa_2
   sky130_fd_sc_hd__fa_4
   sky130_fd_sc_hd__fah_1
   sky130_fd_sc_hd__fahcin_1
   sky130_fd_sc_hd__fahcon_1
   sky130_fd_sc_hd__ha_1
   sky130_fd_sc_hd__ha_2
   sky130_fd_sc_hd__ha_4
   sky130_fd_sc_hd__maj3_1
   sky130_fd_sc_hd__maj3_2
   sky130_fd_sc_hd__maj3_4

Complex AOI / OAI gates
^^^^^^^^^^^^^^^^^^^^^^^

.. currentmodule:: sky130.components

.. autosummary::
   :toctree: _autosummary/

   sky130_fd_sc_hd__a2111o_1
   sky130_fd_sc_hd__a2111o_2
   sky130_fd_sc_hd__a2111o_4
   sky130_fd_sc_hd__a2111oi_0
   sky130_fd_sc_hd__a2111oi_1
   sky130_fd_sc_hd__a2111oi_2
   sky130_fd_sc_hd__a2111oi_4
   sky130_fd_sc_hd__a211o_1
   sky130_fd_sc_hd__a211o_2
   sky130_fd_sc_hd__a211o_4
   sky130_fd_sc_hd__a211oi_1
   sky130_fd_sc_hd__a211oi_2
   sky130_fd_sc_hd__a211oi_4
   sky130_fd_sc_hd__a21bo_1
   sky130_fd_sc_hd__a21bo_2
   sky130_fd_sc_hd__a21bo_4
   sky130_fd_sc_hd__a21boi_0
   sky130_fd_sc_hd__a21boi_1
   sky130_fd_sc_hd__a21boi_2
   sky130_fd_sc_hd__a21boi_4
   sky130_fd_sc_hd__a21o_1
   sky130_fd_sc_hd__a21o_2
   sky130_fd_sc_hd__a21o_4
   sky130_fd_sc_hd__a21oi_1
   sky130_fd_sc_hd__a21oi_2
   sky130_fd_sc_hd__a21oi_4
   sky130_fd_sc_hd__a221o_1
   sky130_fd_sc_hd__a221o_2
   sky130_fd_sc_hd__a221o_4
   sky130_fd_sc_hd__a221oi_1
   sky130_fd_sc_hd__a221oi_2
   sky130_fd_sc_hd__a221oi_4
   sky130_fd_sc_hd__a222oi_1
   sky130_fd_sc_hd__a22o_1
   sky130_fd_sc_hd__a22o_2
   sky130_fd_sc_hd__a22o_4
   sky130_fd_sc_hd__a22oi_1
   sky130_fd_sc_hd__a22oi_2
   sky130_fd_sc_hd__a22oi_4
   sky130_fd_sc_hd__a2bb2o_1
   sky130_fd_sc_hd__a2bb2o_2
   sky130_fd_sc_hd__a2bb2o_4
   sky130_fd_sc_hd__a2bb2oi_1
   sky130_fd_sc_hd__a2bb2oi_2
   sky130_fd_sc_hd__a2bb2oi_4
   sky130_fd_sc_hd__a311o_1
   sky130_fd_sc_hd__a311o_2
   sky130_fd_sc_hd__a311o_4
   sky130_fd_sc_hd__a311oi_1
   sky130_fd_sc_hd__a311oi_2
   sky130_fd_sc_hd__a311oi_4
   sky130_fd_sc_hd__a31o_1
   sky130_fd_sc_hd__a31o_2
   sky130_fd_sc_hd__a31o_4
   sky130_fd_sc_hd__a31oi_1
   sky130_fd_sc_hd__a31oi_2
   sky130_fd_sc_hd__a31oi_4
   sky130_fd_sc_hd__a32o_1
   sky130_fd_sc_hd__a32o_2
   sky130_fd_sc_hd__a32o_4
   sky130_fd_sc_hd__a32oi_1
   sky130_fd_sc_hd__a32oi_2
   sky130_fd_sc_hd__a32oi_4
   sky130_fd_sc_hd__a41o_1
   sky130_fd_sc_hd__a41o_2
   sky130_fd_sc_hd__a41o_4
   sky130_fd_sc_hd__a41oi_1
   sky130_fd_sc_hd__a41oi_2
   sky130_fd_sc_hd__a41oi_4
   sky130_fd_sc_hd__o2111a_1
   sky130_fd_sc_hd__o2111a_2
   sky130_fd_sc_hd__o2111a_4
   sky130_fd_sc_hd__o2111ai_1
   sky130_fd_sc_hd__o2111ai_2
   sky130_fd_sc_hd__o2111ai_4
   sky130_fd_sc_hd__o211a_1
   sky130_fd_sc_hd__o211a_2
   sky130_fd_sc_hd__o211a_4
   sky130_fd_sc_hd__o211ai_1
   sky130_fd_sc_hd__o211ai_2
   sky130_fd_sc_hd__o211ai_4
   sky130_fd_sc_hd__o21a_1
   sky130_fd_sc_hd__o21a_2
   sky130_fd_sc_hd__o21a_4
   sky130_fd_sc_hd__o21ai_0
   sky130_fd_sc_hd__o21ai_1
   sky130_fd_sc_hd__o21ai_2
   sky130_fd_sc_hd__o21ai_4
   sky130_fd_sc_hd__o21ba_1
   sky130_fd_sc_hd__o21ba_2
   sky130_fd_sc_hd__o21ba_4
   sky130_fd_sc_hd__o21bai_1
   sky130_fd_sc_hd__o21bai_2
   sky130_fd_sc_hd__o21bai_4
   sky130_fd_sc_hd__o221a_1
   sky130_fd_sc_hd__o221a_2
   sky130_fd_sc_hd__o221a_4
   sky130_fd_sc_hd__o221ai_1
   sky130_fd_sc_hd__o221ai_2
   sky130_fd_sc_hd__o221ai_4
   sky130_fd_sc_hd__o22a_1
   sky130_fd_sc_hd__o22a_2
   sky130_fd_sc_hd__o22a_4
   sky130_fd_sc_hd__o22ai_1
   sky130_fd_sc_hd__o22ai_2
   sky130_fd_sc_hd__o22ai_4
   sky130_fd_sc_hd__o2bb2a_1
   sky130_fd_sc_hd__o2bb2a_2
   sky130_fd_sc_hd__o2bb2a_4
   sky130_fd_sc_hd__o2bb2ai_1
   sky130_fd_sc_hd__o2bb2ai_2
   sky130_fd_sc_hd__o2bb2ai_4
   sky130_fd_sc_hd__o311a_1
   sky130_fd_sc_hd__o311a_2
   sky130_fd_sc_hd__o311a_4
   sky130_fd_sc_hd__o311ai_0
   sky130_fd_sc_hd__o311ai_1
   sky130_fd_sc_hd__o311ai_2
   sky130_fd_sc_hd__o311ai_4
   sky130_fd_sc_hd__o31a_1
   sky130_fd_sc_hd__o31a_2
   sky130_fd_sc_hd__o31a_4
   sky130_fd_sc_hd__o31ai_1
   sky130_fd_sc_hd__o31ai_2
   sky130_fd_sc_hd__o31ai_4
   sky130_fd_sc_hd__o32a_1
   sky130_fd_sc_hd__o32a_2
   sky130_fd_sc_hd__o32a_4
   sky130_fd_sc_hd__o32ai_1
   sky130_fd_sc_hd__o32ai_2
   sky130_fd_sc_hd__o32ai_4
   sky130_fd_sc_hd__o41a_1
   sky130_fd_sc_hd__o41a_2
   sky130_fd_sc_hd__o41a_4
   sky130_fd_sc_hd__o41ai_1
   sky130_fd_sc_hd__o41ai_2
   sky130_fd_sc_hd__o41ai_4

Flip-flops
^^^^^^^^^^

.. currentmodule:: sky130.components

.. autosummary::
   :toctree: _autosummary/

   sky130_fd_sc_hd__dfbbn_1
   sky130_fd_sc_hd__dfbbn_2
   sky130_fd_sc_hd__dfbbp_1
   sky130_fd_sc_hd__dfrbp_1
   sky130_fd_sc_hd__dfrbp_2
   sky130_fd_sc_hd__dfrtn_1
   sky130_fd_sc_hd__dfrtp_1
   sky130_fd_sc_hd__dfrtp_2
   sky130_fd_sc_hd__dfrtp_4
   sky130_fd_sc_hd__dfsbp_1
   sky130_fd_sc_hd__dfsbp_2
   sky130_fd_sc_hd__dfstp_1
   sky130_fd_sc_hd__dfstp_2
   sky130_fd_sc_hd__dfstp_4
   sky130_fd_sc_hd__dfxbp_1
   sky130_fd_sc_hd__dfxbp_2
   sky130_fd_sc_hd__dfxtp_1
   sky130_fd_sc_hd__dfxtp_2
   sky130_fd_sc_hd__dfxtp_4
   sky130_fd_sc_hd__edfxbp_1
   sky130_fd_sc_hd__edfxtp_1
   sky130_fd_sc_hd__sdfbbn_1
   sky130_fd_sc_hd__sdfbbn_2
   sky130_fd_sc_hd__sdfbbp_1
   sky130_fd_sc_hd__sdfrbp_1
   sky130_fd_sc_hd__sdfrbp_2
   sky130_fd_sc_hd__sdfrtn_1
   sky130_fd_sc_hd__sdfrtp_1
   sky130_fd_sc_hd__sdfrtp_2
   sky130_fd_sc_hd__sdfrtp_4
   sky130_fd_sc_hd__sdfsbp_1
   sky130_fd_sc_hd__sdfsbp_2
   sky130_fd_sc_hd__sdfstp_1
   sky130_fd_sc_hd__sdfstp_2
   sky130_fd_sc_hd__sdfstp_4
   sky130_fd_sc_hd__sdfxbp_1
   sky130_fd_sc_hd__sdfxbp_2
   sky130_fd_sc_hd__sdfxtp_1
   sky130_fd_sc_hd__sdfxtp_2
   sky130_fd_sc_hd__sdfxtp_4
   sky130_fd_sc_hd__sedfxbp_1
   sky130_fd_sc_hd__sedfxbp_2
   sky130_fd_sc_hd__sedfxtp_1
   sky130_fd_sc_hd__sedfxtp_2
   sky130_fd_sc_hd__sedfxtp_4

Latches & delay cells
^^^^^^^^^^^^^^^^^^^^^

.. currentmodule:: sky130.components

.. autosummary::
   :toctree: _autosummary/

   sky130_fd_sc_hd__dlclkp_1
   sky130_fd_sc_hd__dlclkp_2
   sky130_fd_sc_hd__dlclkp_4
   sky130_fd_sc_hd__dlrbn_1
   sky130_fd_sc_hd__dlrbn_2
   sky130_fd_sc_hd__dlrbp_1
   sky130_fd_sc_hd__dlrbp_2
   sky130_fd_sc_hd__dlrtn_1
   sky130_fd_sc_hd__dlrtn_2
   sky130_fd_sc_hd__dlrtn_4
   sky130_fd_sc_hd__dlrtp_1
   sky130_fd_sc_hd__dlrtp_2
   sky130_fd_sc_hd__dlrtp_4
   sky130_fd_sc_hd__dlxbn_1
   sky130_fd_sc_hd__dlxbn_2
   sky130_fd_sc_hd__dlxbp_1
   sky130_fd_sc_hd__dlxtn_1
   sky130_fd_sc_hd__dlxtn_2
   sky130_fd_sc_hd__dlxtn_4
   sky130_fd_sc_hd__dlxtp_1
   sky130_fd_sc_hd__dlygate4sd1_1
   sky130_fd_sc_hd__dlygate4sd2_1
   sky130_fd_sc_hd__dlygate4sd3_1
   sky130_fd_sc_hd__dlymetal6s2s_1
   sky130_fd_sc_hd__dlymetal6s4s_1
   sky130_fd_sc_hd__dlymetal6s6s_1
   sky130_fd_sc_hd__sdlclkp_1
   sky130_fd_sc_hd__sdlclkp_2
   sky130_fd_sc_hd__sdlclkp_4

Low-power
^^^^^^^^^

.. currentmodule:: sky130.components

.. autosummary::
   :toctree: _autosummary/

   sky130_fd_sc_hd__lpflow_bleeder_1
   sky130_fd_sc_hd__lpflow_clkbufkapwr_1
   sky130_fd_sc_hd__lpflow_clkbufkapwr_16
   sky130_fd_sc_hd__lpflow_clkbufkapwr_2
   sky130_fd_sc_hd__lpflow_clkbufkapwr_4
   sky130_fd_sc_hd__lpflow_clkbufkapwr_8
   sky130_fd_sc_hd__lpflow_clkinvkapwr_1
   sky130_fd_sc_hd__lpflow_clkinvkapwr_16
   sky130_fd_sc_hd__lpflow_clkinvkapwr_2
   sky130_fd_sc_hd__lpflow_clkinvkapwr_4
   sky130_fd_sc_hd__lpflow_clkinvkapwr_8
   sky130_fd_sc_hd__lpflow_decapkapwr_12
   sky130_fd_sc_hd__lpflow_decapkapwr_3
   sky130_fd_sc_hd__lpflow_decapkapwr_4
   sky130_fd_sc_hd__lpflow_decapkapwr_6
   sky130_fd_sc_hd__lpflow_decapkapwr_8
   sky130_fd_sc_hd__lpflow_inputiso0n_1
   sky130_fd_sc_hd__lpflow_inputiso0p_1
   sky130_fd_sc_hd__lpflow_inputiso1n_1
   sky130_fd_sc_hd__lpflow_inputiso1p_1
   sky130_fd_sc_hd__lpflow_inputisolatch_1
   sky130_fd_sc_hd__lpflow_isobufsrc_1
   sky130_fd_sc_hd__lpflow_isobufsrc_16
   sky130_fd_sc_hd__lpflow_isobufsrc_2
   sky130_fd_sc_hd__lpflow_isobufsrc_4
   sky130_fd_sc_hd__lpflow_isobufsrc_8
   sky130_fd_sc_hd__lpflow_isobufsrckapwr_16
   sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_1
   sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_2
   sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_4
   sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_4
   sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_1
   sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_2
   sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_4

Physical / fill / tap
^^^^^^^^^^^^^^^^^^^^^

.. currentmodule:: sky130.components

.. autosummary::
   :toctree: _autosummary/

   sky130_fd_sc_hd__conb_1
   sky130_fd_sc_hd__decap_12
   sky130_fd_sc_hd__decap_3
   sky130_fd_sc_hd__decap_4
   sky130_fd_sc_hd__decap_6
   sky130_fd_sc_hd__decap_8
   sky130_fd_sc_hd__diode_2
   sky130_fd_sc_hd__fill_1
   sky130_fd_sc_hd__fill_2
   sky130_fd_sc_hd__fill_4
   sky130_fd_sc_hd__fill_8
   sky130_fd_sc_hd__macro_sparecell
   sky130_fd_sc_hd__probe_p_8
   sky130_fd_sc_hd__probec_p_8
   sky130_fd_sc_hd__tap_1
   sky130_fd_sc_hd__tap_2
   sky130_fd_sc_hd__tapvgnd2_1
   sky130_fd_sc_hd__tapvgnd_1
   sky130_fd_sc_hd__tapvpwrvgnd_1

Analog / RF primitives (sky130_fd_pr)
-------------------------------------

Analog primitive devices: MOSFETs, BJTs, capacitors, ESD devices
and RF test structures.

Capacitors (MIM / VPP)
^^^^^^^^^^^^^^^^^^^^^^

.. currentmodule:: sky130.components

.. autosummary::
   :toctree: _autosummary/

   sky130_fd_pr__cap_vpp_02p4x04p6_m1m2_noshield
   sky130_fd_pr__cap_vpp_02p7x06p1_m1m2m3m4_shieldl1_fingercap
   sky130_fd_pr__cap_vpp_02p7x11p1_m1m2m3m4_shieldl1_fingercap
   sky130_fd_pr__cap_vpp_02p7x21p1_m1m2m3m4_shieldl1_fingercap
   sky130_fd_pr__cap_vpp_02p7x41p1_m1m2m3m4_shieldl1_fingercap
   sky130_fd_pr__cap_vpp_02p9x06p1_m1m2m3m4_shieldl1_fingercap2
   sky130_fd_pr__cap_vpp_03p9x03p9_m1m2_shieldl1_floatm3
   sky130_fd_pr__cap_vpp_04p4x04p6_l1m1m2_noshield
   sky130_fd_pr__cap_vpp_04p4x04p6_l1m1m2_noshield_o2subcell
   sky130_fd_pr__cap_vpp_04p4x04p6_l1m1m2_shieldpo_floatm3
   sky130_fd_pr__cap_vpp_04p4x04p6_m1m2_noshield
   sky130_fd_pr__cap_vpp_04p4x04p6_m1m2_noshield_o2
   sky130_fd_pr__cap_vpp_04p4x04p6_m1m2_shieldl1
   sky130_fd_pr__cap_vpp_04p4x04p6_m1m2m3_shieldl1
   sky130_fd_pr__cap_vpp_04p4x04p6_m1m2m3_shieldl1m5_floatm4
   sky130_fd_pr__cap_vpp_04p4x04p6_m1m2m3_shieldl1m5_floatm4_top
   sky130_fd_pr__cap_vpp_05p9x05p9_m1m2m3m4_shieldl1_wafflecap
   sky130_fd_pr__cap_vpp_06p8x06p1_l1m1m2m3_shieldpom4
   sky130_fd_pr__cap_vpp_06p8x06p1_l1m1m2m3_shieldpom4_top
   sky130_fd_pr__cap_vpp_06p8x06p1_m1m2m3_shieldl1m4
   sky130_fd_pr__cap_vpp_06p8x06p1_m1m2m3_shieldl1m4_top
   sky130_fd_pr__cap_vpp_08p6x07p8_l1m1m2_noshield
   sky130_fd_pr__cap_vpp_08p6x07p8_l1m1m2_noshield_o2subcell
   sky130_fd_pr__cap_vpp_08p6x07p8_l1m1m2_shieldpo_floatm3
   sky130_fd_pr__cap_vpp_08p6x07p8_m1m2_noshield
   sky130_fd_pr__cap_vpp_08p6x07p8_m1m2_shieldl1
   sky130_fd_pr__cap_vpp_08p6x07p8_m1m2m3_shieldl1
   sky130_fd_pr__cap_vpp_08p6x07p8_m1m2m3_shieldl1m5_floatm4
   sky130_fd_pr__cap_vpp_08p6x07p8_m1m2m3_shieldl1m5_floatm4_top
   sky130_fd_pr__cap_vpp_11p3x11p3_m1m2m3m4_shieldl1_wafflecap
   sky130_fd_pr__cap_vpp_11p3x11p8_l1m1m2m3m4_shieldm5_nhv
   sky130_fd_pr__cap_vpp_11p3x11p8_l1m1m2m3m4_shieldm5_nhvtop
   sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2_noshield
   sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2_shieldpom3
   sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3_shieldm4
   sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3_shieldm4_top
   sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3_shieldpom4
   sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3_shieldpom4_top
   sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldm5
   sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldm5_top
   sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5
   sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_top
   sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_x
   sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_x6
   sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_x7
   sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_x8
   sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_x9
   sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_xtop
   sky130_fd_pr__cap_vpp_11p5x11p7_m1m2_noshield
   sky130_fd_pr__cap_vpp_11p5x11p7_m1m2_shieldl1
   sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3_shieldl1
   sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3_shieldl1m5_floatm4
   sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3_shieldl1m5_floatm4_top
   sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3m4_shieldl1m5
   sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3m4_shieldl1m5_top
   sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3m4_shieldm5
   sky130_fd_pr__cap_vpp_11p5x11p7_m1m4_noshield
   sky130_fd_pr__cap_vpp_11p5x11p7_pol1m1m2m3m4m5_noshield
   sky130_fd_pr__cap_vpp_11p5x23p1_pol1m1m2m3m4m5_noshield
   sky130_fd_pr__cap_vpp_22p5x11p7_pol1m1m2m3m4m5_noshield
   sky130_fd_pr__cap_vpp_22p5x23p1_pol1m1m2m3m4m5_noshield
   sky130_fd_pr__cap_vpp_33p6x11p7_pol1m1m2m3m4m5_noshield
   sky130_fd_pr__cap_vpp_33p6x23p1_pol1m1m2m3m4m5_noshield
   sky130_fd_pr__cap_vpp_44p7x11p7_pol1m1m2m3m4m5_noshield
   sky130_fd_pr__cap_vpp_44p7x23p1_pol1m1m2m3m4m5_noshield
   sky130_fd_pr__cap_vpp_55p8x11p7_pol1m1m2m3m4m5_noshield
   sky130_fd_pr__cap_vpp_55p8x11p7_pol1m1m2m3m4m5_noshield_m5pullin
   sky130_fd_pr__cap_vpp_55p8x23p1_pol1m1m2m3m4m5_noshield
   sky130_fd_pr__cap_vpp_55p8x23p1_pol1m1m2m3m4m5_noshield_m5pullin
   sky130_fd_pr__cap_vpp_55p8x23p1_pol1m1m2m3m4m5_noshield_test

RF NFETs
^^^^^^^^

.. currentmodule:: sky130.components

.. autosummary::
   :toctree: _autosummary/

   sky130_fd_pr__rf_nfet_01v8_aM02W1p65L0p15
   sky130_fd_pr__rf_nfet_01v8_aM02W1p65L0p18
   sky130_fd_pr__rf_nfet_01v8_aM02W1p65L0p25
   sky130_fd_pr__rf_nfet_01v8_aM02W3p00L0p15
   sky130_fd_pr__rf_nfet_01v8_aM02W3p00L0p18
   sky130_fd_pr__rf_nfet_01v8_aM02W3p00L0p25
   sky130_fd_pr__rf_nfet_01v8_aM02W5p00L0p15
   sky130_fd_pr__rf_nfet_01v8_aM02W5p00L0p18
   sky130_fd_pr__rf_nfet_01v8_aM02W5p00L0p25
   sky130_fd_pr__rf_nfet_01v8_aM04W1p65L0p15
   sky130_fd_pr__rf_nfet_01v8_aM04W1p65L0p18
   sky130_fd_pr__rf_nfet_01v8_aM04W1p65L0p25
   sky130_fd_pr__rf_nfet_01v8_aM04W3p00L0p15
   sky130_fd_pr__rf_nfet_01v8_aM04W3p00L0p18
   sky130_fd_pr__rf_nfet_01v8_aM04W3p00L0p25
   sky130_fd_pr__rf_nfet_01v8_aM04W5p00L0p15
   sky130_fd_pr__rf_nfet_01v8_aM04W5p00L0p18
   sky130_fd_pr__rf_nfet_01v8_aM04W5p00L0p25
   sky130_fd_pr__rf_nfet_01v8_bM02W1p65L0p15
   sky130_fd_pr__rf_nfet_01v8_bM02W1p65L0p18
   sky130_fd_pr__rf_nfet_01v8_bM02W1p65L0p25
   sky130_fd_pr__rf_nfet_01v8_bM02W3p00L0p15
   sky130_fd_pr__rf_nfet_01v8_bM02W3p00L0p18
   sky130_fd_pr__rf_nfet_01v8_bM02W3p00L0p25
   sky130_fd_pr__rf_nfet_01v8_bM02W5p00L0p15
   sky130_fd_pr__rf_nfet_01v8_bM02W5p00L0p18
   sky130_fd_pr__rf_nfet_01v8_bM02W5p00L0p25
   sky130_fd_pr__rf_nfet_01v8_bM04W1p65L0p15
   sky130_fd_pr__rf_nfet_01v8_bM04W1p65L0p18
   sky130_fd_pr__rf_nfet_01v8_bM04W1p65L0p25
   sky130_fd_pr__rf_nfet_01v8_bM04W3p00L0p15
   sky130_fd_pr__rf_nfet_01v8_bM04W3p00L0p18
   sky130_fd_pr__rf_nfet_01v8_bM04W3p00L0p25
   sky130_fd_pr__rf_nfet_01v8_bM04W5p00L0p15
   sky130_fd_pr__rf_nfet_01v8_bM04W5p00L0p18
   sky130_fd_pr__rf_nfet_01v8_bM04W5p00L0p25
   sky130_fd_pr__rf_nfet_01v8_hcM04W3p00L0p15
   sky130_fd_pr__rf_nfet_01v8_hcM04W5p00L0p15
   sky130_fd_pr__rf_nfet_01v8_lvt_aF02W0p42L0p15
   sky130_fd_pr__rf_nfet_01v8_lvt_aF02W0p84L0p15
   sky130_fd_pr__rf_nfet_01v8_lvt_aF02W1p65L0p15
   sky130_fd_pr__rf_nfet_01v8_lvt_aF02W3p00L0p15
   sky130_fd_pr__rf_nfet_01v8_lvt_aF04W0p42L0p15
   sky130_fd_pr__rf_nfet_01v8_lvt_aF04W0p84L0p15
   sky130_fd_pr__rf_nfet_01v8_lvt_aF04W1p65L0p15
   sky130_fd_pr__rf_nfet_01v8_lvt_aF04W3p00L0p15
   sky130_fd_pr__rf_nfet_01v8_lvt_aF06W0p42L0p15
   sky130_fd_pr__rf_nfet_01v8_lvt_aF06W0p84L0p15
   sky130_fd_pr__rf_nfet_01v8_lvt_aF06W1p65L0p15
   sky130_fd_pr__rf_nfet_01v8_lvt_aF06W3p00L0p15
   sky130_fd_pr__rf_nfet_01v8_lvt_aF08W0p42L0p15
   sky130_fd_pr__rf_nfet_01v8_lvt_aF08W0p84L0p15
   sky130_fd_pr__rf_nfet_01v8_lvt_aF08W1p65L0p15
   sky130_fd_pr__rf_nfet_01v8_lvt_aF08W3p00L0p15
   sky130_fd_pr__rf_nfet_01v8_lvt_aM02W1p65L0p15
   sky130_fd_pr__rf_nfet_01v8_lvt_aM02W1p65L0p18
   sky130_fd_pr__rf_nfet_01v8_lvt_aM02W1p65L0p25
   sky130_fd_pr__rf_nfet_01v8_lvt_aM02W3p00L0p15
   sky130_fd_pr__rf_nfet_01v8_lvt_aM02W3p00L0p18
   sky130_fd_pr__rf_nfet_01v8_lvt_aM02W3p00L0p25
   sky130_fd_pr__rf_nfet_01v8_lvt_aM02W5p00L0p15
   sky130_fd_pr__rf_nfet_01v8_lvt_aM02W5p00L0p18
   sky130_fd_pr__rf_nfet_01v8_lvt_aM02W5p00L0p25
   sky130_fd_pr__rf_nfet_01v8_lvt_aM04W1p65L0p15
   sky130_fd_pr__rf_nfet_01v8_lvt_aM04W1p65L0p18
   sky130_fd_pr__rf_nfet_01v8_lvt_aM04W1p65L0p25
   sky130_fd_pr__rf_nfet_01v8_lvt_aM04W3p00L0p15
   sky130_fd_pr__rf_nfet_01v8_lvt_aM04W3p00L0p18
   sky130_fd_pr__rf_nfet_01v8_lvt_aM04W3p00L0p25
   sky130_fd_pr__rf_nfet_01v8_lvt_aM04W5p00L0p15
   sky130_fd_pr__rf_nfet_01v8_lvt_aM04W5p00L0p18
   sky130_fd_pr__rf_nfet_01v8_lvt_aM04W5p00L0p25
   sky130_fd_pr__rf_nfet_01v8_lvt_bM02W1p65L0p15
   sky130_fd_pr__rf_nfet_01v8_lvt_bM02W1p65L0p18
   sky130_fd_pr__rf_nfet_01v8_lvt_bM02W1p65L0p25
   sky130_fd_pr__rf_nfet_01v8_lvt_bM02W3p00L0p15
   sky130_fd_pr__rf_nfet_01v8_lvt_bM02W3p00L0p18
   sky130_fd_pr__rf_nfet_01v8_lvt_bM02W3p00L0p25
   sky130_fd_pr__rf_nfet_01v8_lvt_bM02W5p00L0p15
   sky130_fd_pr__rf_nfet_01v8_lvt_bM02W5p00L0p18
   sky130_fd_pr__rf_nfet_01v8_lvt_bM02W5p00L0p25
   sky130_fd_pr__rf_nfet_01v8_lvt_bM04W1p65L0p15
   sky130_fd_pr__rf_nfet_01v8_lvt_bM04W1p65L0p18
   sky130_fd_pr__rf_nfet_01v8_lvt_bM04W1p65L0p25
   sky130_fd_pr__rf_nfet_01v8_lvt_bM04W3p00L0p15
   sky130_fd_pr__rf_nfet_01v8_lvt_bM04W3p00L0p18
   sky130_fd_pr__rf_nfet_01v8_lvt_bM04W3p00L0p25
   sky130_fd_pr__rf_nfet_01v8_lvt_bM04W5p00L0p15
   sky130_fd_pr__rf_nfet_01v8_lvt_bM04W5p00L0p18
   sky130_fd_pr__rf_nfet_01v8_lvt_bM04W5p00L0p25
   sky130_fd_pr__rf_nfet_01v8_lvt_cM02W1p65L0p15
   sky130_fd_pr__rf_nfet_01v8_lvt_cM02W1p65L0p18
   sky130_fd_pr__rf_nfet_01v8_lvt_cM02W1p65L0p25
   sky130_fd_pr__rf_nfet_01v8_lvt_cM02W3p00L0p15
   sky130_fd_pr__rf_nfet_01v8_lvt_cM02W3p00L0p18
   sky130_fd_pr__rf_nfet_01v8_lvt_cM02W3p00L0p25
   sky130_fd_pr__rf_nfet_01v8_lvt_cM02W5p00L0p15
   sky130_fd_pr__rf_nfet_01v8_lvt_cM02W5p00L0p18
   sky130_fd_pr__rf_nfet_01v8_lvt_cM02W5p00L0p25
   sky130_fd_pr__rf_nfet_01v8_lvt_cM04W1p65L0p15
   sky130_fd_pr__rf_nfet_01v8_lvt_cM04W1p65L0p18
   sky130_fd_pr__rf_nfet_01v8_lvt_cM04W1p65L0p25
   sky130_fd_pr__rf_nfet_01v8_lvt_cM04W3p00L0p15
   sky130_fd_pr__rf_nfet_01v8_lvt_cM04W3p00L0p18
   sky130_fd_pr__rf_nfet_01v8_lvt_cM04W3p00L0p25
   sky130_fd_pr__rf_nfet_01v8_lvt_cM04W5p00L0p15
   sky130_fd_pr__rf_nfet_01v8_lvt_cM04W5p00L0p18
   sky130_fd_pr__rf_nfet_01v8_lvt_cM04W5p00L0p25
   sky130_fd_pr__rf_nfet_01v8_mcM04W3p00L0p15
   sky130_fd_pr__rf_nfet_01v8_mcM04W5p00L0p15
   sky130_fd_pr__rf_nfet_20v0_aup
   sky130_fd_pr__rf_nfet_20v0_noptap_iso
   sky130_fd_pr__rf_nfet_20v0_nvt_aup
   sky130_fd_pr__rf_nfet_20v0_nvt_noptap_iso
   sky130_fd_pr__rf_nfet_20v0_nvt_withptap
   sky130_fd_pr__rf_nfet_20v0_nvt_withptap_iso
   sky130_fd_pr__rf_nfet_20v0_withptap
   sky130_fd_pr__rf_nfet_20v0_withptap_iso
   sky130_fd_pr__rf_nfet_20v0_zvt_withptap
   sky130_fd_pr__rf_nfet_g5v0d10v5_aM04W3p00L0p50
   sky130_fd_pr__rf_nfet_g5v0d10v5_aM04W5p00L0p50
   sky130_fd_pr__rf_nfet_g5v0d10v5_aM04W7p00L0p50
   sky130_fd_pr__rf_nfet_g5v0d10v5_aM10W3p00L0p50
   sky130_fd_pr__rf_nfet_g5v0d10v5_aM10W5p00L0p50
   sky130_fd_pr__rf_nfet_g5v0d10v5_aM10W7p00L0p50
   sky130_fd_pr__rf_nfet_g5v0d10v5_bM02W3p00L0p50
   sky130_fd_pr__rf_nfet_g5v0d10v5_bM02W5p00L0p50
   sky130_fd_pr__rf_nfet_g5v0d10v5_bM04W3p00L0p50
   sky130_fd_pr__rf_nfet_g5v0d10v5_bM04W5p00L0p50
   sky130_fd_pr__rf_nfet_g5v0d10v5_bM04W7p00L0p50
   sky130_fd_pr__rf_nfet_g5v0d10v5_bM10W3p00L0p50
   sky130_fd_pr__rf_nfet_g5v0d10v5_bM10W5p00L0p50
   sky130_fd_pr__rf_nfet_g5v0d10v5_bM10W7p00L0p50

RF PFETs
^^^^^^^^

.. currentmodule:: sky130.components

.. autosummary::
   :toctree: _autosummary/

   sky130_fd_pr__rf_pfet_01v8_aF02W0p84L0p15
   sky130_fd_pr__rf_pfet_01v8_aF02W1p68L0p15
   sky130_fd_pr__rf_pfet_01v8_aF02W2p00L0p15
   sky130_fd_pr__rf_pfet_01v8_aF02W3p00L0p15
   sky130_fd_pr__rf_pfet_01v8_aF02W5p00L0p15
   sky130_fd_pr__rf_pfet_01v8_aF04W0p84L0p15
   sky130_fd_pr__rf_pfet_01v8_aF04W1p68L0p15
   sky130_fd_pr__rf_pfet_01v8_aF04W2p00L0p15
   sky130_fd_pr__rf_pfet_01v8_aF04W3p00L0p15
   sky130_fd_pr__rf_pfet_01v8_aF04W5p00L0p15
   sky130_fd_pr__rf_pfet_01v8_aF06W0p84L0p15
   sky130_fd_pr__rf_pfet_01v8_aF06W1p68L0p15
   sky130_fd_pr__rf_pfet_01v8_aF06W2p00L0p15
   sky130_fd_pr__rf_pfet_01v8_aF06W3p00L0p15
   sky130_fd_pr__rf_pfet_01v8_aF08W0p84L0p15
   sky130_fd_pr__rf_pfet_01v8_aF08W1p68L0p15
   sky130_fd_pr__rf_pfet_01v8_aM02W1p65L0p15
   sky130_fd_pr__rf_pfet_01v8_aM02W1p65L0p18
   sky130_fd_pr__rf_pfet_01v8_aM02W1p65L0p25
   sky130_fd_pr__rf_pfet_01v8_aM02W3p00L0p15
   sky130_fd_pr__rf_pfet_01v8_aM02W3p00L0p18
   sky130_fd_pr__rf_pfet_01v8_aM02W3p00L0p25
   sky130_fd_pr__rf_pfet_01v8_aM02W5p00L0p15
   sky130_fd_pr__rf_pfet_01v8_aM02W5p00L0p18
   sky130_fd_pr__rf_pfet_01v8_aM02W5p00L0p25
   sky130_fd_pr__rf_pfet_01v8_aM04W1p65L0p15
   sky130_fd_pr__rf_pfet_01v8_aM04W1p65L0p18
   sky130_fd_pr__rf_pfet_01v8_aM04W1p65L0p25
   sky130_fd_pr__rf_pfet_01v8_aM04W3p00L0p15
   sky130_fd_pr__rf_pfet_01v8_aM04W3p00L0p18
   sky130_fd_pr__rf_pfet_01v8_aM04W3p00L0p25
   sky130_fd_pr__rf_pfet_01v8_aM04W5p00L0p15
   sky130_fd_pr__rf_pfet_01v8_aM04W5p00L0p18
   sky130_fd_pr__rf_pfet_01v8_aM04W5p00L0p25
   sky130_fd_pr__rf_pfet_01v8_bM02W1p65L0p15
   sky130_fd_pr__rf_pfet_01v8_bM02W1p65L0p18
   sky130_fd_pr__rf_pfet_01v8_bM02W1p65L0p25
   sky130_fd_pr__rf_pfet_01v8_bM02W3p00L0p15
   sky130_fd_pr__rf_pfet_01v8_bM02W3p00L0p18
   sky130_fd_pr__rf_pfet_01v8_bM02W3p00L0p25
   sky130_fd_pr__rf_pfet_01v8_bM02W5p00L0p15
   sky130_fd_pr__rf_pfet_01v8_bM02W5p00L0p18
   sky130_fd_pr__rf_pfet_01v8_bM02W5p00L0p25
   sky130_fd_pr__rf_pfet_01v8_bM04W1p65L0p15
   sky130_fd_pr__rf_pfet_01v8_bM04W1p65L0p18
   sky130_fd_pr__rf_pfet_01v8_bM04W1p65L0p25
   sky130_fd_pr__rf_pfet_01v8_bM04W3p00L0p15
   sky130_fd_pr__rf_pfet_01v8_bM04W3p00L0p18
   sky130_fd_pr__rf_pfet_01v8_bM04W3p00L0p25
   sky130_fd_pr__rf_pfet_01v8_bM04W5p00L0p15
   sky130_fd_pr__rf_pfet_01v8_bM04W5p00L0p18
   sky130_fd_pr__rf_pfet_01v8_bM04W5p00L0p25
   sky130_fd_pr__rf_pfet_01v8_hcM04W3p00L0p15
   sky130_fd_pr__rf_pfet_01v8_hcM04W5p00L0p15
   sky130_fd_pr__rf_pfet_01v8_lvt_aM02W3p00L0p35
   sky130_fd_pr__rf_pfet_01v8_lvt_aM02W3p00L0p50
   sky130_fd_pr__rf_pfet_01v8_lvt_aM02W5p00L0p35
   sky130_fd_pr__rf_pfet_01v8_lvt_aM02W5p00L0p50
   sky130_fd_pr__rf_pfet_01v8_lvt_aM04W3p00L0p35
   sky130_fd_pr__rf_pfet_01v8_lvt_aM04W3p00L0p50
   sky130_fd_pr__rf_pfet_01v8_lvt_aM04W5p00L0p35
   sky130_fd_pr__rf_pfet_01v8_lvt_aM04W5p00L0p50
   sky130_fd_pr__rf_pfet_01v8_mcM04W3p00L0p15
   sky130_fd_pr__rf_pfet_01v8_mcM04W5p00L0p15
   sky130_fd_pr__rf_pfet_01v8_mvt_aF02W0p84L0p15
   sky130_fd_pr__rf_pfet_20v0_withptap

RF NPN BJTs
^^^^^^^^^^^

.. currentmodule:: sky130.components

.. autosummary::
   :toctree: _autosummary/

   sky130_fd_pr__rf_npn_05v5_W1p00L1p00
   sky130_fd_pr__rf_npn_05v5_W1p00L2p00
   sky130_fd_pr__rf_npn_05v5_W1p00L4p00
   sky130_fd_pr__rf_npn_05v5_W1p00L8p00
   sky130_fd_pr__rf_npn_05v5_W2p00L2p00
   sky130_fd_pr__rf_npn_05v5_W2p00L4p00
   sky130_fd_pr__rf_npn_05v5_W2p00L8p00
   sky130_fd_pr__rf_npn_05v5_W5p00L5p00
   sky130_fd_pr__rf_npn_11v0_W1p00L1p00

RF PNP BJTs
^^^^^^^^^^^

.. currentmodule:: sky130.components

.. autosummary::
   :toctree: _autosummary/

   sky130_fd_pr__rf_pnp_05v5_W0p68L0p68
   sky130_fd_pr__rf_pnp_05v5_W3p40L3p40

ESD devices
^^^^^^^^^^^

.. currentmodule:: sky130.components

.. autosummary::
   :toctree: _autosummary/

   sky130_fd_pr__esd_rf_nfet_20v0_hbm_21vW60p00
   sky130_fd_pr__esd_rf_nfet_20v0_hbm_32vW60p00
   sky130_fd_pr__esd_rf_nfet_20v0_iec_21vW60p00
   sky130_fd_pr__esd_rf_nfet_20v0_iec_32vW60p00

RF test structures
^^^^^^^^^^^^^^^^^^

.. currentmodule:: sky130.components

.. autosummary::
   :toctree: _autosummary/

   sky130_fd_pr__rf_test_coil1
   sky130_fd_pr__rf_test_coil2
   sky130_fd_pr__rf_test_coil3

RF aura test structures
^^^^^^^^^^^^^^^^^^^^^^^

.. currentmodule:: sky130.components

.. autosummary::
   :toctree: _autosummary/

   sky130_fd_pr__rf_aura_blocking
   sky130_fd_pr__rf_aura_drc_flag_check
   sky130_fd_pr__rf_aura_lvs_drc
