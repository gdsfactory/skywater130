"""Generate interactive layer_stack.md for skywater130.

Reads layer_stack and cross_sections from the PDK and writes
docs/layer_stack.md with interactive SVG/JS visualizations.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

from sky130.config import PATH
from sky130 import PDK

BANDS = [("", PDK)]

# ---------------------------------------------------------------------------
# Colour palette
# ---------------------------------------------------------------------------

MATERIAL_COLORS = {
    "si": "#A0A0A0", "silicon": "#A0A0A0",
    "sio2": "#FFF8DC", "oxide": "#D0D0D0",
    "sin": "#8FBC8F", "sion": "#8FBC8F",
    "ge": "#4682B4", "al": "#4CAF50", "cu": "#D0A050",
    "w": "#9E9E9E", "tin": "#DDA0DD", "air": "#E8F4FD",
    "nclad": "#FFF8DC", "nbox": "#FFF8DC",
}

XS_MATERIAL_COLORS = {
    "si": "#5B8CBE", "silicon": "#5B8CBE",
    "sin": "#2E8B57", "sion": "#2E8B57",
    "ge": "#4682B4", "al": "#CCC", "cu": "#D0A050",
    "tin": "#CD853F", "w": "#9E9E9E",
}


def _color_for_layer(material):
    mat = (material or "").lower().strip()
    return MATERIAL_COLORS.get(mat, "#D0D0D0")


def _color_for_xs(material):
    mat = (material or "").lower().strip()
    return XS_MATERIAL_COLORS.get(mat, "#999")


def _infer_layer_type(material, name):
    mat = (material or "").lower()
    n = (name or "").lower()
    if any(m in mat for m in ("al", "cu", "w", "tin", "nickel", "metal")):
        return "conductor"
    if "via" in n:
        return "via"
    if "sub" in n or "box" in n:
        return "substrate"
    return "dielectric"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _gds_layer_number(layer_attr):
    if layer_attr is None:
        return None
    inner = getattr(layer_attr, "layer", layer_attr)
    if isinstance(inner, (tuple, list)) and len(inner) >= 1:
        try:
            return int(inner[0])
        except (ValueError, TypeError):
            return None
    try:
        return int(inner)
    except (ValueError, TypeError):
        return None


def _nice_step(range_val, target_ticks=10):
    raw = range_val / target_ticks
    mag = 10 ** math.floor(math.log10(raw))
    residual = raw / mag
    if residual <= 1.5:
        return mag
    elif residual <= 3.5:
        return 2 * mag
    elif residual <= 7.5:
        return 5 * mag
    return 10 * mag


# ---------------------------------------------------------------------------
# Data extraction
# ---------------------------------------------------------------------------


def _extract_layers(layer_stack):
    layers = []
    for name, level in layer_stack.layers.items():
        thickness = getattr(level, "thickness", 0) or 0
        zmin = getattr(level, "zmin", 0) or 0
        material = getattr(level, "material", "") or ""
        gds = _gds_layer_number(getattr(level, "layer", None))
        layers.append({
            "name": name, "gds": gds, "material": material,
            "type": _infer_layer_type(material, name),
            "zmin": round(zmin, 4), "zmax": round(zmin + thickness, 4),
            "thickness": round(thickness, 4),
            "color": _color_for_layer(material),
        })
    layers.sort(key=lambda l: l["zmin"])
    return layers


def _compute_layout(layers, svg_w=550, svg_h=750):
    margin = {"top": 60, "bottom": 30, "left": 70, "right": 100}
    plot_h = svg_h - margin["top"] - margin["bottom"]

    real = [l for l in layers if abs(l["thickness"]) > 1e-9]
    if not real:
        return layers, []

    n = len(real)
    row_h = plot_h / max(n, 1)
    for i, l in enumerate(real):
        l["uy"] = round(margin["top"] + (n - 1 - i) * row_h, 1)
        l["uh"] = round(row_h * 0.93, 1)

    all_z = []
    for l in real:
        all_z.extend([l["zmin"], l["zmax"]])
    z_min_g = min(all_z)
    z_max_g = max(all_z)
    z_range = z_max_g - z_min_g or 1.0

    def z_to_y(z):
        frac = (z - z_min_g) / z_range
        return margin["top"] + plot_h - frac * plot_h

    for l in real:
        overlapping = [ol for ol in real if
                       ol["zmin"] < l["zmax"] - 1e-6 and ol["zmax"] > l["zmin"] + 1e-6]
        l["ncols"] = len(overlapping)
        l["col"] = overlapping.index(l) if l in overlapping else 0
        sy_top = z_to_y(l["zmax"])
        sy_bot = z_to_y(l["zmin"])
        l["sy"] = round(sy_top, 1)
        l["sh"] = round(max(sy_bot - sy_top, 2), 1)

    ticks = []
    step = _nice_step(z_range)
    z = math.floor(z_min_g / step) * step
    while z <= z_max_g + step * 0.5:
        ticks.append({"z": round(z, 2), "py": round(z_to_y(z), 1)})
        z += step

    return real, ticks


def _extract_cross_sections(pdk, layer_stack):
    xs_dict = getattr(pdk, "cross_sections", {})
    if not xs_dict:
        return []

    layer_z_by_gds = {}
    layer_z_by_name = {}
    for name, level in layer_stack.layers.items():
        thickness = getattr(level, "thickness", 0) or 0
        zmin = getattr(level, "zmin", 0) or 0
        material = getattr(level, "material", "") or ""
        gds = _gds_layer_number(getattr(level, "layer", None))
        info = {"name": name, "zmin": zmin, "thickness": thickness, "material": material, "gds": gds}
        if gds is not None:
            layer_z_by_gds[gds] = info
        layer_z_by_name[name] = info

    layer_name_to_gds = {}
    layer_map = getattr(pdk, "layers", None)
    if layer_map is not None:
        try:
            for entry in layer_map:
                lname = getattr(entry, "name", None)
                val = getattr(entry, "value", None)
                gds = _gds_layer_number(val) if isinstance(val, (tuple, list)) else (val if isinstance(val, int) else _gds_layer_number(val))
                if lname and gds is not None:
                    layer_name_to_gds[lname] = gds
        except TypeError:
            pass

    def resolve(layer_ref):
        gds = _gds_layer_number(layer_ref)
        if gds is not None and gds in layer_z_by_gds:
            return layer_z_by_gds[gds]
        if isinstance(layer_ref, str):
            if layer_ref in layer_z_by_name:
                return layer_z_by_name[layer_ref]
            g = layer_name_to_gds.get(layer_ref)
            if g is not None and g in layer_z_by_gds:
                return layer_z_by_gds[g]
        return None

    results = []
    for xs_name, xs_func in xs_dict.items():
        try:
            xs = xs_func() if callable(xs_func) else xs_func
        except Exception:
            continue
        sections = getattr(xs, "sections", [])
        main_layer = getattr(xs, "layer", None)
        main_width = getattr(xs, "width", None)
        xs_layers = []

        if main_layer is not None and main_width is not None:
            info = resolve(main_layer)
            if info:
                xs_layers.append({
                    "name": info["name"], "material": info["material"],
                    "zmin": round(info["zmin"], 4),
                    "zmax": round(info["zmin"] + info["thickness"], 4),
                    "thickness": round(info["thickness"], 4),
                    "width": round(float(main_width), 2), "gds": info["gds"],
                })

        for section in sections:
            sec_layer = getattr(section, "layer", None)
            sec_width = getattr(section, "width", None)
            if sec_layer is None or sec_width is None:
                continue
            info = resolve(sec_layer)
            if info:
                xs_layers.append({
                    "name": info["name"], "material": info["material"],
                    "zmin": round(info["zmin"], 4),
                    "zmax": round(info["zmin"] + info["thickness"], 4),
                    "thickness": round(info["thickness"], 4),
                    "width": round(float(sec_width), 2), "gds": info["gds"],
                })

        if xs_layers:
            results.append({"name": xs_name, "layers": xs_layers})

    return results


# ---------------------------------------------------------------------------
# SVG rendering
# ---------------------------------------------------------------------------

_svg_counter = 100


def _next_id():
    global _svg_counter
    _svg_counter += 1
    return f"sv_{_svg_counter}"


def _render_layer_stack(layers, ticks, svg_id, svg_w=550, svg_h=750):
    margin = {"top": 60, "bottom": 30, "left": 70, "right": 100}
    plot_w = svg_w - margin["left"] - margin["right"]
    plot_h = svg_h - margin["top"] - margin["bottom"]
    d = json.dumps(layers, separators=(",", ": "))
    t = json.dumps(ticks, separators=(",", ": "))
    m = json.dumps(margin, separators=(",", ": "))

    return f'''<div id="{svg_id}" style="position:relative;display:inline-block;font-family:system-ui,sans-serif;padding:10px 10px 40px 10px">
  <div style="margin-bottom:6px">
    <button class="sv-btn" data-mode="uniform" style="font-size:12px;padding:3px 10px;cursor:pointer;border:1px solid #aaa;border-radius:3px;background:#e0e0e0">Uniform</button>
    <button class="sv-btn" data-mode="scale" style="font-size:12px;padding:3px 10px;cursor:pointer;border:1px solid #aaa;border-radius:3px;background:#fff;margin-left:4px">To Scale</button>
  </div>
  <svg width="{svg_w}" height="{svg_h}" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,sans-serif" font-size="11">
    <rect width="{svg_w}" height="{svg_h}" fill="white"/>
    <text x="{svg_w//2}" y="24" text-anchor="middle" font-size="14" font-weight="bold">Layer Stack</text>
    <g class="ticks"></g><g class="layers"></g>
  </svg>
  <div class="tooltip" style="display:none;position:absolute;background:white;color:#222;border:1px solid #ccc;border-radius:4px;padding:6px 10px;font-size:11px;pointer-events:none;box-shadow:0 2px 6px rgba(0,0,0,.15);z-index:10;white-space:nowrap"></div>
</div>
<script>
(function(){{
  const root=document.getElementById("{svg_id}"),svg=root.querySelector("svg"),gT=svg.querySelector(".ticks"),gL=svg.querySelector(".layers"),tip=root.querySelector(".tooltip");
  const data={d},ticks={t},margin={m},plotW={plot_w},plotH={plot_h};
  let mode="uniform";
  function lum(hex){{const r=parseInt(hex.slice(1,3),16)/255,g=parseInt(hex.slice(3,5),16)/255,b=parseInt(hex.slice(5,7),16)/255;return .299*r+.587*g+.114*b}}
  function render(){{
    gT.innerHTML="";
    if(mode==="scale"){{
      const ax=margin.left-10,tl=5,yT=margin.top,yB=margin.top+plotH;
      const a=document.createElementNS("http://www.w3.org/2000/svg","line");
      Object.entries({{x1:ax,y1:yT,x2:ax,y2:yB,stroke:"#666","stroke-width":1}}).forEach(([k,v])=>a.setAttribute(k,v));
      gT.appendChild(a);
      ticks.forEach(t=>{{
        const iz=Math.abs(t.z)<1e-9;
        const tk=document.createElementNS("http://www.w3.org/2000/svg","line");
        Object.entries({{x1:ax-tl,y1:t.py,x2:ax,y2:t.py,stroke:"#666","stroke-width":iz?1.5:1}}).forEach(([k,v])=>tk.setAttribute(k,v));
        gT.appendChild(tk);
        const lb=document.createElementNS("http://www.w3.org/2000/svg","text");
        lb.setAttribute("x",ax-tl-3);lb.setAttribute("y",t.py+3);lb.setAttribute("text-anchor","end");
        lb.setAttribute("font-size","9");lb.setAttribute("fill",iz?"#333":"#666");
        if(iz)lb.setAttribute("font-weight","bold");
        lb.textContent=t.z.toFixed(2);gT.appendChild(lb);
      }});
    }}
    gL.innerHTML="";
    data.forEach((d,i)=>{{
      const y=mode==="scale"?d.sy:d.uy,h=mode==="scale"?d.sh:d.uh;
      let rx=margin.left,rw=plotW;
      if(mode==="scale"&&d.ncols>1){{const cw=plotW/d.ncols;rx=margin.left+d.col*cw;rw=cw}}
      const g=document.createElementNS("http://www.w3.org/2000/svg","g");g.dataset.idx=i;
      const rect=document.createElementNS("http://www.w3.org/2000/svg","rect");
      Object.entries({{x:rx,y,width:rw,height:h,fill:d.color,stroke:"black","stroke-width":.5}}).forEach(([k,v])=>rect.setAttribute(k,v));
      g.appendChild(rect);
      const show=mode==="uniform"||(h>=14&&rw>=d.name.length*6);
      if(show){{
        const tc=lum(d.color)>.45?"#222":"#fff";
        const txt=document.createElementNS("http://www.w3.org/2000/svg","text");
        txt.setAttribute("x",rx+rw/2);txt.setAttribute("y",y+h/2+4);txt.setAttribute("text-anchor","middle");
        txt.setAttribute("font-weight","bold");txt.setAttribute("font-size","10");txt.setAttribute("fill",tc);
        txt.setAttribute("stroke",d.color);txt.setAttribute("stroke-width","3");txt.setAttribute("paint-order","stroke");
        txt.textContent=d.name;g.appendChild(txt);
      }}
      if(show&&d.gds!=null&&mode==="uniform"){{
        const gt=document.createElementNS("http://www.w3.org/2000/svg","text");
        gt.setAttribute("x",rx+rw+8);gt.setAttribute("y",y+h/2+4);gt.setAttribute("font-size","9");gt.setAttribute("fill","#888");
        gt.textContent="L"+d.gds;g.appendChild(gt);
      }}
      gL.appendChild(g);
    }});
  }}
  gL.addEventListener("mousemove",e=>{{
    const g=e.target.closest("g[data-idx]");if(!g){{tip.style.display="none";return}}
    const d=data[+g.dataset.idx];
    tip.innerHTML=`<b>${{d.name}}</b><br>GDS: ${{d.gds??"N/A"}}<br>Material: ${{d.material}}<br>Type: ${{d.type}}<br>z: ${{d.zmin}}–${{d.zmax}} µm<br>Thickness: ${{d.thickness}} µm`;
    const r=root.getBoundingClientRect();tip.style.display="block";
    tip.style.left=(e.clientX-r.left+12)+"px";tip.style.top=(e.clientY-r.top+12)+"px";
  }});
  gL.addEventListener("mouseleave",()=>tip.style.display="none");
  root.querySelectorAll(".sv-btn").forEach(btn=>{{
    btn.addEventListener("click",()=>{{
      mode=btn.dataset.mode;root.querySelectorAll(".sv-btn").forEach(b=>b.style.background="#fff");
      btn.style.background="#e0e0e0";render();
    }});
  }});
  render();
  (function(svg){{
    const W=+svg.getAttribute("width"),H=+svg.getAttribute("height");
    let vb={{x:0,y:0,w:W,h:H}};svg.setAttribute("viewBox",`${{vb.x}} ${{vb.y}} ${{vb.w}} ${{vb.h}}`);
    svg.addEventListener("wheel",function(e){{if(!e.ctrlKey)return;e.preventDefault();
      const f=e.deltaY>0?1.12:1/1.12,pt=sp(e);vb.x=pt.x-(pt.x-vb.x)*f;vb.y=pt.y-(pt.y-vb.y)*f;vb.w*=f;vb.h*=f;av()}},{{passive:false}});
    let dr=null;
    svg.addEventListener("mousedown",function(e){{if(e.button!==0)return;dr={{sx:e.clientX,sy:e.clientY,vx:vb.x,vy:vb.y}};svg.style.cursor="grabbing"}});
    window.addEventListener("mousemove",function(e){{if(!dr)return;const s=vb.w/W;vb.x=dr.vx-(e.clientX-dr.sx)*s;vb.y=dr.vy-(e.clientY-dr.sy)*s;av()}});
    window.addEventListener("mouseup",function(){{dr=null;svg.style.cursor=""}});
    svg.addEventListener("dblclick",function(){{vb={{x:0,y:0,w:W,h:H}};av()}});
    function av(){{svg.setAttribute("viewBox",`${{vb.x}} ${{vb.y}} ${{vb.w}} ${{vb.h}}`)}}
    function sp(e){{const r=svg.getBoundingClientRect();return{{x:vb.x+(e.clientX-r.left)/r.width*vb.w,y:vb.y+(e.clientY-r.top)/r.height*vb.h}}}}
  }})(svg);
}})();
</script>'''


def _render_cross_sections(cross_sections, layer_stack, svg_id, svg_w=1000, svg_h=550):
    if not cross_sections:
        return ""
    margin_l, margin_r, margin_t, margin_b = 60, 20, 40, 70
    plot_w = svg_w - margin_l - margin_r
    plot_h = svg_h - margin_t - margin_b

    box_t = getattr(layer_stack, "box_thickness", 2.0) or 2.0
    all_z = [-box_t, 0.0]
    clad_top = 0.0
    for name, level in layer_stack.layers.items():
        zmin = getattr(level, "zmin", 0) or 0
        thickness = getattr(level, "thickness", 0) or 0
        all_z.extend([zmin, zmin + thickness])
        if "clad" in name.lower():
            clad_top = max(clad_top, zmin + thickness)
    for xs in cross_sections:
        for layer in xs["layers"]:
            all_z.extend([layer["zmin"], layer["zmax"]])

    z_min_g = min(all_z)
    z_max_g = max(all_z)
    z_range = (z_max_g - z_min_g) or 1.0

    def z2y(z):
        return margin_t + plot_h - (z - z_min_g) / z_range * plot_h

    n_xs = len(cross_sections)
    col_w = plot_w / max(n_xs, 1)

    parts = []
    parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{svg_w}" height="{svg_h}" font-family="system-ui,sans-serif" font-size="11">')
    parts.append(f'<rect width="{svg_w}" height="{svg_h}" fill="white"/>')
    parts.append(f'<text x="{svg_w//2}" y="24" text-anchor="middle" font-size="14" font-weight="bold">PDK Cross-Sections</text>')

    step = _nice_step(z_range, 8)
    z = math.floor(z_min_g / step) * step
    while z <= z_max_g + step * 0.5:
        y = z2y(z)
        parts.append(f'<line x1="{margin_l}" y1="{y:.1f}" x2="{svg_w-margin_r}" y2="{y:.1f}" stroke="#EEE" stroke-width="1"/>')
        parts.append(f'<text x="{margin_l-6}" y="{y+4:.1f}" text-anchor="end" font-size="9" fill="#666">{z:.2f}</text>')
        z += step

    all_data = []
    idx = 0
    for i, xs in enumerate(cross_sections):
        cx = margin_l + i * col_w + 0.7
        cxe = cx + col_w - 1.4
        inner_w = col_w - 2 * 6.0
        center = cx + (col_w - 1.4) / 2

        # Cladding background
        cy_top = z2y(clad_top) if clad_top > 0 else z2y(z_max_g)
        cy_bot = z2y(0)
        parts.append(f'<g data-idx="{idx}"><rect x="{cx:.1f}" y="{cy_top:.1f}" width="{col_w-1.4:.1f}" height="{cy_bot-cy_top:.1f}" fill="#FFF8DC" opacity="0.6"/></g>')
        all_data.append({"name": "Cladding", "material": "SiO2", "zmin": 0, "zmax": round(clad_top, 3), "thickness": round(clad_top, 3), "gds": None})
        idx += 1

        # Substrate background
        sy_top = z2y(0)
        sy_bot = z2y(-box_t)
        parts.append(f'<g data-idx="{idx}"><rect x="{cx:.1f}" y="{sy_top:.1f}" width="{col_w-1.4:.1f}" height="{sy_bot-sy_top:.1f}" fill="#C0C0C0" opacity="0.5"/></g>')
        all_data.append({"name": "Substrate", "material": "Si", "zmin": round(-box_t, 3), "zmax": 0, "thickness": round(box_t, 3), "gds": None})
        idx += 1

        # Column borders
        bt = min(cy_top, margin_t)
        bb = max(sy_bot, margin_t + plot_h)
        parts.append(f'<line x1="{cx:.1f}" y1="{bt:.1f}" x2="{cx:.1f}" y2="{bb:.1f}" stroke="#CCC" stroke-width="1" stroke-dasharray="3,3"/>')
        parts.append(f'<line x1="{cxe:.1f}" y1="{bt:.1f}" x2="{cxe:.1f}" y2="{bb:.1f}" stroke="#CCC" stroke-width="1" stroke-dasharray="3,3"/>')

        # Layers
        for layer in xs["layers"]:
            yt = z2y(layer["zmax"])
            yb = z2y(layer["zmin"])
            h = max(yb - yt, 2)
            wf = min(layer["width"] / 20.0, 1.0)
            rw = inner_w * wf
            rx = center - rw / 2
            color = _color_for_xs(layer["material"])
            parts.append(f'<g data-idx="{idx}"><rect x="{rx:.1f}" y="{yt:.1f}" width="{rw:.1f}" height="{h:.1f}" fill="{color}" stroke="#444" stroke-width="0.5"/></g>')
            all_data.append(layer)
            idx += 1

        # Label
        ly = margin_t + plot_h + 15
        parts.append(f'<text x="{center:.0f}" y="{ly}" text-anchor="middle" font-size="10" font-weight="bold">{xs["name"]}</text>')

    parts.append(f'<text x="12" y="{(margin_t+plot_h)//2}" text-anchor="middle" font-size="11" transform="rotate(-90,12,{(margin_t+plot_h)//2})">Z (µm)</text>')
    parts.append('</svg>')
    svg_html = "\n".join(parts)
    dj = json.dumps(all_data, separators=(",", ": "))

    return f'''<div id="{svg_id}" style="position:relative;display:inline-block;font-family:system-ui,sans-serif">
  {svg_html}
  <div class="tooltip" style="display:none;position:absolute;background:white;color:#222;border:1px solid #ccc;border-radius:4px;padding:6px 10px;font-size:11px;pointer-events:none;box-shadow:0 2px 6px rgba(0,0,0,.15);z-index:10;white-space:nowrap"></div>
</div>
<script>
(function(){{
  const root=document.getElementById("{svg_id}"),tip=root.querySelector(".tooltip"),data={dj};
  root.querySelector("svg").addEventListener("mousemove",e=>{{
    const g=e.target.closest("g[data-idx]");if(!g){{tip.style.display="none";return}}
    const d=data[+g.dataset.idx];
    tip.innerHTML=`<b>${{d.name}}</b><br>Material: ${{d.material}}${{d.width!=null?`<br>Width: ${{d.width}} µm`:""}}<br>GDS: ${{d.gds??"N/A"}}<br>z: ${{d.zmin}}–${{d.zmax}} µm<br>Thickness: ${{d.thickness}} µm`;
    const r=root.getBoundingClientRect();tip.style.display="block";
    tip.style.left=(e.clientX-r.left+12)+"px";tip.style.top=(e.clientY-r.top+12)+"px";
  }});
  root.querySelector("svg").addEventListener("mouseleave",()=>tip.style.display="none");
  (function(svg){{
    const W=+svg.getAttribute("width"),H=+svg.getAttribute("height");
    let vb={{x:0,y:0,w:W,h:H}};svg.setAttribute("viewBox",`${{vb.x}} ${{vb.y}} ${{vb.w}} ${{vb.h}}`);
    svg.addEventListener("wheel",function(e){{if(!e.ctrlKey)return;e.preventDefault();
      const f=e.deltaY>0?1.12:1/1.12,pt=sp(e);vb.x=pt.x-(pt.x-vb.x)*f;vb.y=pt.y-(pt.y-vb.y)*f;vb.w*=f;vb.h*=f;av()}},{{passive:false}});
    let dr=null;
    svg.addEventListener("mousedown",function(e){{if(e.button!==0)return;dr={{sx:e.clientX,sy:e.clientY,vx:vb.x,vy:vb.y}};svg.style.cursor="grabbing"}});
    window.addEventListener("mousemove",function(e){{if(!dr)return;const s=vb.w/W;vb.x=dr.vx-(e.clientX-dr.sx)*s;vb.y=dr.vy-(e.clientY-dr.sy)*s;av()}});
    window.addEventListener("mouseup",function(){{dr=null;svg.style.cursor=""}});
    svg.addEventListener("dblclick",function(){{vb={{x:0,y:0,w:W,h:H}};av()}});
    function av(){{svg.setAttribute("viewBox",`${{vb.x}} ${{vb.y}} ${{vb.w}} ${{vb.h}}`)}}
    function sp(e){{const r=svg.getBoundingClientRect();return{{x:vb.x+(e.clientX-r.left)/r.width*vb.w,y:vb.y+(e.clientY-r.top)/r.height*vb.h}}}}
  }})(root.querySelector("svg"));
}})();
</script>'''


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

CSS = '''<style>
  .layer-stack-viz .section { margin-bottom: 32px; }
  .layer-stack-viz .section h2 {
    font-size: 15px; color: #555; margin-bottom: 10px;
    border-bottom: 1px solid #ddd; padding-bottom: 4px;
  }
  .layer-stack-viz .viz-container {
    background: white; border: 1px solid #e0e0e0; border-radius: 6px;
    padding: 12px; display: inline-block;
  }
</style>'''



def main():
    filepath = PATH.repo / "docs" / "layer_stack.md"
    filepath.parent.mkdir(parents=True, exist_ok=True)

    parts = ["# Layer Stack\n"]
    parts.append("Interactive layer stack and cross-section visualizations. "
                 "Hover for details, Ctrl+scroll to zoom, drag to pan, double-click to reset.\n")

    for band_label, pdk in BANDS:
        pdk.activate()
        ls = getattr(pdk, "layer_stack", None)
        if ls is None:
            print(f"  Skipping {band_label or 'default'}: no layer_stack")
            continue

        if band_label:
            parts.append(f"\n## {band_label}\n")

        parts.append(CSS)
        parts.append('\n<div class="layer-stack-viz">')

        layers = _extract_layers(ls)
        layers, ticks = _compute_layout(layers)
        if layers:
            sid = _next_id()
            parts.append('<div class="section">')
            parts.append('  <h2>Layer Stack</h2>')
            parts.append(f'  <div class="viz-container">{_render_layer_stack(layers, ticks, sid)}</div>')
            parts.append('</div>')

        xs = _extract_cross_sections(pdk, ls)
        if xs:
            sid = _next_id()
            parts.append('<div class="section">')
            parts.append('  <h2>Cross-Sections</h2>')
            parts.append(f'  <div class="viz-container">{_render_cross_sections(xs, ls, sid)}</div>')
            parts.append('</div>')

        parts.append('</div>')

    content = "\n".join(parts) + "\n"
    filepath.write_text(content)
    print(f"Wrote {filepath}")


if __name__ == "__main__":
    main()
