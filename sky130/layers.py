import gdsfactory as gf
from gdsfactory.technology import LayerLevel, LayerMap, LayerStack
from gdsfactory.typings import Layer

from sky130.config import PATH


class LayerMapSky130(LayerMap):
    areaidanalog: Layer = (81, 79)
    areaidcore: Layer = (81, 2)
    areaidcritCorner: Layer = (81, 51)
    areaidcritSid: Layer = (81, 52)
    areaiddeadZon: Layer = (81, 50)
    areaiddieCut: Layer = (81, 11)
    areaiddiode: Layer = (81, 23)
    areaidesd: Layer = (81, 19)
    areaidetest: Layer = (81, 101)
    areaidextendedDrain: Layer = (81, 57)
    areaidframe: Layer = (81, 3)
    areaidframeRect: Layer = (81, 12)
    areaidhvnwell: Layer = (81, 63)
    areaidinjection: Layer = (81, 17)
    areaidlowTapDensity: Layer = (81, 14)
    areaidlvNative: Layer = (81, 60)
    areaidmoduleCut: Layer = (81, 10)
    areaidnotCritSide: Layer = (81, 15)
    areaidopcDrop: Layer = (81, 54)
    areaidphoto: Layer = (81, 81)
    areaidrdlprobepad: Layer = (81, 27)
    areaidrfdiode: Layer = (81, 125)
    areaidseal: Layer = (81, 1)
    areaidsigPadDiff: Layer = (81, 6)
    areaidsigPadMetNtr: Layer = (81, 8)
    areaidsigPadWell: Layer = (81, 7)
    areaidstandardc: Layer = (81, 4)
    areaidsubstrateCut: Layer = (81, 53)
    areaidwaffleWindow: Layer = (81, 13)
    blankingdrawing: Layer = (124, 40)
    bumpdrawing: Layer = (127, 22)
    capacitordrawing: Layer = (82, 64)
    cbumpmask: Layer = (101, 0)
    cctm1drawing: Layer = (101, 44)
    cctm1mask: Layer = (35, 0)
    cctm1maskAdd: Layer = (101, 43)
    cctm1maskDrop: Layer = (101, 42)
    ccu1mmask: Layer = (93, 0)
    cdnmdrawing: Layer = (110, 20)
    cdnmmask: Layer = (48, 0)
    cdnmmaskAdd: Layer = (110, 21)
    cdnmmaskDrop: Layer = (110, 22)
    cfomdrawing: Layer = (22, 20)
    cfommask: Layer = (23, 0)
    cfommaskAdd: Layer = (22, 21)
    cfommaskDrop: Layer = (22, 22)
    cfomwaffleDrop: Layer = (22, 24)
    chvntmdrawing: Layer = (38, 20)
    chvntmmask: Layer = (39, 0)
    chvntmmaskAdd: Layer = (38, 21)
    chvntmmaskDrop: Layer = (38, 22)
    chvtpmdrawing: Layer = (88, 44)
    chvtpmmask: Layer = (97, 0)
    chvtpmmaskAdd: Layer = (97, 43)
    chvtpmmaskDrop: Layer = (97, 42)
    chvtrmdrawing: Layer = (98, 44)
    chvtrmmask: Layer = (98, 0)
    chvtrmmaskAdd: Layer = (98, 43)
    chvtrmmaskDrop: Layer = (98, 42)
    cldntmdrawing: Layer = (11, 20)
    cldntmmask: Layer = (11, 0)
    cli1mdrawing: Layer = (115, 44)
    cli1mmask: Layer = (56, 0)
    cli1mmaskAdd: Layer = (115, 43)
    cli1mmaskDrop: Layer = (115, 42)
    clicm1drawing: Layer = (106, 44)
    clicm1mask: Layer = (43, 0)
    clicm1maskAdd: Layer = (106, 43)
    clicm1maskDrop: Layer = (106, 42)
    clvomdrawing: Layer = (45, 20)
    clvommask: Layer = (46, 0)
    clvommaskAdd: Layer = (45, 21)
    clvommaskDrop: Layer = (45, 22)
    clvtnmdrawing: Layer = (25, 44)
    clvtnmmask: Layer = (25, 0)
    clvtnmmaskAdd: Layer = (25, 43)
    clvtnmmaskDrop: Layer = (25, 42)
    cmm1drawing: Layer = (62, 20)
    cmm1mask: Layer = (36, 0)
    cmm1maskAdd: Layer = (62, 21)
    cmm1maskDrop: Layer = (62, 22)
    cmm1waffleDrop: Layer = (62, 24)
    cmm2drawing: Layer = (105, 44)
    cmm2mask: Layer = (41, 0)
    cmm2maskAdd: Layer = (105, 43)
    cmm2maskDrop: Layer = (105, 42)
    cmm2waffleDrop: Layer = (105, 52)
    cmm3drawing: Layer = (107, 20)
    cmm3mask: Layer = (34, 0)
    cmm3maskAdd: Layer = (107, 21)
    cmm3maskDrop: Layer = (107, 22)
    cmm3waffleDrop: Layer = (107, 24)
    cmm4mask: Layer = (51, 0)
    cmm4maskAdd: Layer = (112, 43)
    cmm4maskDrop: Layer = (112, 42)
    cmm4waffleDrop: Layer = (112, 4)
    cmm5mask: Layer = (59, 0)
    cmm5waffleDrop: Layer = (117, 4)
    cncmdrawing: Layer = (96, 44)
    cncmmask: Layer = (17, 0)
    cnpcdrawing: Layer = (44, 20)
    cnpcmask: Layer = (49, 0)
    cnpcmaskAdd: Layer = (44, 43)
    cnpcmaskDrop: Layer = (44, 42)
    cnsdmdrawing: Layer = (29, 20)
    cnsdmmask: Layer = (30, 0)
    cnsdmmaskAdd: Layer = (29, 21)
    cnsdmmaskDrop: Layer = (29, 22)
    cnsmmask: Layer = (22, 0)
    cntmdrawing: Layer = (26, 20)
    cntmmask: Layer = (27, 0)
    cntmmaskAdd: Layer = (26, 21)
    cntmmaskDrop: Layer = (26, 22)
    cnwmdrawing: Layer = (109, 44)
    cnwmmask: Layer = (21, 0)
    cnwmmaskAdd: Layer = (109, 43)
    cnwmmaskDrop: Layer = (109, 42)
    conomdrawing: Layer = (87, 44)
    conommask: Layer = (88, 0)
    conommaskAdd: Layer = (87, 43)
    conommaskDrop: Layer = (87, 42)
    cp1mdrawing: Layer = (33, 44)
    cp1mmask: Layer = (28, 0)
    cp1mmaskAdd: Layer = (33, 43)
    cp1mmaskDrop: Layer = (33, 42)
    cp1mwaffleDrop: Layer = (33, 24)
    cpbomask: Layer = (99, 0)
    cpdmdrawing: Layer = (104, 44)
    cpdmmask: Layer = (37, 0)
    cpdmmaskAdd: Layer = (104, 43)
    cpdmmaskDrop: Layer = (104, 42)
    cpmm2mask: Layer = (94, 0)
    cpmmdrawing: Layer = (91, 44)
    cpsdmdrawing: Layer = (31, 20)
    cpsdmmask: Layer = (32, 0)
    cpsdmmaskAdd: Layer = (31, 21)
    cpsdmmaskDrop: Layer = (31, 22)
    crpmdrawing: Layer = (53, 44)
    crpmmask: Layer = (96, 0)
    crpmmaskAdd: Layer = (53, 43)
    crpmmaskDrop: Layer = (53, 42)
    crrpmmask: Layer = (102, 0)
    ctunmdrawing: Layer = (96, 20)
    ctunmmask: Layer = (20, 0)
    ctunmmaskAdd: Layer = (96, 21)
    ctunmmaskDrop: Layer = (96, 22)
    cubmmask: Layer = (100, 0)
    cviam2drawing: Layer = (108, 20)
    cviam2mask: Layer = (44, 0)
    cviam2maskAdd: Layer = (108, 21)
    cviam2maskDrop: Layer = (108, 22)
    cviam3drawing: Layer = (112, 20)
    cviam3mask: Layer = (50, 0)
    cviam3maskAdd: Layer = (112, 21)
    cviam3maskDrop: Layer = (112, 22)
    cviam4drawing: Layer = (117, 20)
    cviam4mask: Layer = (58, 0)
    cviam4maskAdd: Layer = (117, 21)
    cviam4maskDrop: Layer = (117, 22)
    cviamdrawing: Layer = (105, 20)
    cviammask: Layer = (40, 0)
    cviammaskAdd: Layer = (105, 21)
    cviammaskDrop: Layer = (105, 22)
    diffboundary: Layer = (65, 4)
    diffcut: Layer = (65, 14)
    diffdrawing: Layer = (65, 20)
    diffhv: Layer = (65, 8)
    difflabel: Layer = (65, 6)
    diffnet: Layer = (65, 23)
    diffpin: Layer = (65, 16)
    diffres: Layer = (65, 13)
    dnwelldrawing: Layer = (64, 18)
    fomdummy: Layer = (22, 23)
    hvidrawing: Layer = (75, 20)
    hvntmdrawing: Layer = (125, 20)
    hvtpdrawing: Layer = (78, 44)
    hvtrdrawing: Layer = (18, 20)
    inductordrawing: Layer = (82, 24)
    inductorlabel: Layer = (82, 25)
    inductorterm1: Layer = (82, 26)
    inductorterm2: Layer = (82, 27)
    inductorterm3: Layer = (82, 28)
    ldntmdrawing: Layer = (11, 44)
    li1blockage: Layer = (67, 10)
    li1boundary: Layer = (67, 4)
    li1cut: Layer = (67, 14)
    li1drawing: Layer = (67, 20)
    li1label: Layer = (67, 5)
    li1net: Layer = (67, 23)
    li1pin: Layer = (67, 16)
    li1probe: Layer = (67, 25)
    li1res: Layer = (67, 13)
    li1short: Layer = (67, 15)
    licon1boundary: Layer = (66, 60)
    licon1drawing: Layer = (66, 44)
    licon1net: Layer = (66, 41)
    licon1pin: Layer = (66, 58)
    lvtndrawing: Layer = (125, 44)
    markererror: Layer = (83, 6)
    markerwarning: Layer = (83, 7)
    mconboundary: Layer = (67, 60)
    mcondrawing: Layer = (67, 44)
    mconnet: Layer = (67, 41)
    mconpin: Layer = (67, 48)
    met1blockage: Layer = (68, 10)
    met1boundary: Layer = (68, 4)
    met1cut: Layer = (68, 14)
    met1drawing: Layer = (68, 20)
    met1label: Layer = (68, 5)
    met1net: Layer = (68, 23)
    met1option1: Layer = (68, 32)
    met1option2: Layer = (68, 33)
    met1option3: Layer = (68, 34)
    met1option4: Layer = (68, 35)
    met1option5: Layer = (68, 36)
    met1option6: Layer = (68, 37)
    met1option7: Layer = (68, 38)
    met1option8: Layer = (68, 39)
    met1pin: Layer = (68, 16)
    met1probe: Layer = (68, 25)
    met1psa1: Layer = (68, 88)
    met1psa2: Layer = (68, 89)
    met1psa3: Layer = (68, 90)
    met1psa4: Layer = (68, 91)
    met1psa5: Layer = (68, 92)
    met1psa6: Layer = (68, 93)
    met1res: Layer = (68, 13)
    met1short: Layer = (68, 15)
    met2blockage: Layer = (69, 10)
    met2boundary: Layer = (69, 4)
    met2cut: Layer = (69, 14)
    met2drawing: Layer = (69, 20)
    met2label: Layer = (69, 5)
    met2net: Layer = (69, 23)
    met2option1: Layer = (69, 32)
    met2option2: Layer = (69, 33)
    met2option3: Layer = (69, 34)
    met2option4: Layer = (69, 35)
    met2option5: Layer = (69, 36)
    met2option6: Layer = (69, 37)
    met2option7: Layer = (69, 38)
    met2option8: Layer = (69, 39)
    met2pin: Layer = (69, 16)
    met2probe: Layer = (69, 25)
    met2psa1: Layer = (69, 88)
    met2psa2: Layer = (69, 89)
    met2psa3: Layer = (69, 90)
    met2psa4: Layer = (69, 91)
    met2psa5: Layer = (69, 92)
    met2psa6: Layer = (69, 93)
    met2res: Layer = (69, 13)
    met2short: Layer = (69, 15)
    met3blockage: Layer = (70, 10)
    met3boundary: Layer = (70, 4)
    met3cut: Layer = (70, 14)
    met3drawing: Layer = (70, 20)
    met3fuse: Layer = (70, 17)
    met3label: Layer = (70, 5)
    met3net: Layer = (70, 23)
    met3option1: Layer = (70, 32)
    met3option2: Layer = (70, 33)
    met3option3: Layer = (70, 34)
    met3option4: Layer = (70, 35)
    met3option5: Layer = (70, 36)
    met3option6: Layer = (70, 37)
    met3option7: Layer = (70, 38)
    met3option8: Layer = (70, 39)
    met3pin: Layer = (70, 16)
    met3probe: Layer = (70, 25)
    met3psa1: Layer = (70, 88)
    met3psa2: Layer = (70, 89)
    met3psa3: Layer = (70, 90)
    met3psa4: Layer = (70, 91)
    met3psa5: Layer = (70, 92)
    met3psa6: Layer = (70, 93)
    met3res: Layer = (70, 13)
    met3short: Layer = (70, 15)
    met4blockage: Layer = (71, 10)
    met4boundary: Layer = (71, 4)
    met4cut: Layer = (71, 14)
    met4drawing: Layer = (71, 20)
    met4fuse: Layer = (71, 17)
    met4label: Layer = (71, 5)
    met4net: Layer = (71, 23)
    met4option1: Layer = (71, 32)
    met4option2: Layer = (71, 33)
    met4option3: Layer = (71, 34)
    met4option4: Layer = (71, 35)
    met4option5: Layer = (71, 36)
    met4option6: Layer = (71, 37)
    met4option7: Layer = (71, 38)
    met4option8: Layer = (71, 39)
    met4pin: Layer = (71, 16)
    met4probe: Layer = (71, 25)
    met4psa1: Layer = (71, 88)
    met4psa2: Layer = (71, 89)
    met4psa3: Layer = (71, 90)
    met4psa4: Layer = (71, 91)
    met4psa5: Layer = (71, 92)
    met4psa6: Layer = (71, 93)
    met4res: Layer = (71, 13)
    met4short: Layer = (71, 15)
    met5blockage: Layer = (72, 10)
    met5boundary: Layer = (72, 4)
    met5cut: Layer = (72, 14)
    met5drawing: Layer = (72, 20)
    met5fuse: Layer = (72, 17)
    met5label: Layer = (72, 5)
    met5net: Layer = (72, 23)
    met5option1: Layer = (72, 32)
    met5option2: Layer = (72, 33)
    met5option3: Layer = (72, 34)
    met5option4: Layer = (72, 35)
    met5option5: Layer = (72, 36)
    met5option6: Layer = (72, 37)
    met5option7: Layer = (72, 38)
    met5option8: Layer = (72, 39)
    met5pin: Layer = (72, 16)
    met5probe: Layer = (72, 25)
    met5psa1: Layer = (72, 88)
    met5psa2: Layer = (72, 89)
    met5psa3: Layer = (72, 90)
    met5psa4: Layer = (72, 91)
    met5psa5: Layer = (72, 92)
    met5psa6: Layer = (72, 93)
    met5res: Layer = (72, 13)
    met5short: Layer = (72, 15)
    ncmdrawing: Layer = (92, 44)
    npcdrawing: Layer = (95, 20)
    npndrawing: Layer = (82, 20)
    npnlabel: Layer = (82, 5)
    nsdmdrawing: Layer = (93, 44)
    nsmdrawing: Layer = (61, 20)
    nwelldrawing: Layer = (64, 20)
    nwelllabel: Layer = (64, 5)
    nwellnet: Layer = (84, 23)
    nwellpin: Layer = (64, 16)
    overlapboundary: Layer = (90, 4)
    overlapdrawing: Layer = (90, 20)
    padCenterdrawing: Layer = (81, 20)
    paddrawing: Layer = (76, 20)
    padlabel: Layer = (76, 5)
    padpin: Layer = (76, 16)
    pmm2drawing: Layer = (77, 20)
    pmmdrawing: Layer = (85, 44)
    pnpdrawing: Layer = (82, 44)
    pnplabel: Layer = (82, 59)
    polyboundary: Layer = (66, 4)
    polycut: Layer = (66, 14)
    polydrawing: Layer = (66, 20)
    polygate: Layer = (66, 9)
    polylabel: Layer = (66, 5)
    polymodel: Layer = (66, 83)
    polynet: Layer = (66, 23)
    polypin: Layer = (66, 16)
    polyprobe: Layer = (66, 25)
    polyres: Layer = (66, 13)
    polyshort: Layer = (66, 15)
    prBoundaryboundary: Layer = (235, 4)
    prBoundarydrawing: Layer = (235, 0)
    prunedrawing: Layer = (84, 44)
    psdmdrawing: Layer = (94, 20)
    pwellcut: Layer = (64, 14)
    pwelldrawing: Layer = (64, 44)
    pwellisolabel: Layer = (44, 5)
    pwellisopin: Layer = (44, 16)
    pwelllabel: Layer = (64, 59)
    pwellpin: Layer = (122, 16)
    pwellres: Layer = (64, 13)
    rdlcondrawing: Layer = (13, 0)
    rdlcut: Layer = (74, 14)
    rdldrawing: Layer = (74, 20)
    rdllabel: Layer = (74, 5)
    rdloption1: Layer = (89, 32)
    rdloption2: Layer = (89, 33)
    rdloption3: Layer = (89, 34)
    rdloption4: Layer = (89, 35)
    rdloption5: Layer = (89, 36)
    rdloption6: Layer = (89, 37)
    rdloption7: Layer = (89, 38)
    rdloption8: Layer = (89, 39)
    rdlpin: Layer = (74, 16)
    rdlpsa1: Layer = (74, 88)
    rdlpsa2: Layer = (74, 89)
    rdlpsa3: Layer = (74, 90)
    rdlpsa4: Layer = (74, 91)
    rdlpsa5: Layer = (74, 92)
    rdlpsa6: Layer = (74, 93)
    rdlres: Layer = (74, 13)
    rdlshort: Layer = (74, 15)
    rpmdrawing: Layer = (86, 20)
    rrpmdrawing: Layer = (102, 20)
    tapboundary: Layer = (65, 60)
    tapdrawing: Layer = (65, 44)
    taplabel: Layer = (65, 5)
    tapnet: Layer = (65, 41)
    tappin: Layer = (65, 48)
    targetdrawing: Layer = (76, 44)
    textdrawing: Layer = (83, 44)
    tunmdrawing: Layer = (80, 20)
    ubmdrawing: Layer = (127, 21)
    vhvidrawing: Layer = (74, 21)
    via2blockage: Layer = (7, 3)
    via2boundary: Layer = (69, 60)
    via2drawing: Layer = (69, 44)
    via2net: Layer = (69, 41)
    via2pin: Layer = (69, 58)
    via3blockage: Layer = (9, 3)
    via3boundary: Layer = (70, 60)
    via3drawing: Layer = (70, 44)
    via3label: Layer = (9, 1)
    via3net: Layer = (70, 41)
    via3pin: Layer = (70, 48)
    via4blockage: Layer = (11, 3)
    via4boundary: Layer = (71, 60)
    via4drawing: Layer = (71, 44)
    via4label: Layer = (11, 1)
    via4net: Layer = (71, 41)
    via4pin: Layer = (71, 48)
    viablockage: Layer = (5, 3)
    viaboundary: Layer = (68, 60)
    viadrawing: Layer = (68, 44)
    vialabel: Layer = (5, 1)
    vianet: Layer = (68, 41)
    viapin: Layer = (68, 58)

    diff: Layer = (
        65,
        20,
    )  # Active (diffusion) area (type opposite of well/substrate underneath)
    tap: Layer = (
        65,
        44,
    )  # Active (diffusion) area (type equal to the well/substrate underneath) (N+ and P+)
    nwell: Layer = (64, 20)  # N-well region
    dnwell: Layer = (64, 18)  # Deep n-well region
    pwbm: Layer = (
        19,
        44,
    )  # Regions (in UHVI) blocked from p-well implant (DE MOS devices only)
    pwde: Layer = (124, 20)  # Regions to receive p-well drain-extended implants
    hvtr: Layer = (18, 20)  # High-Vt RF transistor implant
    hvtp: Layer = (78, 44)  # High-Vt LVPMOS implant
    ldntm: Layer = (11, 44)  # N-tip implant on SONOS devices
    hvi: Layer = (75, 20)  # High voltage (5.0V) thick oxide gate regions
    tunm: Layer = (80, 20)  # SONOS device tunnel implant

    lvtn: Layer = (125, 44)  # Low-Vt NMOS device
    poly: Layer = (66, 20)  # Polysilicon
    hvntm: Layer = (125, 20)  # High voltage N-tip implant
    nsdm: Layer = (93, 44)  # N+ source/drain implant
    psdm: Layer = (94, 20)  # P+ source/drain implant
    rpm: Layer = (86, 20)  # 300 ohms/square polysilicon resistor implant
    urpm: Layer = (79, 20)  # 2000 ohms/square polysilicon resistor implant
    npc: Layer = (95, 20)  # Nitride poly cut (under licon1 areas)
    licon1: Layer = (66, 44)  # Contact to local interconnect
    li1: Layer = (67, 20)  # Local interconnect
    mcon: Layer = (67, 44)  # Contact from local interconnect to metal1
    met1: Layer = (68, 20)  # Metal 1
    via: Layer = (68, 44)  # Contact from metal 1 to metal 2
    met2: Layer = (69, 20)  # Metal 2
    via2: Layer = (69, 44)  # Contact from metal 2 to metal 3
    met3: Layer = (70, 20)  # Metal 3
    via3: Layer = (70, 44)  # Contact from metal 3 to metal 4
    met4: Layer = (71, 20)  # Metal 4
    via4: Layer = (71, 44)  # Contact from metal 4 to metal 5
    met5: Layer = (72, 20)  # Metal 5
    pad: Layer = (76, 20)  # Passivation cut (opening over pads)
    nsm: Layer = (61, 20)  # Nitride seal mask
    capm: Layer = (89, 44)  # MiM capacitor plate over metal 3
    cap2m: Layer = (97, 44)  # MiM capacitor plate over metal 4

    LABEL_INSTANCE: Layer = (66, 0)
    TEXT: Layer = (66, 0)


LAYER = LayerMapSky130

nm = 1e-3
poly_spacer_width = 0.03
dnwell_depth = 1.2
dnwell_outdiff = 0.3
pwell_depth = 0.7
nwell_depth = 0.8
nwell_outdiff = 0.2
ldd_impl_depth = 0.06
ldd_impl_radius = 0.02
sd_impl_depth = 0.12
sd_impl_radius = 0.04
sti_depth = 0.3
sti_taper = 7
gox_thickness = 0.004
hvgox_thickness = 0.008
poly_thickness = 0.18
bpsg_thickness = 0.94
li_thickness = 0.1
ild2_thickness = 0.43
m1_thickness = 0.36
ild3_thickness = 0.27 + m1_thickness
m2_thickness = 0.36
ild4_thickness = 0.42 + m2_thickness
m3_thickness = 0.845
ild5_thickness = 0.39 + m3_thickness
m4_thickness = 0.845
ild6_thickness = 0.505 + m4_thickness
m5_thickness = 1.26
capm_thickness = 0.06
capm_diel_thickness = 0.04
cap2m_thickness = 0.06
cap2m_diel_thickness = 0.04
passv_thickness = 0.6
pi_thickness = 6.1
pi_recess = 2.0

via1_thickness = 0.27
via2_thickness = 0.42
via3_thickness = 0.39
via4_thickness = 0.505
licon1_thickness = 0.9361
mcon_thickness = 0.075 + 0.265


def get_layer_stack() -> LayerStack:
    """Returns sky LayerStack."""
    zmin_m1 = licon1_thickness + li_thickness + mcon_thickness
    zmin_m2 = zmin_m1 + m1_thickness + via1_thickness
    zmin_m3 = zmin_m2 + m2_thickness + via2_thickness
    zmin_m4 = zmin_m3 + m3_thickness + via3_thickness
    zmin_m5 = zmin_m4 + m4_thickness + via4_thickness

    thickness_nwell = sd_impl_depth  # made up number

    return LayerStack(
        layers=dict(
            poly=LayerLevel(
                layer=LAYER.poly,
                thickness=poly_thickness,
                zmin=0.0,
                material="psi",
            ),
            dnwell=LayerLevel(
                layer=LAYER.dnwell,
                zmin=-dnwell_depth,
                material="n",
                thickness=dnwell_depth,
            ),
            nwell=LayerLevel(
                layer=LAYER.nwell,
                zmin=-thickness_nwell,
                material="n",
                thickness=thickness_nwell,
            ),
            pwell=LayerLevel(
                layer=LAYER.pwbm,
                zmin=-pwell_depth,
                material="p",
                thickness=pwell_depth,
            ),
            nsdm=LayerLevel(
                layer=LAYER.nsdm,
                zmin=-sd_impl_depth,
                material="n",
                thickness=sd_impl_depth,
            ),
            hvtp=LayerLevel(
                layer=LAYER.hvtp,
                zmin=-sd_impl_depth,
                material="p",
                thickness=sd_impl_depth,
            ),
            licon1=LayerLevel(
                layer=LAYER.licon1,
                zmin=0,
                material="metal",
                thickness=licon1_thickness,
            ),
            li1=LayerLevel(
                layer=LAYER.li1,
                zmin=licon1_thickness,
                material="metal",
                thickness=li_thickness,
            ),
            mcon=LayerLevel(
                layer=LAYER.mcon,
                zmin=licon1_thickness + li_thickness,
                material="metal",
                thickness=mcon_thickness,
            ),
            met1=LayerLevel(
                layer=LAYER.met1,
                zmin=zmin_m1,
                material="metal",
                thickness=m1_thickness,
            ),
            via1=LayerLevel(
                layer=LAYER.via,
                zmin=zmin_m1 + m1_thickness,
                material="metal",
                thickness=via1_thickness,
            ),
            met2=LayerLevel(
                layer=LAYER.met2,
                zmin=zmin_m2,
                material="metal",
                thickness=m2_thickness,
            ),
            via2=LayerLevel(
                layer=LAYER.via2,
                zmin=zmin_m2 + m2_thickness,
                material="metal",
                thickness=via2_thickness,
            ),
            met3=LayerLevel(
                layer=LAYER.met3,
                zmin=zmin_m3,
                material="metal",
                thickness=m3_thickness,
            ),
            via3=LayerLevel(
                layer=LAYER.via3,
                zmin=zmin_m3 + m3_thickness,
                material="metal",
                thickness=via3_thickness,
            ),
            met4=LayerLevel(
                layer=LAYER.met4,
                zmin=zmin_m4,
                material="metal",
                thickness=m4_thickness,
            ),
            via4=LayerLevel(
                layer=LAYER.via4,
                zmin=zmin_m4 + m4_thickness,
                material="metal",
                thickness=via4_thickness,
            ),
            met5=LayerLevel(
                layer=LAYER.met5,
                zmin=zmin_m5,
                material="metal",
                thickness=m5_thickness,
            ),
        )
    )


LAYER_STACK = get_layer_stack()
LAYER_VIEWS = gf.technology.LayerViews(PATH.lyp_yaml)
connectivity = [
    ("met1", "via", "met2"),
    ("met2", "via2", "met3"),
    ("met3", "via3", "met4"),
    ("met4", "via4", "met5"),
    ("licon1", "li1", "mcon"),
    ("poly", "licon1"),
    ("nwell", "dnwell"),
    ("nwell", "nsdm"),
    ("pwell", "pwbm"),
    ("hvtp", "pwbm"),
    ("hvi", "poly"),
    ("ldntm", "poly"),
    ("hvntm", "poly"),
]


if __name__ == "__main__":
    # LAYER_VIEWS.to_yaml(PATH.lyp_yaml)
    # LAYER_VIEWS.to_lyp(PATH.lyp)
    # print(PATH.lyp)
    # print(lyp_to_dataclass(PATH.lyp))
    # print(LAYER_STACK.get_klayout_3d_script())
    from gdsfactory.technology.klayout_tech import KLayoutTechnology

    t = KLayoutTechnology(
        name="sky130",
        layer_map=LAYER,
        layer_views=LAYER_VIEWS,
        layer_stack=LAYER_STACK,
        connectivity=connectivity,
    )
    t.write_tech(tech_dir=PATH.klayout)
