# https://github.com/klayoutmatthias/sky130_xsection

delta(0.002)
height(20.0)
layers_file("sky130_xs.lyp")


# Input section
diff   = layer("65/20")   # Active (diffusion) area (type opposite of well/substrate underneath)
tap    = layer("65/44")   # Active (diffusion) area (type equal to the well/substrate underneath) (i.e., N+ and P+)
nwell  = layer("64/20")   # N-well region
dnwell = layer("64/18")   # Deep n-well region
pwbm   = layer("19/44")   # Regions (in UHVI) blocked from p-well implant (DE MOS devices only)
pwde   = layer("124/20")  # Regions to receive p-well drain-extended implants
hvtr   = layer("18/20")   # High-Vt RF transistor implant
hvtp   = layer("78/44")   # High-Vt LVPMOS implant
ldntm  = layer("11/44")   # N-tip implant on SONOS devices
hvi    = layer("75/20")   # High voltage (5.0V) thick oxide gate regions
tunm   = layer("80/20")   # SONOS device tunnel implant
lvtn   = layer("125/44")  # Low-Vt NMOS device
poly   = layer("66/20")   # Polysilicon
hvntm  = layer("125/20")  # High voltage N-tip implant
nsdm   = layer("93/44")   # N+ source/drain implant
psdm   = layer("94/20")   # P+ source/drain implant
rpm    = layer("86/20")   # 300 ohms/square polysilicon resistor implant
urpm   = layer("79/20")   # 2000 ohms/square polysilicon resistor implant
npc    = layer("95/20")   # Nitride poly cut (under licon1 areas)
licon1 = layer("66/44")   # Contact to local interconnect
li1    = layer("67/20")   # Local interconnect
mcon   = layer("67/44")   # Contact from local interconnect to metal1
met1   = layer("68/20")   # Metal 1
via    = layer("68/44")   # Contact from metal 1 to metal 2
met2   = layer("69/20")   # Metal 2
via2   = layer("69/44")   # Contact from metal 2 to metal 3
met3   = layer("70/20")   # Metal 3
via3   = layer("70/44")   # Contact from metal 3 to metal 4
met4   = layer("71/20")   # Metal 4
via4   = layer("71/44")   # Contact from metal 4 to metal 5
met5   = layer("72/20")   # Metal 5
pad    = layer("76/20")   # Passivation cut (opening over pads)
nsm    = layer("61/20")   # Nitride seal mask
capm   = layer("89/44")   # MiM capacitor plate over metal 3
cap2m  = layer("97/44")   # MiM capacitor plate over metal 4


# Variables

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


# Computed layers

poly_with_spacer = poly.sized(poly_spacer_width)
imide = pad.sized(pi_recess).inverted


# Process section

feol = []

m_psub = bulk
feol << m_psub

m_dnwell = mask(dnwell).grow(dnwell_depth, -dnwell_outdiff, mode: :round, into: feol)
feol << m_dnwell

m_pwell = grow(pwell_depth, 0.0, into: feol)
feol << m_pwell

m_nwell = mask(nwell).grow(nwell_depth, -nwell_outdiff, mode: :round, into: feol)
feol << m_nwell

m_nldd = mask(nsdm.not(poly)).grow(ldd_impl_depth, -ldd_impl_radius, mode: :round, into: feol)
feol << m_nldd

m_nsd = mask(nsdm.not(poly_with_spacer)).grow(sd_impl_depth, -sd_impl_radius, mode: :round, into: feol)
feol << m_nsd

m_pldd = mask(psdm.not(poly)).grow(ldd_impl_depth, -ldd_impl_radius, mode: :round, into: feol)
feol << m_pldd

m_psd = mask(psdm.not(poly_with_spacer)).grow(sd_impl_depth, -sd_impl_radius, mode: :round, into: feol)
feol << m_psd

mask(diff.or(tap).inverted).etch(sti_depth, taper: sti_taper, into: feol)

m_bpsg = deposit(sti_depth, 0.0)
planarize(into: m_bpsg, to: 0.0)

m_gox = deposit(gox_thickness)
m_gox = m_gox.or(mask(hvi).grow(hvgox_thickness - gox_thickness, 0.0))

m_poly = mask(poly).grow(poly_thickness, 0.0)

etch(2 * hvgox_thickness, 0.0, into: m_gox)

m_spacer = deposit(poly_thickness, poly_spacer_width, mode: :round)
etch(poly_thickness, 0.0, into: m_spacer)

m_bpsg = m_bpsg.or(deposit(bpsg_thickness, 0.0))
planarize(into: m_bpsg, to: bpsg_thickness)

li_bottom = bpsg_thickness
m_licon = mask(licon1).grow(bpsg_thickness, into: m_bpsg)
m_li = mask(li1).grow(li_thickness)
m_ild = deposit(ild2_thickness)

m1_bottom = li_bottom + ild2_thickness
planarize(into: m_ild, to: m1_bottom)
m_mcon = mask(mcon).grow(ild2_thickness, into: m_ild)

m_m1 = mask(met1).grow(m1_thickness)
m_ild = m_ild.or(deposit(ild3_thickness))

m2_bottom = m1_bottom + ild3_thickness
planarize(into: m_ild, to: m2_bottom)
m_via = mask(via).grow(ild3_thickness, into: m_ild)

m_m2 = mask(met2).grow(m2_thickness)
m_ild = m_ild.or(deposit(ild4_thickness))

m3_bottom = m2_bottom + ild4_thickness
planarize(into: m_ild, to: m3_bottom)
m_via2 = mask(via2).grow(ild4_thickness, into: m_ild)

m_m3 = mask(met3).grow(m3_thickness)
m_ild = m_ild.or(deposit(ild5_thickness))

m4_bottom = m3_bottom + ild5_thickness
planarize(into: m_ild, to: m4_bottom)

capm_depth = ild5_thickness-m3_thickness-capm_diel_thickness-capm_thickness/2
m_capm = mask(capm).grow(capm_thickness/2, into: m_ild, buried: capm_depth)

m_via3 = mask(via3.not(capm)).grow(ild5_thickness, into: m_ild)
m_via3 = m_via3.or(mask(via3.and(capm)).grow(capm_depth, into: m_ild))

m_m4 = mask(met4).grow(m4_thickness)
m_ild = m_ild.or(deposit(ild6_thickness))

m5_bottom = m4_bottom + ild6_thickness
planarize(into: m_ild, to: m5_bottom)

cap2m_depth = ild6_thickness-m4_thickness-cap2m_diel_thickness-cap2m_thickness/2
m_cap2m = mask(cap2m).grow(cap2m_thickness/2, into: m_ild, buried: cap2m_depth)

m_via4 = mask(via4.not(cap2m)).grow(ild6_thickness, into: m_ild)
m_via4 = m_via4.or(mask(via4.and(cap2m)).grow(cap2m_depth, into: m_ild))

m_m5 = mask(met5).grow(m5_thickness)

m_passv = deposit(passv_thickness, passv_thickness, mode: :square)
mask(pad).etch(passv_thickness, into: m_passv)

# two-step PI deposition - avoids topology at surface
pi_step1 = 3.0
pi_xradius = 3.0
m_pi = mask(imide).grow(pi_step1, 0.0)
planarize(into: m_pi, to: m5_bottom + pi_step1)
m_pi = m_pi.or(mask(imide).grow(pi_thickness - pi_step1, -pi_xradius, mode: :round))


# Output section

output("1/0", m_psub)
output("2/0", m_dnwell)
output("3/0", m_nwell)
output("4/0", m_pwell)
output("5/0", m_nldd)
output("6/0", m_nsd)
output("7/0", m_pldd)
output("8/0", m_psd)

output("20/0", m_bpsg)
output("21/0", m_gox)
output("22/0", m_poly)
output("23/0", m_spacer)

output("30/0", m_licon)
output("31/0", m_li)
output("32/0", m_ild)
output("33/0", m_mcon)
output("34/0", m_m1)
output("35/0", m_via)
output("36/0", m_m2)
output("37/0", m_via2)
output("38/0", m_m3)
output("38/10", m_capm)
output("39/0", m_via3)
output("40/0", m_m4)
output("40/10", m_cap2m)
output("41/0", m_via4)
output("42/0", m_m5)

output("50/0", m_passv)
output("51/0", m_pi)
