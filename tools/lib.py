from PIL import Image
import os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=ROOT+'/assets/paycheck/'; B=ROOT+'/assets/budget/'
def sz(p): return Image.open(p).size
def h(p,w): a,b=sz(p); return round(w*b/a)
FONTS='''@font-face{font-family:L;src:url(file:///usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf);font-weight:400 700}
@font-face{font-family:L;font-style:italic;src:url(file:///usr/share/fonts/truetype/google-fonts/Lora-Italic-Variable.ttf);font-weight:400 700}
@font-face{font-family:P;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf);font-weight:700}
@font-face{font-family:P;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf);font-weight:500}
*{box-sizing:border-box}body{margin:0}
.c{position:relative;width:1080px;height:1350px;overflow:hidden;font-family:P}
.a{position:absolute}'''
SH='box-shadow:0 40px 70px -30px rgba(0,0,0,.55)'
def img(p,x,y,w,rot=0,r=22,z=3,extra=''):
    return f'<img class="a" src="file://{p}" style="left:{x}px;top:{y}px;width:{w}px;height:{h(p,w)}px;border-radius:{r}px;transform:rotate({rot}deg);z-index:{z};{SH};{extra}">'
def phone(p,x,y,w,rot=0,z=4,frame='#111827'):
    hh=round(w*2.12)
    return f'<div class="a" style="left:{x}px;top:{y}px;width:{w}px;height:{hh}px;background:{frame};border-radius:{round(w*.17)}px;padding:10px;transform:rotate({rot}deg);z-index:{z};{SH}"><img src="file://{p}" style="width:100%;height:100%;object-fit:cover;object-position:top;border-radius:{round(w*.13)}px;display:block"></div>'
def lap(p,x,y,w,z=2,frame='#1A2233'):
    hh=round(w*.625)
    return f'<div class="a" style="left:{x}px;top:{y}px;width:{w}px;z-index:{z}"><div style="background:{frame};border-radius:16px 16px 6px 6px;padding:11px 11px 13px;{SH}"><img src="file://{p}" style="display:block;width:100%;height:{hh}px;object-fit:cover;object-position:top left;border-radius:5px"></div><div style="height:13px;margin:0 -30px;background:linear-gradient(#D9D6CC,#B5B0A2);border-radius:0 0 20px 20px"></div></div>'
BAG='<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 7h12l1 13H5z"/><path d="M9 7a3 3 0 0 1 6 0"/></svg>'
def cta(bg,fg,label,y=1196,sub='#'):
    return f'''<div class="a" style="left:60px;right:60px;top:{y}px;height:104px;border-radius:26px;background:{bg};color:{fg};display:flex;align-items:center;justify-content:center;gap:20px;z-index:9;box-shadow:0 24px 40px -24px rgba(0,0,0,.5)">{BAG}<div style="text-align:left"><div style="font-size:18px;font-weight:500;letter-spacing:.18em;opacity:.85">{label}</div><div style="font-size:34px;font-weight:700;letter-spacing:-.01em;line-height:40px">etsy.com/shop/MethodNMargins</div></div></div>'''
def brand(color,y=48):
    return f'<div class="a" style="left:0;right:0;top:{y}px;text-align:center;font-size:18px;font-weight:700;letter-spacing:.34em;color:{color};z-index:9">METHOD &amp; MARGIN</div>'
def check(c,fg='#fff',s=34):
    return f'<span style="width:{s}px;height:{s}px;border-radius:50%;background:{c};display:inline-flex;align-items:center;justify-content:center;flex:none"><svg width="{s*.55}" height="{s*.55}" viewBox="0 0 24 24" fill="none" stroke="{fg}" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7"/></svg></span>'
def page(body): return f'<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}</style></head><body><div class="c" id="c">{body}</div></body></html>'

# ---- palettes
NV='#13264A'; GOLD='#E2B85C'; CRM='#F6F1E6'            # Paycheck Planner (navy + gold)
BG='#F4EEDD'; G='#2F571B'; GD='#1E3A14'; LIME='#C8E3A8'; INK='#1B2617'; CL='#B8682F'   # Budget Planner (green + cream)
def render(posts, outdir=ROOT+'/posts', srcdir=ROOT+'/src'):
    """posts: dict name->html. Writes src/name.html and posts/name.jpg (2160x2700)."""
    from playwright.sync_api import sync_playwright
    from PIL import Image as I
    out=[]
    with sync_playwright() as p:
        b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox','--allow-file-access-from-files'])
        pg=b.new_page(device_scale_factor=2,viewport={'width':1080,'height':1350})
        for k,v in posts.items():
            f=f'{srcdir}/{k}.html'; open(f,'w').write(v)
            pg.goto('file://'+f); pg.wait_for_timeout(600)
            png=f'/tmp/{k}.png'; pg.locator('#c').screenshot(path=png)
            jpg=f'{outdir}/{k}.jpg'; I.open(png).convert('RGB').save(jpg,quality=92,optimize=True); out.append(jpg)
        b.close()
    return out
