import sys,os; sys.path.insert(0,os.path.dirname(__file__))
from lib import *
def tag(x,y,t,bg,fg,ic,z=7):
    return f'<div class="a" style="left:{x}px;top:{y}px;z-index:{z};display:flex;align-items:center;gap:12px;background:{bg};color:{fg};border-radius:18px;padding:14px 22px 14px 14px;font-size:23px;font-weight:700;box-shadow:0 18px 30px -16px rgba(0,0,0,.5)">{check(ic,bg,32)}{t}</div>'
def crop(p,x,y,w,cx,cy,cw,ch,r=26,z=4,rot=0):
    """show region (cx,cy,cw,ch) of image p (original px) scaled to width w"""
    W,H=sz(p); s=w/cw; hh=round(ch*s)
    return f'<div class="a" style="left:{x}px;top:{y}px;width:{w}px;height:{hh}px;border-radius:{r}px;overflow:hidden;z-index:{z};transform:rotate({rot}deg);{SH};background:url(file://{p}) no-repeat;background-size:{round(W*s)}px {round(H*s)}px;background-position:-{round(cx*s)}px -{round(cy*s)}px"></div>'
pillsty='border-radius:999px;padding:10px 24px;font-size:20px;font-weight:700;letter-spacing:.16em;display:inline-block'
posts={}

# 12:00 — Paycheck: question post, cropped "Where this paycheck goes" breakdown (cream)
chip=lambda t,dot: f'<span style="display:inline-flex;align-items:center;gap:12px;background:#fff;color:{NV};border-radius:999px;padding:14px 26px;font-size:26px;font-weight:700;box-shadow:0 14px 24px -16px rgba(0,0,0,.4)"><span style="width:18px;height:18px;border-radius:50%;background:{dot}"></span>{t}</span>'
posts['2026-11-27-paycheck-where-it-goes']=page(f'''<div class="a" style="inset:0;background:{CRM}"></div>
<div class="a" style="right:-200px;top:-160px;width:620px;height:620px;border-radius:50%;background:#ECE3CF"></div>
{brand('#5A5F6B')}
<div class="a" style="left:70px;top:120px;width:940px;z-index:5;color:#141B2D">
 <div style="{pillsty};background:{NV};color:#fff">ADHD PAYCHECK PLANNER</div>
 <div style="font-family:L;font-weight:700;font-size:96px;line-height:102px;letter-spacing:-.02em;margin-top:26px">Where did my</div>
 <div style="font-family:L;font-style:italic;font-weight:600;font-size:100px;line-height:108px;color:#B8862F;letter-spacing:-.02em">paycheck go?</div>
 <div style="font-size:29px;line-height:40px;font-weight:500;color:#4A4F5C;margin-top:16px">See where every dollar goes, before you spend it.</div>
</div>
{crop(P+'d-paycheck.png',60,530,960,545,725,2290,890,z=4)}
<div class="a" style="left:0;right:0;top:950px;text-align:center;z-index:6"><span style="display:inline-block;background:{GOLD};color:{NV};border-radius:20px;padding:18px 34px;font-family:L;font-style:italic;font-weight:700;font-size:40px;transform:rotate(-2deg);box-shadow:0 18px 30px -16px rgba(0,0,0,.5)">Every dollar gets a job.</span></div>
{cta(NV,'#fff','ADHD PAYCHECK PLANNER · SHOP NOW')}''')

# 14:00 — Budget: weekly check-in, 4-step progress + card (clay/cream)
seg=''.join(f'<div style="flex:1;text-align:center"><div style="height:16px;border-radius:8px;background:{G if i==0 else "#E3D9BF"}"></div><div style="margin-top:12px;font-size:24px;font-weight:700;color:{G if i==0 else "#8A8470"}">Step {i+1}</div></div>' for i in range(4))
posts['2026-11-27-budget-checkin']=page(f'''<div class="a" style="inset:0;background:{BG}"></div>
<div class="a" style="left:-220px;bottom:-260px;width:760px;height:760px;border-radius:50%;background:#EADFC4"></div>
{brand('#6B5A3E')}
<div class="a" style="left:60px;right:60px;top:120px;text-align:center;z-index:5;color:{INK}">
 <div style="{pillsty};background:{G};color:#fff">ADHD BUDGET PLANNER</div>
 <div style="font-family:L;font-weight:700;font-size:92px;line-height:98px;letter-spacing:-.02em;margin-top:26px">Your weekly money</div>
 <div style="font-family:L;font-style:italic;font-weight:600;font-size:96px;line-height:104px;color:{CL};letter-spacing:-.02em">check-in.</div>
 <div style="font-size:29px;line-height:40px;font-weight:500;color:#4D4A3C;margin-top:16px">4 short steps. About 2 minutes. Then you’re done.</div>
</div>
{img(B+'s-checkin.png',110,630,860,r=28,z=4)}
<div class="a" style="left:50px;top:480px;z-index:6;width:170px;height:170px;border-radius:50%;background:{CL};color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(-8deg);box-shadow:0 20px 34px -18px rgba(0,0,0,.6)"><div style="font-family:L;font-weight:700;font-size:52px;line-height:54px">~2</div><div style="font-size:22px;font-weight:700;letter-spacing:.12em">MIN</div></div>
{cta(GD,'#fff','ADHD BUDGET PLANNER · SHOP NOW')}''')

# 17:00 — Paycheck: myth vs fact, catch up (navy)
posts['2026-11-27-paycheck-catch-up']=page(f'''<div class="a" style="inset:0;background:linear-gradient(160deg,#1B3766,{NV} 65%)"></div>
{brand('#AFC0DD')}
<div class="a" style="left:70px;top:120px;width:940px;z-index:5;color:#fff">
 <div style="{pillsty};background:{GOLD};color:{NV}">ADHD PAYCHECK PLANNER</div>
 <div style="font-family:L;font-weight:700;font-size:92px;line-height:98px;letter-spacing:-.02em;margin-top:26px">Missed a few days?</div>
 <div style="font-family:L;font-style:italic;font-weight:600;font-size:96px;line-height:104px;color:{GOLD};letter-spacing:-.02em">That’s normal.</div>
</div>
<div class="a" style="left:70px;top:470px;width:500px;z-index:5;color:#fff">
 <div style="background:rgba(255,255,255,.08);border:2px solid rgba(255,255,255,.18);border-radius:26px;padding:28px 30px">
  <div style="font-size:22px;font-weight:700;letter-spacing:.2em;color:#E89A8C">MYTH</div>
  <div style="font-family:L;font-size:38px;line-height:48px;font-weight:600;margin-top:10px;color:#D5DEEE;text-decoration:line-through;text-decoration-color:rgba(232,154,140,.8);text-decoration-thickness:3px">Skipped logging = budget ruined.</div>
 </div>
 <div style="background:{GOLD};color:{NV};border-radius:26px;padding:28px 30px;margin-top:24px;box-shadow:0 24px 40px -22px rgba(0,0,0,.6)">
  <div style="font-size:22px;font-weight:700;letter-spacing:.2em">FACT</div>
  <div style="font-family:L;font-size:38px;line-height:48px;font-weight:700;margin-top:10px">A rough total per category is enough. Fix it later.</div>
 </div>
 <div style="margin-top:26px;font-size:27px;line-height:38px;font-weight:500;color:#D5DEEE">“Catch up” fills the gap in one go.</div>
</div>
{img(P+'s-catchup.png',600,470,430,rot=3,r=26,z=4)}
{cta(GOLD,NV,'ADHD PAYCHECK PLANNER · SHOP NOW')}''')

# 19:00 — Budget: make it yours, themes + accessibility (light, two phones + look card)
c2=lambda t: f'<span style="background:#fff;color:{GD};border:2px solid #C9D8B4;border-radius:999px;padding:12px 22px;font-size:24px;font-weight:700">{t}</span>'
posts['2026-11-27-budget-make-it-yours']=page(f'''<div class="a" style="inset:0;background:#EEF0E6"></div>
{brand('#4A5641')}
<div class="a" style="left:60px;right:60px;top:110px;text-align:center;z-index:5;color:{INK}">
 <div style="{pillsty};background:{G};color:#fff">ADHD BUDGET PLANNER</div>
 <div style="font-family:L;font-weight:700;font-size:96px;line-height:102px;letter-spacing:-.02em;margin-top:24px">Make it look</div>
 <div style="font-family:L;font-style:italic;font-weight:600;font-size:100px;line-height:108px;color:{G};letter-spacing:-.02em">like yours.</div>
</div>
{phone(B+'p-th-plum.png',105,470,230,rot=-6,z=3,frame='#2A1B33')}
{phone(B+'p-th-cocoa-dark.png',745,470,230,rot=6,z=3,frame='#1C1410')}
{img(B+'e-look.png',300,560,480,r=24,z=5)}
<div class="a" style="left:60px;right:60px;top:1000px;display:flex;flex-wrap:wrap;justify-content:center;gap:12px;z-index:6">{c2('7 themes')}{c2('Dark mode')}{c2('Bigger text')}{c2('Easier-to-read font')}{c2('Higher contrast')}{c2('Calm animations')}</div>
{cta(GD,'#fff','ADHD BUDGET PLANNER · SHOP NOW')}''')

if __name__=='__main__': print(render(posts))
