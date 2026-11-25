import sys,os; sys.path.insert(0,os.path.dirname(__file__))
from lib import *
posts={}

# ---------- 1  Paycheck hook (navy)
NV='#13264A'; GOLD='#E2B85C'; CRM='#F6F1E6'
posts['2026-11-26-paycheck-hook']=page(f'''<div class="a" style="inset:0;background:radial-gradient(circle at 50% 30%,#21407A,{NV} 70%)"></div>
<div class="a" style="left:-120px;top:780px;width:520px;height:520px;border-radius:50%;background:rgba(226,184,92,.10)"></div>
{brand('#AFC0DD')}
<div class="a" style="left:60px;right:60px;top:118px;text-align:center;color:#fff;z-index:5">
 <div style="font-family:L;font-weight:700;font-size:104px;line-height:104px;letter-spacing:-.02em">Got paid Friday.</div>
 <div style="font-family:L;font-style:italic;font-weight:600;font-size:110px;line-height:118px;color:{GOLD};letter-spacing:-.02em">Broke by Monday?</div>
 <div style="font-size:32px;line-height:44px;font-weight:500;color:#D5DEEE;margin-top:22px">See exactly what’s safe to spend<br>until your next payday.</div>
</div>
{img(P+'e-hero.png',70,560,700,rot=-3,r=26,z=4)}
{phone(P+'p-bills.png',740,520,270,rot=5,z=5,frame='#0B1428')}
<div class="a" style="left:96px;top:1000px;z-index:6;display:flex;gap:12px">
 <span style="background:{GOLD};color:{NV};border-radius:999px;padding:12px 22px;font-size:22px;font-weight:700">Built for ADHD brains</span>
 <span style="background:rgba(255,255,255,.12);color:#fff;border-radius:999px;padding:12px 22px;font-size:22px;font-weight:700;border:1.5px solid rgba(255,255,255,.3)">Free demo</span>
</div>
{cta(GOLD,NV,'ADHD PAYCHECK PLANNER · SHOP NOW')}''')
# ---------- 2  Budget one number (cream / green)
BG='#F4EEDD'; G='#2F571B'; GD='#1E3A14'; LIME='#C8E3A8'; INK='#1B2617'
chip=lambda t: f'<div style="display:flex;align-items:center;gap:12px;background:#FFFDF6;border:1.5px solid #DCD0AE;border-radius:999px;padding:12px 22px 12px 12px;font-size:23px;font-weight:700;color:{INK}">{check(G,LIME,32)}{t}</div>'
posts['2026-11-27-budget-one-number']=page(f'''<div class="a" style="inset:0;background:{BG}"></div>
<div class="a" style="left:640px;top:-160px;width:620px;height:620px;border-radius:50%;background:#E9DFC2"></div>
{brand('#4A5641')}
<div class="a" style="left:60px;right:60px;top:110px;text-align:center;color:{INK};z-index:5">
 <div style="display:inline-block;background:{G};color:#fff;border-radius:999px;padding:10px 24px;font-size:20px;font-weight:700;letter-spacing:.16em">ADHD BUDGET PLANNER</div>
 <div style="font-family:L;font-weight:700;font-size:100px;line-height:100px;letter-spacing:-.02em;margin-top:26px">Your whole budget.</div>
 <div style="font-family:L;font-style:italic;font-weight:600;font-size:104px;line-height:112px;color:{G};letter-spacing:-.02em">One number.</div>
 <div style="font-size:30px;line-height:42px;font-weight:500;color:#3A4632;margin-top:18px">Open it. See what’s safe to spend today. Done.</div>
</div>
<div class="a" style="left:60px;right:60px;top:540px;height:630px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:44px;z-index:5"><img src="file://{B}e-hero.png" style="width:940px;border-radius:30px;{SH}"><div style="display:flex;flex-wrap:wrap;justify-content:center;gap:14px;max-width:900px">{chip('Bills already set aside')}{chip('Updates as you spend')}{chip('No spreadsheets')}</div></div>
{cta(GD,'#fff','ADHD BUDGET PLANNER · SHOP NOW')}''')
# ---------- 3  Impulse (clay accent)
CL='#B8682F'
posts['2026-11-29-budget-impulse']=page(f'''<div class="a" style="inset:0;background:#F3E7D6"></div>
<div class="a" style="left:-200px;top:520px;width:700px;height:700px;border-radius:50%;background:#EBD9BF"></div>
{brand('#7A5A3C')}
<div class="a" style="left:60px;top:110px;width:960px;color:{INK};z-index:5">
 <div style="font-size:30px;font-weight:700;color:{CL};letter-spacing:.04em">YOUR ADHD BRAIN:</div>
 <div style="font-family:L;font-weight:700;font-size:96px;line-height:100px;letter-spacing:-.02em">“Add to cart.”</div>
 <div style="font-size:30px;font-weight:700;color:{G};letter-spacing:.04em;margin-top:22px">THIS APP:</div>
 <div style="font-family:L;font-style:italic;font-weight:600;font-size:96px;line-height:104px;color:{G};letter-spacing:-.02em">“Let’s check first.”</div>
</div>
{img(B+'s-cooloff.png',60,640,560,rot=-4,r=24,z=3)}
{img(B+'s-afford.png',480,540,520,rot=3,r=24,z=4)}
<div class="a" style="left:70px;top:{640+h(B+'s-cooloff.png',560)+20}px;z-index:6;background:{CL};color:#fff;border-radius:18px;padding:14px 22px;font-size:22px;line-height:30px;font-weight:700;max-width:420px">Not sure? Park it on the<br>cool-off list for 48 hours.</div>
{cta(GD,'#fff','ADHD BUDGET PLANNER · SHOP NOW')}''')
# ---------- 3  Paycheck next steps
posts['2026-11-28-paycheck-next-3']=page(f'''<div class="a" style="inset:0;background:{CRM}"></div>
<div class="a" style="left:700px;top:-180px;width:600px;height:600px;border-radius:50%;background:#E9E1CF"></div>
{brand('#5A5F6B')}
<div class="a" style="left:60px;right:60px;top:108px;text-align:center;color:#141B2D;z-index:5">
 <div style="display:inline-block;background:{NV};color:#fff;border-radius:999px;padding:10px 24px;font-size:20px;font-weight:700;letter-spacing:.16em">ADHD PAYCHECK PLANNER</div>
 <div style="font-family:L;font-weight:700;font-size:84px;line-height:94px;letter-spacing:-.025em;margin-top:26px">Money stuff piling up?</div>
 <div style="font-family:L;font-style:italic;font-weight:600;font-size:100px;line-height:110px;color:#B8862F;letter-spacing:-.02em">Just do these 3.</div>
 <div style="font-size:30px;line-height:42px;font-weight:500;color:#4A4F5C;margin-top:16px">It picks what matters right now, so your brain doesn’t have to.</div>
</div>
{img(P+'e-now.png',40,560,1000,r=26,z=4)}
<div class="a" style="left:60px;right:60px;top:{560+h(P+'e-now.png',1000)+70}px;display:flex;justify-content:center;gap:16px;z-index:5">
{''.join(f'<div style="background:{NV};color:#fff;border-radius:20px;padding:18px 24px;text-align:center;width:300px"><div style="font-family:L;font-weight:700;font-size:44px;color:{GOLD};line-height:48px">{n}</div><div style="font-size:21px;font-weight:700;margin-top:4px">{d}</div></div>' for n,d in [('3','next steps only'),('1','tap to mark paid'),('0','spreadsheets')])}
</div>
{cta(NV,'#fff','ADHD PAYCHECK PLANNER · SHOP NOW')}''')
# ---------- 5  Trust / pay once
row=lambda t: f'<div style="display:flex;align-items:center;gap:20px;font-family:L;font-weight:700;font-size:70px;line-height:84px;color:#fff;letter-spacing:-.02em">{check(GOLD,NV,58)}{t}</div>'
posts['2026-11-30-paycheck-pay-once']=page(f'''<div class="a" style="inset:0;background:linear-gradient(160deg,#16305C,#0E1D38)"></div>
{brand('#AFC0DD')}
<div class="a" style="left:80px;top:120px;z-index:5;display:flex;flex-direction:column;gap:6px">{row('No subscription.')}{row('No account.')}{row('No bank login.')}</div>
<div class="a" style="left:80px;top:420px;z-index:5;font-family:L;font-style:italic;font-weight:600;font-size:64px;color:{GOLD}">Pay once. Keep it.</div>
<div class="a" style="left:80px;top:510px;z-index:5;font-size:28px;line-height:40px;font-weight:500;color:#D5DEEE;width:900px">A private budgeting app that works offline in your browser. Your money data stays on your device.</div>
{lap(P+'d-home.png',80,680,720,z=3,frame='#0A1122')}
{phone(P+'p-spending.png',770,690,230,rot=4,z=4,frame='#0A1122')}
<div class="a" style="left:630px;top:600px;z-index:6;width:170px;height:170px;border-radius:50%;background:{CL};color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(10deg);outline:2px dashed #F6D8B8;outline-offset:-10px;box-shadow:0 20px 36px -16px rgba(0,0,0,.6)"><span style="font-size:15px;font-weight:700;letter-spacing:.16em">TRY A</span><span style="font-family:L;font-style:italic;font-weight:600;font-size:46px;line-height:50px">Free</span><span style="font-size:15px;font-weight:700;letter-spacing:.16em">DEMO</span></div>
{cta(GOLD,NV,'ADHD PAYCHECK PLANNER · SHOP NOW')}''')


if __name__=='__main__': print(render(posts))
