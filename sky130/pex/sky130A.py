#
# This creates a technology definition example for sky130A:
# https://skywater-pdk.readthedocs.io/en/main/_images/metal_stack.svg
#

import sys
import warnings
from pathlib import Path

try:
    from gf_pex.techfile import (
        CapacitanceInfo,
        ComputedLayerInfo,
        ComputedLayerKind,
        ConformalDielectricLayer,
        Contact,
        ContactResistance,
        DiffusionLayer,
        FieldOxideLayer,
        GDSPair,
        LayerInfo,
        LayerPurpose,
        LayerResistance,
        MetalLayer,
        NWellLayer,
        OverlapCapacitance,
        ProcessParasiticsInfo,
        ProcessStackInfo,
        ResistanceInfo,
        SideOverlapCapacitance,
        SidewallCapacitance,
        SimpleDielectricLayer,
        StackLayerInfo,
        StackLayerType,
        SubstrateCapacitance,
        SubstrateLayer,
        Techfile,
        ViaResistance,
    )
except ImportError:
    warnings.warn(
        "gf_pex is not installed. Cannot build techfile from gf180mcuD. "
        "Install it with: pip install gf-pex",
        stacklevel=2,
    )
    sys.exit(1)

DNWELL = LayerPurpose.PURPOSE_DNWELL
NWELL = LayerPurpose.PURPOSE_NWELL
DIFF = LayerPurpose.PURPOSE_DIFF
N_P_TAP = LayerPurpose.PURPOSE_NTAP_OR_PTAP
NTAP = LayerPurpose.PURPOSE_NTAP
PTAP = LayerPurpose.PURPOSE_PTAP
PIMP = LayerPurpose.PURPOSE_P_IMPLANT
NIMP = LayerPurpose.PURPOSE_N_IMPLANT
CONT = LayerPurpose.PURPOSE_CONTACT
METAL = LayerPurpose.PURPOSE_METAL
VIA = LayerPurpose.PURPOSE_VIA
MIM = LayerPurpose.PURPOSE_MIM_CAP

KREG = ComputedLayerKind.KIND_REGULAR
KCAP = ComputedLayerKind.KIND_DEVICE_CAPACITOR
KPIN = ComputedLayerKind.KIND_PIN
KLBL = ComputedLayerKind.KIND_LABEL

# TODO: Replace the current tech.layers, tech.lvs_computed_layers and tech.process_layer_stack with existing API on gdsfactory

def build_layers(tech: Techfile) -> None:
    #                    purpose  name      drw_gds       pin_gds       label_gds     description
    tech.layers.append(LayerInfo(purpose=DNWELL,  name="dnwell", drw_gds_pair=GDSPair(layer=64, datatype=18),                                                                    description="Deep N-well"))
    tech.layers.append(LayerInfo(purpose=NWELL,   name="nwell",  drw_gds_pair=GDSPair(layer=64, datatype=20), pin_gds_pair=GDSPair(layer=64, datatype=16), label_gds_pair=GDSPair(layer=64, datatype=5),  description="N-well region"))
    tech.layers.append(LayerInfo(purpose=DIFF,    name="diff",   drw_gds_pair=GDSPair(layer=65, datatype=20), pin_gds_pair=GDSPair(layer=65, datatype=16), label_gds_pair=GDSPair(layer=65, datatype=5),  description="Active (diffusion) area"))
    tech.layers.append(LayerInfo(purpose=N_P_TAP, name="tap",    drw_gds_pair=GDSPair(layer=65, datatype=44),                                                                    description="Active (diffusion) area (type equal to the well/substrate underneath) (i.e., N+ and P+)"))
    tech.layers.append(LayerInfo(purpose=PIMP,    name="psdm",   drw_gds_pair=GDSPair(layer=94, datatype=20),                                                                    description="P+ source/drain implant"))
    tech.layers.append(LayerInfo(purpose=NIMP,    name="nsdm",   drw_gds_pair=GDSPair(layer=93, datatype=44),                                                                    description="N+ source/drain implant"))
    tech.layers.append(LayerInfo(purpose=METAL,   name="poly",   drw_gds_pair=GDSPair(layer=66, datatype=20), pin_gds_pair=GDSPair(layer=66, datatype=16), label_gds_pair=GDSPair(layer=66, datatype=5),  description="Polysilicon"))
    tech.layers.append(LayerInfo(purpose=CONT,    name="licon1", drw_gds_pair=GDSPair(layer=66, datatype=44),                                                                    description="Contact to local interconnect"))
    tech.layers.append(LayerInfo(purpose=METAL,   name="li1",    drw_gds_pair=GDSPair(layer=67, datatype=20), pin_gds_pair=GDSPair(layer=67, datatype=16), label_gds_pair=GDSPair(layer=67, datatype=5),  description="Local interconnect"))
    tech.layers.append(LayerInfo(purpose=VIA,     name="mcon",   drw_gds_pair=GDSPair(layer=67, datatype=44),                                                                    description="Contact from local interconnect to met1"))
    tech.layers.append(LayerInfo(purpose=METAL,   name="met1",   drw_gds_pair=GDSPair(layer=68, datatype=20), pin_gds_pair=GDSPair(layer=68, datatype=16), label_gds_pair=GDSPair(layer=68, datatype=5),  description="Metal 1"))
    tech.layers.append(LayerInfo(purpose=VIA,     name="via",    drw_gds_pair=GDSPair(layer=68, datatype=44),                                                                    description="Contact from met1 to met2"))
    tech.layers.append(LayerInfo(purpose=METAL,   name="met2",   drw_gds_pair=GDSPair(layer=69, datatype=20), pin_gds_pair=GDSPair(layer=69, datatype=16), label_gds_pair=GDSPair(layer=69, datatype=5),  description="Metal 2"))
    tech.layers.append(LayerInfo(purpose=VIA,     name="via2",   drw_gds_pair=GDSPair(layer=69, datatype=44),                                                                    description="Contact from met2 to met3"))
    tech.layers.append(LayerInfo(purpose=METAL,   name="met3",   drw_gds_pair=GDSPair(layer=70, datatype=20), pin_gds_pair=GDSPair(layer=70, datatype=16), label_gds_pair=GDSPair(layer=70, datatype=5),  description="Metal 3"))
    tech.layers.append(LayerInfo(purpose=VIA,     name="via3",   drw_gds_pair=GDSPair(layer=70, datatype=44),                                                                    description="Contact from cap above met3 to met4"))
    tech.layers.append(LayerInfo(purpose=MIM,     name="capm",   drw_gds_pair=GDSPair(layer=89, datatype=44),                                                                    description="MiM capacitor plate over metal 3"))
    tech.layers.append(LayerInfo(purpose=METAL,   name="met4",   drw_gds_pair=GDSPair(layer=71, datatype=20), pin_gds_pair=GDSPair(layer=71, datatype=16), label_gds_pair=GDSPair(layer=71, datatype=5),  description="Metal 4"))
    tech.layers.append(LayerInfo(purpose=MIM,     name="capm2",  drw_gds_pair=GDSPair(layer=97, datatype=44),                                                                    description="MiM capacitor plate over metal 4"))
    tech.layers.append(LayerInfo(purpose=VIA,     name="via4",   drw_gds_pair=GDSPair(layer=71, datatype=44),                                                                    description="Contact from met4 to met5 (no MiM cap)"))
    tech.layers.append(LayerInfo(purpose=METAL,   name="met5",   drw_gds_pair=GDSPair(layer=72, datatype=20), pin_gds_pair=GDSPair(layer=72, datatype=16), label_gds_pair=GDSPair(layer=72, datatype=5),  description="Metal 5"))


def build_lvs_computed_layers(tech: Techfile) -> None:
    #                                       purpose kind   lvs_name          lvs_gds                            orig_layer    description
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KREG, layer_info=LayerInfo(purpose=DNWELL, name="dnwell",        description="Deep NWell",                                                          drw_gds_pair=GDSPair(layer=64, datatype=18)),  original_layer_name="dnwell",     ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KREG, layer_info=LayerInfo(purpose=NWELL,  name="nwell",         description="NWell",                                                               drw_gds_pair=GDSPair(layer=64, datatype=20)),  original_layer_name="nwell",      ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KREG, layer_info=LayerInfo(purpose=NIMP,   name="nsd",           description="borrow from nsdm",                                                    drw_gds_pair=GDSPair(layer=93, datatype=44)),  original_layer_name="nsdm",       ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KREG, layer_info=LayerInfo(purpose=PIMP,   name="psd",           description="borrow from psdm",                                                    drw_gds_pair=GDSPair(layer=94, datatype=20)),  original_layer_name="psdm",       ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KREG, layer_info=LayerInfo(purpose=NTAP,   name="ntap_conn",     description="Separate ntap, original tap is 65,44, we need seperate ntap/ptap",    drw_gds_pair=GDSPair(layer=65, datatype=144)), original_layer_name="tap",        ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KREG, layer_info=LayerInfo(purpose=PTAP,   name="ptap_conn",     description="Separate ptap, original tap is 65,44, we need seperate ntap/ptap",    drw_gds_pair=GDSPair(layer=65, datatype=244)), original_layer_name="tap",        ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KREG, layer_info=LayerInfo(purpose=METAL,  name="poly_con",      description="Computed layer for poly",                                             drw_gds_pair=GDSPair(layer=66, datatype=20)),  original_layer_name="poly",       ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KREG, layer_info=LayerInfo(purpose=METAL,  name="li_con",        description="Computed layer for li1",                                              drw_gds_pair=GDSPair(layer=67, datatype=20)),  original_layer_name="li1",        ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KREG, layer_info=LayerInfo(purpose=METAL,  name="met1_con",      description="Computed layer for met1",                                             drw_gds_pair=GDSPair(layer=68, datatype=20)),  original_layer_name="met1",       ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KREG, layer_info=LayerInfo(purpose=METAL,  name="met2_con",      description="Computed layer for met2",                                             drw_gds_pair=GDSPair(layer=69, datatype=20)),  original_layer_name="met2",       ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KREG, layer_info=LayerInfo(purpose=METAL,  name="met3_ncap",     description="Computed layer for met3 (no cap)",                                    drw_gds_pair=GDSPair(layer=70, datatype=20)),  original_layer_name="met3",       ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KREG, layer_info=LayerInfo(purpose=METAL,  name="met4_ncap",     description="Computed layer for met4 (no cap)",                                    drw_gds_pair=GDSPair(layer=71, datatype=20)),  original_layer_name="met4",       ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KREG, layer_info=LayerInfo(purpose=METAL,  name="met5_con",      description="Computed layer for met5",                                             drw_gds_pair=GDSPair(layer=72, datatype=20)),  original_layer_name="met5",       ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KREG, layer_info=LayerInfo(purpose=CONT,   name="licon_nsd_con",  description="Computed layer for contact from nsdm to li1",                        drw_gds_pair=GDSPair(layer=66, datatype=4401)), original_layer_name="licon1",   ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KREG, layer_info=LayerInfo(purpose=CONT,   name="licon_psd_con",  description="Computed layer for contact from psdm to li1",                        drw_gds_pair=GDSPair(layer=66, datatype=4402)), original_layer_name="licon1",   ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KREG, layer_info=LayerInfo(purpose=CONT,   name="licon_poly_con", description="Computed layer for contact from poly to li1",                        drw_gds_pair=GDSPair(layer=66, datatype=4403)), original_layer_name="licon1",   ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KREG, layer_info=LayerInfo(purpose=VIA,    name="mcon_con",      description="Computed layer for contact between li1 and met1",                     drw_gds_pair=GDSPair(layer=67, datatype=44)),  original_layer_name="mcon",       ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KREG, layer_info=LayerInfo(purpose=VIA,    name="via1_con",      description="Computed layer for contact between met1 and met2",                    drw_gds_pair=GDSPair(layer=68, datatype=44)),  original_layer_name="via",        ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KREG, layer_info=LayerInfo(purpose=VIA,    name="via2_con",      description="Computed layer for contact between met2 and met3",                    drw_gds_pair=GDSPair(layer=69, datatype=44)),  original_layer_name="via2",       ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KREG, layer_info=LayerInfo(purpose=VIA,    name="via3_ncap",     description="Computed layer for via3 (no MIM cap)",                                drw_gds_pair=GDSPair(layer=70, datatype=144)), original_layer_name="via3",       ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KREG, layer_info=LayerInfo(purpose=VIA,    name="via4_ncap",     description="Computed layer for via4 (no MIM cap)",                                drw_gds_pair=GDSPair(layer=71, datatype=144)), original_layer_name="via4",       ))

    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KCAP, layer_info=LayerInfo(purpose=VIA,    name="via3_cap",      description="Computed layer for via3 (with MIM cap)",                              drw_gds_pair=GDSPair(layer=70, datatype=244)), original_layer_name="via3",       ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KCAP, layer_info=LayerInfo(purpose=VIA,    name="via4_cap",      description="Computed layer for via4 (with MIM cap)",                              drw_gds_pair=GDSPair(layer=71, datatype=244)), original_layer_name="via4",       ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KCAP, layer_info=LayerInfo(purpose=METAL,  name="met3_cap",      description="metal3 part of MiM cap",                                              drw_gds_pair=GDSPair(layer=70, datatype=20)),  original_layer_name="met3",       ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KCAP, layer_info=LayerInfo(purpose=METAL,  name="met4_cap",      description="metal4 part of MiM cap",                                              drw_gds_pair=GDSPair(layer=71, datatype=20)),  original_layer_name="met4",       ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KCAP, layer_info=LayerInfo(purpose=MIM,    name="capm",          description="MiM cap above metal3",                                                drw_gds_pair=GDSPair(layer=89, datatype=44)),  original_layer_name="capm",       ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KCAP, layer_info=LayerInfo(purpose=MIM,    name="capm2",         description="MiM cap above metal4",                                                drw_gds_pair=GDSPair(layer=97, datatype=44)),  original_layer_name="capm2",      ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KCAP, layer_info=LayerInfo(purpose=METAL,  name="poly_vpp",      description="Computed layer for poly (MOM cap)",                                   drw_gds_pair=GDSPair(layer=66, datatype=20)),  original_layer_name="poly",       ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KCAP, layer_info=LayerInfo(purpose=METAL,  name="li_vpp",        description="Capacitor device metal (MOM cap)",                                    drw_gds_pair=GDSPair(layer=67, datatype=20)),  original_layer_name="li1",        ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KCAP, layer_info=LayerInfo(purpose=METAL,  name="met1_vpp",      description="Capacitor device metal (MOM cap)",                                    drw_gds_pair=GDSPair(layer=68, datatype=20)),  original_layer_name="met1",       ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KCAP, layer_info=LayerInfo(purpose=METAL,  name="met2_vpp",      description="Capacitor device metal (MOM cap)",                                    drw_gds_pair=GDSPair(layer=69, datatype=20)),  original_layer_name="met2",       ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KCAP, layer_info=LayerInfo(purpose=METAL,  name="met3_vpp",      description="Capacitor device metal (MOM cap)",                                    drw_gds_pair=GDSPair(layer=70, datatype=20)),  original_layer_name="met3",       ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KCAP, layer_info=LayerInfo(purpose=METAL,  name="met4_vpp",      description="Capacitor device metal (MOM cap)",                                    drw_gds_pair=GDSPair(layer=71, datatype=20)),  original_layer_name="met4",       ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KCAP, layer_info=LayerInfo(purpose=METAL,  name="met5_vpp",      description="Capacitor device metal (MOM cap)",                                    drw_gds_pair=GDSPair(layer=72, datatype=20)),  original_layer_name="met5",       ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KCAP, layer_info=LayerInfo(purpose=CONT,   name="licon_vpp",     description="Capacitor device contact (MOM cap)",                                  drw_gds_pair=GDSPair(layer=66, datatype=44)),  original_layer_name="licon1",     ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KCAP, layer_info=LayerInfo(purpose=VIA,    name="mcon_vpp",      description="Capacitor device contact (MOM cap)",                                  drw_gds_pair=GDSPair(layer=67, datatype=44)),  original_layer_name="mcon",       ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KCAP, layer_info=LayerInfo(purpose=VIA,    name="via1_vpp",      description="Capacitor device contact (MOM cap)",                                  drw_gds_pair=GDSPair(layer=68, datatype=44)),  original_layer_name="via",        ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KCAP, layer_info=LayerInfo(purpose=VIA,    name="via2_vpp",      description="Capacitor device contact (MOM cap)",                                  drw_gds_pair=GDSPair(layer=69, datatype=44)),  original_layer_name="via2",       ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KCAP, layer_info=LayerInfo(purpose=VIA,    name="via3_vpp",      description="Capacitor device contact (MOM cap)",                                  drw_gds_pair=GDSPair(layer=70, datatype=44)),  original_layer_name="via3",       ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KCAP, layer_info=LayerInfo(purpose=VIA,    name="via4_vpp",      description="Capacitor device contact (MOM cap)",                                  drw_gds_pair=GDSPair(layer=71, datatype=44)),  original_layer_name="via4",       ))

    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KPIN, layer_info=LayerInfo(purpose=METAL,  name="poly_pin_con",  description="Poly pin",                                                            drw_gds_pair=GDSPair(layer=66, datatype=16)),  original_layer_name="poly.pin",   ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KPIN, layer_info=LayerInfo(purpose=METAL,  name="li_pin_con",    description="li1 pin",                                                             drw_gds_pair=GDSPair(layer=67, datatype=16)),  original_layer_name="li1.pin",    ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KPIN, layer_info=LayerInfo(purpose=METAL,  name="met1_pin_con",  description="met1 pin",                                                            drw_gds_pair=GDSPair(layer=68, datatype=16)),  original_layer_name="met1.pin",   ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KPIN, layer_info=LayerInfo(purpose=METAL,  name="met2_pin_con",  description="met2 pin",                                                            drw_gds_pair=GDSPair(layer=69, datatype=16)),  original_layer_name="met2.pin",   ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KPIN, layer_info=LayerInfo(purpose=METAL,  name="met3_pin_con",  description="met3 pin",                                                            drw_gds_pair=GDSPair(layer=70, datatype=16)),  original_layer_name="met3.pin",   ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KPIN, layer_info=LayerInfo(purpose=METAL,  name="met4_pin_con",  description="met4 pin",                                                            drw_gds_pair=GDSPair(layer=71, datatype=16)),  original_layer_name="met4.pin",   ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KPIN, layer_info=LayerInfo(purpose=METAL,  name="met5_pin_con",  description="met5 pin",                                                            drw_gds_pair=GDSPair(layer=72, datatype=16)),  original_layer_name="met5.pin",   ))

    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KLBL, layer_info=LayerInfo(purpose=METAL,  name="poly_label",    description="Poly label",                                                          drw_gds_pair=GDSPair(layer=66, datatype=5)),   original_layer_name="poly.label", ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KLBL, layer_info=LayerInfo(purpose=METAL,  name="li_label",      description="li1 label",                                                           drw_gds_pair=GDSPair(layer=67, datatype=5)),   original_layer_name="li1.label",  ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KLBL, layer_info=LayerInfo(purpose=METAL,  name="met1_label",    description="met1 label",                                                          drw_gds_pair=GDSPair(layer=68, datatype=5)),   original_layer_name="met1.label", ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KLBL, layer_info=LayerInfo(purpose=METAL,  name="met2_label",    description="met2 label",                                                          drw_gds_pair=GDSPair(layer=69, datatype=5)),   original_layer_name="met2.label", ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KLBL, layer_info=LayerInfo(purpose=METAL,  name="met3_label",    description="met3 label",                                                          drw_gds_pair=GDSPair(layer=70, datatype=5)),   original_layer_name="met3.label", ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KLBL, layer_info=LayerInfo(purpose=METAL,  name="met4_label",    description="met4 label",                                                          drw_gds_pair=GDSPair(layer=71, datatype=5)),   original_layer_name="met4.label", ))
    tech.lvs_computed_layers.append(ComputedLayerInfo(kind=KLBL, layer_info=LayerInfo(purpose=METAL,  name="met5_label",    description="met5 label",                                                          drw_gds_pair=GDSPair(layer=72, datatype=5)),   original_layer_name="met5.label", ))


def build_process_stack_info(tech: Techfile) -> None:
    tech.process_stack = ProcessStackInfo()
    psi = tech.process_stack

    capm_thickness = 0.1
    capild_k = 4.52
    capild_thickness = 0.02

    # SUBSTRATE
    psi.layers.append(StackLayerInfo(name="subs", layer_type=StackLayerType.LAYER_TYPE_SUBSTRATE,
        substrate_layer=SubstrateLayer(height=0.1, thickness=0.33, reference="fox")))

    # NWELL / DIFF
    psi.layers.append(StackLayerInfo(name="nwell", layer_type=StackLayerType.LAYER_TYPE_NWELL,
        nwell_layer=NWellLayer(z=0.1, reference="fox", contact_above=Contact())))
    psi.layers.append(StackLayerInfo(name="nsd", layer_type=StackLayerType.LAYER_TYPE_DIFFUSION,
        diffusion_layer=DiffusionLayer(z=0.323, reference="fox",
            contact_above=Contact(name="licon_nsd_con", layer_below="nsdm", metal_above="li1", thickness=0.9361, width=0.17, spacing=0.17, border=0.0))))
    psi.layers.append(StackLayerInfo(name="psd", layer_type=StackLayerType.LAYER_TYPE_DIFFUSION,
        diffusion_layer=DiffusionLayer(z=0.323, reference="fox",
            contact_above=Contact(name="licon_psd_con", layer_below="psdm", metal_above="li1", thickness=0.9361, width=0.17, spacing=0.17, border=0.0))))

    # FOX
    psi.layers.append(StackLayerInfo(name="fox", layer_type=StackLayerType.LAYER_TYPE_FIELD_OXIDE,
        field_oxide_layer=FieldOxideLayer(dielectric_k=4.632)))

    # POLY
    psi.layers.append(StackLayerInfo(name="poly", layer_type=StackLayerType.LAYER_TYPE_METAL,
        metal_layer=MetalLayer(z=0.3262, thickness=0.18,
            contact_above=Contact(name="licon_poly_con", layer_below="poly", metal_above="li1", thickness=0.4299, width=0.17, spacing=0.17, border=0.0))))
    psi.layers.append(StackLayerInfo(name="iox", layer_type=StackLayerType.LAYER_TYPE_SIDEWALL_DIELECTRIC,
        sidewall_dielectric_layer=SidewallDielectricLayer(dielectric_k=0.39, height_above_metal=0.18, width_outside_sidewall=0.006, reference="poly")))
    psi.layers.append(StackLayerInfo(name="spnit", layer_type=StackLayerType.LAYER_TYPE_SIDEWALL_DIELECTRIC,
        sidewall_dielectric_layer=SidewallDielectricLayer(dielectric_k=7.5, height_above_metal=0.121, width_outside_sidewall=0.0431, reference="iox")))
    psi.layers.append(StackLayerInfo(name="psg", layer_type=StackLayerType.LAYER_TYPE_SIMPLE_DIELECTRIC,
        simple_dielectric_layer=SimpleDielectricLayer(dielectric_k=3.9, reference="fox")))

    # LI1
    psi.layers.append(StackLayerInfo(name="li1", layer_type=StackLayerType.LAYER_TYPE_METAL,
        metal_layer=MetalLayer(z=0.9361, thickness=0.1,
            contact_above=Contact(name="mcon_con", layer_below="li1", metal_above="met1", thickness=1.3761 - (0.9361 + 0.1), width=0.17, spacing=0.19, border=0.0))))
    psi.layers.append(StackLayerInfo(name="lint", layer_type=StackLayerType.LAYER_TYPE_CONFORMAL_DIELECTRIC,
        conformal_dielectric_layer=ConformalDielectricLayer(dielectric_k=7.3, thickness_over_metal=0.075, thickness_where_no_metal=0.075, thickness_sidewall=0.075, reference="li1")))
    psi.layers.append(StackLayerInfo(name="nild2", layer_type=StackLayerType.LAYER_TYPE_SIMPLE_DIELECTRIC,
        simple_dielectric_layer=SimpleDielectricLayer(dielectric_k=4.05, reference="lint")))

    # MET1
    psi.layers.append(StackLayerInfo(name="met1", layer_type=StackLayerType.LAYER_TYPE_METAL,
        metal_layer=MetalLayer(z=1.3761, thickness=0.36,
            contact_above=Contact(name="via1_con", layer_below="met1", metal_above="met2", thickness=0.27, width=0.15, spacing=0.17, border=0.055))))
    psi.layers.append(StackLayerInfo(name="nild3c", layer_type=StackLayerType.LAYER_TYPE_SIDEWALL_DIELECTRIC,
        sidewall_dielectric_layer=SidewallDielectricLayer(dielectric_k=3.5, height_above_metal=0.0, width_outside_sidewall=0.03, reference="met1")))
    psi.layers.append(StackLayerInfo(name="nild3", layer_type=StackLayerType.LAYER_TYPE_SIMPLE_DIELECTRIC,
        simple_dielectric_layer=SimpleDielectricLayer(dielectric_k=4.5, reference="nild2")))

    # MET2
    psi.layers.append(StackLayerInfo(name="met2", layer_type=StackLayerType.LAYER_TYPE_METAL,
        metal_layer=MetalLayer(z=2.0061, thickness=0.36,
            contact_above=Contact(name="via2_con", layer_below="met2", metal_above="met3", thickness=0.42, width=0.20, spacing=0.20, border=0.04))))
    psi.layers.append(StackLayerInfo(name="nild4c", layer_type=StackLayerType.LAYER_TYPE_SIDEWALL_DIELECTRIC,
        sidewall_dielectric_layer=SidewallDielectricLayer(dielectric_k=3.5, height_above_metal=0.0, width_outside_sidewall=0.03, reference="met2")))
    psi.layers.append(StackLayerInfo(name="nild4", layer_type=StackLayerType.LAYER_TYPE_SIMPLE_DIELECTRIC,
        simple_dielectric_layer=SimpleDielectricLayer(dielectric_k=4.2, reference="nild3")))

    # MET3 (two variants: ncap and cap)
    psi.layers.append(StackLayerInfo(name="met3_ncap", layer_type=StackLayerType.LAYER_TYPE_METAL,
        metal_layer=MetalLayer(z=2.7861, thickness=0.845,
            contact_above=Contact(name="via3_ncap", layer_below="met3", metal_above="met4", thickness=0.39, width=0.20, spacing=0.20, border=0.06))))
    psi.layers.append(StackLayerInfo(name="met3_cap", layer_type=StackLayerType.LAYER_TYPE_METAL,
        metal_layer=MetalLayer(z=2.7861, thickness=0.845)))
    psi.layers.append(StackLayerInfo(name="capild", layer_type=StackLayerType.LAYER_TYPE_CONFORMAL_DIELECTRIC,
        conformal_dielectric_layer=ConformalDielectricLayer(dielectric_k=capild_k, thickness_over_metal=capild_thickness, thickness_where_no_metal=0.0, thickness_sidewall=0.0, reference="met3_cap")))
    psi.layers.append(StackLayerInfo(name="nild5", layer_type=StackLayerType.LAYER_TYPE_SIMPLE_DIELECTRIC,
        simple_dielectric_layer=SimpleDielectricLayer(dielectric_k=4.1, reference="nild4")))

    # CAPM (MIM cap above met3)
    psi.layers.append(StackLayerInfo(name="capm", layer_type=StackLayerType.LAYER_TYPE_METAL,
        metal_layer=MetalLayer(z=2.7861 + 0.845 + capild_thickness, thickness=capm_thickness,
            contact_above=Contact(name="via3_cap", layer_below="met3", metal_above="met4", thickness=0.29, width=0.20, spacing=0.20, border=0.06))))
    psi.layers.append(StackLayerInfo(name="nild5", layer_type=StackLayerType.LAYER_TYPE_SIMPLE_DIELECTRIC,
        simple_dielectric_layer=SimpleDielectricLayer(dielectric_k=4.1, reference="nild4")))

    # MET4 (two variants: ncap and cap)
    psi.layers.append(StackLayerInfo(name="met4_ncap", layer_type=StackLayerType.LAYER_TYPE_METAL,
        metal_layer=MetalLayer(z=4.0211, thickness=0.845,
            contact_above=Contact(name="via4_ncap", layer_below="met4", metal_above="met5", thickness=0.505, width=0.80, spacing=0.80, border=0.19))))
    psi.layers.append(StackLayerInfo(name="capild", layer_type=StackLayerType.LAYER_TYPE_CONFORMAL_DIELECTRIC,
        conformal_dielectric_layer=ConformalDielectricLayer(dielectric_k=capild_k, thickness_over_metal=capild_thickness, thickness_where_no_metal=0.0, thickness_sidewall=0.0, reference="met4_cap")))
    psi.layers.append(StackLayerInfo(name="met4_cap", layer_type=StackLayerType.LAYER_TYPE_METAL,
        metal_layer=MetalLayer(z=4.0211, thickness=0.845)))
    psi.layers.append(StackLayerInfo(name="nild6", layer_type=StackLayerType.LAYER_TYPE_SIMPLE_DIELECTRIC,
        simple_dielectric_layer=SimpleDielectricLayer(dielectric_k=4.0, reference="nild5")))

    # CAPM2 (MIM cap above met4)
    psi.layers.append(StackLayerInfo(name="capm2", layer_type=StackLayerType.LAYER_TYPE_METAL,
        metal_layer=MetalLayer(z=4.0211 + 0.845 + capild_thickness, thickness=capm_thickness,
            contact_above=Contact(name="via4_cap", layer_below="met4", metal_above="met5", thickness=0.505 - 0.1, width=0.80, spacing=0.80, border=0.19))))
    psi.layers.append(StackLayerInfo(name="nild6", layer_type=StackLayerType.LAYER_TYPE_SIMPLE_DIELECTRIC,
        simple_dielectric_layer=SimpleDielectricLayer(dielectric_k=4.0, reference="nild5")))

    # MET5
    psi.layers.append(StackLayerInfo(name="met5", layer_type=StackLayerType.LAYER_TYPE_METAL,
        metal_layer=MetalLayer(z=5.3711, thickness=1.26)))
    psi.layers.append(StackLayerInfo(name="topox", layer_type=StackLayerType.LAYER_TYPE_SIDEWALL_DIELECTRIC,
        sidewall_dielectric_layer=SidewallDielectricLayer(dielectric_k=3.9, height_above_metal=0.09, width_outside_sidewall=0.07, reference="met5")))
    psi.layers.append(StackLayerInfo(name="topnit", layer_type=StackLayerType.LAYER_TYPE_CONFORMAL_DIELECTRIC,
        conformal_dielectric_layer=ConformalDielectricLayer(dielectric_k=7.5, thickness_over_metal=0.54, thickness_where_no_metal=0.4223, thickness_sidewall=0.3777, reference="topox")))
    psi.layers.append(StackLayerInfo(name="air", layer_type=StackLayerType.LAYER_TYPE_SIMPLE_DIELECTRIC,
        simple_dielectric_layer=SimpleDielectricLayer(dielectric_k=3.0, reference="topnit")))


def build_process_parasitics_info(tech: Techfile) -> None:
    tech.process_parasitics = ProcessParasiticsInfo(
        side_halo=8.0,
        resistance=ResistanceInfo(),
        capacitance=CapacitanceInfo(),
    )
    ex = tech.process_parasitics
    ri = ex.resistance
    ci = ex.capacitance

    # sheet resistance (mΩ/sq)
    ri.layers.append(LayerResistance(layer_name="poly", resistance=48200))
    ri.layers.append(LayerResistance(layer_name="li1",  resistance=12800))
    ri.layers.append(LayerResistance(layer_name="met1", resistance=125))
    ri.layers.append(LayerResistance(layer_name="met2", resistance=125))
    ri.layers.append(LayerResistance(layer_name="met3", resistance=47))
    ri.layers.append(LayerResistance(layer_name="met4", resistance=47))
    ri.layers.append(LayerResistance(layer_name="met5", resistance=29))

    # contact resistance (mΩ/CNT)
    ri.contacts.append(ContactResistance(contact_name="licon_nsd_con",  device_layer_name="nsdm", layer_above="li1", resistance=185000))
    ri.contacts.append(ContactResistance(contact_name="licon_psd_con",  device_layer_name="psdm", layer_above="li1", resistance=585000))
    ri.contacts.append(ContactResistance(contact_name="licon_poly_con", device_layer_name="poly", layer_above="li1", resistance=152000))

    # via resistance (mΩ/via)
    ri.vias.append(ViaResistance(via_name="poly", resistance=152000))
    ri.vias.append(ViaResistance(via_name="mcon", resistance=9300))
    ri.vias.append(ViaResistance(via_name="via",  resistance=4500))
    ri.vias.append(ViaResistance(via_name="via2", resistance=3410))
    ri.vias.append(ViaResistance(via_name="via3", resistance=3410))
    ri.vias.append(ViaResistance(via_name="via4", resistance=380))

    # substrate capacitance (aF/µm² area, aF/µm perimeter)
    ci.substrates.append(SubstrateCapacitance(layer_name="poly", area_capacitance=106.13, perimeter_capacitance=55.27))
    ci.substrates.append(SubstrateCapacitance(layer_name="li1",  area_capacitance=36.99,  perimeter_capacitance=40.7))
    ci.substrates.append(SubstrateCapacitance(layer_name="met1", area_capacitance=25.78,  perimeter_capacitance=40.57))
    ci.substrates.append(SubstrateCapacitance(layer_name="met2", area_capacitance=17.5,   perimeter_capacitance=37.76))
    ci.substrates.append(SubstrateCapacitance(layer_name="met3", area_capacitance=12.37,  perimeter_capacitance=40.99))
    ci.substrates.append(SubstrateCapacitance(layer_name="met4", area_capacitance=8.42,   perimeter_capacitance=36.68))
    ci.substrates.append(SubstrateCapacitance(layer_name="met5", area_capacitance=6.32,   perimeter_capacitance=38.85))

    diff_nonfet = "diff"
    poly_nonres = "poly"
    all_active = "diff"

    # overlap capacitance (aF/µm²)
    ci.overlaps.append(OverlapCapacitance(top_layer_name="pwell",  bottom_layer_name="dnwell",     capacitance=120.0))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="poly",   bottom_layer_name="nwell",      capacitance=106.13))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="poly",   bottom_layer_name="pwell",      capacitance=106.13))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="li1",    bottom_layer_name="pwell",      capacitance=36.99))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="li1",    bottom_layer_name="nwell",      capacitance=36.99))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="li1",    bottom_layer_name="nwell",      capacitance=36.99))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="li1",    bottom_layer_name=diff_nonfet,  capacitance=55.3))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="li1",    bottom_layer_name="poly",       capacitance=94.16))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="met1",   bottom_layer_name="pwell",      capacitance=25.78))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="met1",   bottom_layer_name="nwell",      capacitance=25.78))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="met1",   bottom_layer_name=diff_nonfet,  capacitance=33.6))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="met1",   bottom_layer_name=poly_nonres,  capacitance=44.81))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="met1",   bottom_layer_name="li1",        capacitance=114.20))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="met2",   bottom_layer_name="nwell",      capacitance=17.5))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="met2",   bottom_layer_name="pwell",      capacitance=17.5))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="met2",   bottom_layer_name=diff_nonfet,  capacitance=20.8))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="met2",   bottom_layer_name=poly_nonres,  capacitance=24.50))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="met2",   bottom_layer_name="li1",        capacitance=37.56))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="met2",   bottom_layer_name="met1",       capacitance=133.86))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="met3",   bottom_layer_name="nwell",      capacitance=12.37))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="met3",   bottom_layer_name="pwell",      capacitance=12.37))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="met3",   bottom_layer_name=all_active,   capacitance=14.2))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="met3",   bottom_layer_name=poly_nonres,  capacitance=16.06))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="met3",   bottom_layer_name="li1",        capacitance=20.79))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="met3",   bottom_layer_name="met1",       capacitance=34.54))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="met3",   bottom_layer_name="met2",       capacitance=86.19))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="met4",   bottom_layer_name="nwell",      capacitance=8.42))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="met4",   bottom_layer_name="pwell",      capacitance=8.42))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="met4",   bottom_layer_name=all_active,   capacitance=9.41))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="met4",   bottom_layer_name=poly_nonres,  capacitance=10.01))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="met4",   bottom_layer_name="li1",        capacitance=11.67))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="met4",   bottom_layer_name="met1",       capacitance=15.03))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="met4",   bottom_layer_name="met2",       capacitance=20.33))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="met4",   bottom_layer_name="met3",       capacitance=84.03))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="met5",   bottom_layer_name="nwell",      capacitance=6.32))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="met5",   bottom_layer_name="pwell",      capacitance=6.32))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="met5",   bottom_layer_name=all_active,   capacitance=6.88))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="met5",   bottom_layer_name=poly_nonres,  capacitance=7.21))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="met5",   bottom_layer_name="li1",        capacitance=8.03))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="met5",   bottom_layer_name="met1",       capacitance=9.48))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="met5",   bottom_layer_name="met2",       capacitance=11.34))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="met5",   bottom_layer_name="met3",       capacitance=19.63))
    ci.overlaps.append(OverlapCapacitance(top_layer_name="met5",   bottom_layer_name="met4",       capacitance=68.33))

    # sidewall capacitance (aF/µm, offset µm)
    ci.sidewalls.append(SidewallCapacitance(layer_name="poly", capacitance=16.0,  offset=0.0))
    ci.sidewalls.append(SidewallCapacitance(layer_name="li1",  capacitance=25.5,  offset=0.14))
    ci.sidewalls.append(SidewallCapacitance(layer_name="met1", capacitance=44,    offset=0.25))
    ci.sidewalls.append(SidewallCapacitance(layer_name="met2", capacitance=50,    offset=0.3))
    ci.sidewalls.append(SidewallCapacitance(layer_name="met3", capacitance=74.0,  offset=0.4))
    ci.sidewalls.append(SidewallCapacitance(layer_name="met4", capacitance=94.0,  offset=0.57))
    ci.sidewalls.append(SidewallCapacitance(layer_name="met5", capacitance=155,   offset=0.5))

    # sidewall-overlap capacitance (aF/µm)
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="poly",  out_layer_name="nwell",      capacitance=55.27))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="poly",  out_layer_name="pwell",      capacitance=55.27))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="li1",   out_layer_name="nwell",      capacitance=40.70))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="li1",   out_layer_name="pwell",      capacitance=40.70))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="li1",   out_layer_name=diff_nonfet,  capacitance=44.27))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="li1",   out_layer_name=poly_nonres,  capacitance=51.85))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="poly",  out_layer_name="li1",        capacitance=25.14))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met1",  out_layer_name="nwell",      capacitance=40.57))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met1",  out_layer_name="pwell",      capacitance=40.57))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met1",  out_layer_name=diff_nonfet,  capacitance=43.10))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met1",  out_layer_name=poly_nonres,  capacitance=46.72))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="poly",  out_layer_name="met1",       capacitance=16.69))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met1",  out_layer_name="li1",        capacitance=59.50))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="li1",   out_layer_name="met1",       capacitance=34.70))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met2",  out_layer_name="nwell",      capacitance=37.76))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met2",  out_layer_name="pwell",      capacitance=37.76))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met2",  out_layer_name=diff_nonfet,  capacitance=39.54))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met2",  out_layer_name=poly_nonres,  capacitance=41.22))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="poly",  out_layer_name="met2",       capacitance=11.17))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met2",  out_layer_name="li1",        capacitance=46.28))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="li1",   out_layer_name="met2",       capacitance=21.74))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met2",  out_layer_name="met1",       capacitance=67.05))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met1",  out_layer_name="met2",       capacitance=48.19))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met3",  out_layer_name="nwell",      capacitance=40.99))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met3",  out_layer_name="pwell",      capacitance=40.99))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met3",  out_layer_name=all_active,   capacitance=42.25))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met3",  out_layer_name=poly_nonres,  capacitance=43.53))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="poly",  out_layer_name="met3",       capacitance=9.18))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met3",  out_layer_name="li1",        capacitance=46.71))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="li1",   out_layer_name="met3",       capacitance=15.08))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met3",  out_layer_name="met1",       capacitance=54.81))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met1",  out_layer_name="met3",       capacitance=26.68))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met3",  out_layer_name="met2",       capacitance=69.85))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met2",  out_layer_name="met3",       capacitance=44.43))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met4",  out_layer_name="nwell",      capacitance=36.68))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met4",  out_layer_name="pwell",      capacitance=36.68))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met4",  out_layer_name=diff_nonfet,  capacitance=37.57))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met4",  out_layer_name=poly_nonres,  capacitance=38.11))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="poly",  out_layer_name="met4",       capacitance=6.35))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met4",  out_layer_name="li1",        capacitance=39.71))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="li1",   out_layer_name="met4",       capacitance=10.14))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met4",  out_layer_name="met1",       capacitance=42.56))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met1",  out_layer_name="met4",       capacitance=16.42))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met4",  out_layer_name="met2",       capacitance=46.38))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met2",  out_layer_name="met4",       capacitance=22.33))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met4",  out_layer_name="met3",       capacitance=70.52))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met3",  out_layer_name="met4",       capacitance=42.64))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met5",  out_layer_name="nwell",      capacitance=38.85))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met5",  out_layer_name="pwell",      capacitance=38.85))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met5",  out_layer_name=diff_nonfet,  capacitance=39.52))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met5",  out_layer_name=poly_nonres,  capacitance=39.91))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="poly",  out_layer_name="met5",       capacitance=6.49))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met5",  out_layer_name="li1",        capacitance=41.15))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="li1",   out_layer_name="met5",       capacitance=7.64))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met5",  out_layer_name="met1",       capacitance=43.19))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met1",  out_layer_name="met5",       capacitance=12.02))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met5",  out_layer_name="met2",       capacitance=45.59))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met2",  out_layer_name="met5",       capacitance=15.69))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met5",  out_layer_name="met3",       capacitance=54.15))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met3",  out_layer_name="met5",       capacitance=27.84))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met5",  out_layer_name="met4",       capacitance=82.82))
    ci.sideoverlaps.append(SideOverlapCapacitance(in_layer_name="met4",  out_layer_name="met5",       capacitance=46.98))


def build_tech() -> Techfile:
    tech = Techfile(name="sky130A")
    build_layers(tech)
    build_lvs_computed_layers(tech)
    build_process_stack_info(tech)
    build_process_parasitics_info(tech)
    return tech
