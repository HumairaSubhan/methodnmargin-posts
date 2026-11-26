import sys,os; sys.path.insert(0,os.path.dirname(__file__))
from lib import *
def crop(p,x,y,w,cx,cy,cw,ch,r=26,z=4,rot=0):
    W,H=sz(p); s=w/cw; hh=round(ch*s)
    return f'<div class="a" style="left:{x}px;top:{y}px;width:{w}px;height:{hh}px;border-radius:{r}px;overflow:hidden;z-index:{z};transform:rotate({rot}deg);{SH};background:url(file://{p}) no-repeat;background-size:{round(W*s)}px {round(H*s)}px;background-position:-{round(cx*s)}px -{round(cy*s)}px"></div>'
pillsty='border-radius:999px;padding:10px 24px;font-size:20px;font-weight:700;letter-spacing:.16em;display:inline-block'
posts={}

# 10:00 — Budget: set aside first, single feature close-up (cream, big tilted card + lime sticker)
posts['2026-11-28-budget-set-aside']=page(f'''<div class="a" style="inset:0;background:{BG}"></div>
<div class="a" style="right:-240px;top:380px;width:760px;height:760px;border-radius:50%;background:#E6EDCF"></div>
{brand('#6B5A3E')}
<div class="a" style="left:70px;top:120px;width:940px;z-index:5;color:{INK}">
 <div style="{pillsty};background:{G};color:#fff">ADHD BUDGET PLANNER</div>
 <div style="font-family:L;font-weight:700;font-size:96px;line-height:102px;letter-spacing:-.02em;margin-top:26px">Pay future-you</div>
 <div style="font-family:L;font-style:italic;font-weight:600;font-size:100px;line-height:108px;color:{G};letter-spacing:-.02em">first.</div>
 <div style="font-size:29px;line-height:40px;font-weight:500;color:#4D4A3C;margin-top:16px">Bills, subscriptions, funds, goals and debt come out<br>before you see a single spendable dollar.</div>
</div>
{img(B+'e-setaside.png',170,570,740,rot=-2,r=30,z=4)}
{cta(GD,'#fff','ADHD BUDGET PLANNER · SHOP NOW')}''')

# 14:00 — Budget: subscriptions, fanned cards + big yearly stat (clay)
posts['2026-11-28-budget-subscriptions']=page(f'''<div class="a" style="inset:0;background:linear-gradient(170deg,#C9773C,{CL} 60%,#9C5424)"></div>
{brand('#F6DCC4')}
<div class="a" style="left:60px;right:60px;top:120px;text-align:center;z-index:5;color:#fff">
 <div style="{pillsty};background:#FFF7EA;color:{CL}">ADHD BUDGET PLANNER</div>
 <div style="font-family:L;font-weight:700;font-size:92px;line-height:98px;letter-spacing:-.02em;margin-top:26px">Little subscriptions</div>
 <div style="font-family:L;font-style:italic;font-weight:600;font-size:100px;line-height:108px;color:#FFE3B8;letter-spacing:-.02em">add up.</div>
 <div style="font-size:29px;line-height:40px;font-weight:500;color:#FBE7D6;margin-top:16px">Monthly and yearly ones on one list, each with its renewal date.</div>
</div>
{img(B+'e-sub1.png',70,530,640,rot=-4,r=28,z=4)}
{img(B+'e-sub2.png',370,765,640,rot=3,r=28,z=5)}
<div class="a" style="left:60px;top:925px;z-index:6;background:{GD};color:#fff;border-radius:22px;padding:18px 26px;transform:rotate(-3deg);box-shadow:0 20px 34px -18px rgba(0,0,0,.6)"><div style="font-size:19px;font-weight:700;letter-spacing:.16em;color:{LIME}">TAP WHEN YOU CANCEL</div><div style="font-family:L;font-style:italic;font-weight:700;font-size:36px;line-height:44px">“I cancelled it”</div></div>
{cta('#FFF7EA',GD,'ADHD BUDGET PLANNER · SHOP NOW')}''')

# 17:00 — Paycheck: bills per paycheck, "3 things" numbered list right + tilted phone left (navy)
num=lambda n,t,s: f'<div style="display:flex;gap:20px;align-items:flex-start;margin-top:30px"><div style="flex:none;width:58px;height:58px;border-radius:50%;background:{GOLD};color:{NV};font-family:L;font-weight:700;font-size:34px;display:flex;align-items:center;justify-content:center">{n}</div><div><div style="font-size:31px;line-height:38px;font-weight:700;color:#fff">{t}</div><div style="font-size:24px;line-height:33px;font-weight:500;color:#C3CFE6;margin-top:4px">{s}</div></div></div>'
posts['2026-11-28-paycheck-bills-per-paycheck']=page(f'''<div class="a" style="inset:0;background:radial-gradient(circle at 75% 30%,#21417A,{NV} 70%)"></div>
{brand('#AFC0DD')}
<div class="a" style="left:60px;right:60px;top:120px;text-align:center;z-index:5;color:#fff">
 <div style="{pillsty};background:{GOLD};color:{NV}">ADHD PAYCHECK PLANNER</div>
 <div style="font-family:L;font-weight:700;font-size:92px;line-height:98px;letter-spacing:-.02em;margin-top:26px">Bills, sorted by</div>
 <div style="font-family:L;font-style:italic;font-weight:600;font-size:100px;line-height:108px;color:{GOLD};letter-spacing:-.02em">paycheck.</div>
</div>
{phone(P+'p-bills.png',70,450,330,rot=-4,z=4,frame='#0A1122')}
<div class="a" style="left:450px;top:470px;width:570px;z-index:5">
 <div style="font-size:22px;font-weight:700;letter-spacing:.2em;color:{GOLD}">3 THINGS IT SHOWS YOU</div>
 {num(1,'What this paycheck covers','Only the bills due before next payday.')}
 {num(2,'What’s still left to pay','Tick each bill off as you pay it.')}
 {num(3,'What the next one needs','No surprises two weeks from now.')}
 <div style="margin-top:44px;background:rgba(255,255,255,.08);border:2px solid rgba(226,184,92,.55);border-radius:24px;padding:24px 28px"><div style="font-family:L;font-style:italic;font-weight:700;font-size:36px;line-height:44px;color:{GOLD}">Ticked the wrong one?</div><div style="font-size:25px;line-height:35px;font-weight:500;color:#D5DEEE;margin-top:6px">Undo is right at the top of the page.</div></div>
</div>
{cta(GOLD,NV,'ADHD PAYCHECK PLANNER · SHOP NOW')}''')

# 19:00 — Budget: gentle overspending help, relatable quote (dark green, quote card + cropped sheet)
posts['2026-11-28-budget-overspent']=page(f'''<div class="a" style="inset:0;background:linear-gradient(180deg,#25461A,{GD})"></div>
{brand('#B9CFA6')}
<div class="a" style="left:70px;right:70px;top:120px;z-index:5;color:#fff">
 <div style="font-family:L;font-style:italic;font-weight:600;font-size:150px;line-height:90px;color:{LIME};height:80px">“</div>
 <div style="font-family:L;font-weight:700;font-size:84px;line-height:92px;letter-spacing:-.02em">I went over, so<br>why even bother?</div>
 <div style="margin-top:28px;display:flex;align-items:center;gap:18px"><div style="width:60px;height:4px;background:{LIME};border-radius:2px"></div><div style="font-size:30px;line-height:40px;font-weight:500;color:#DCE8D2">Because fixing it is gentle. No guilt.</div></div>
</div>
{crop(B+'s-recovery.png',110,520,860,0,0,1080,648,r=28,z=4)}
<div class="a" style="left:0;right:0;top:1080px;text-align:center;z-index:6"><span style="display:inline-block;background:{LIME};color:{GD};border-radius:20px;padding:16px 30px;font-size:27px;font-weight:700;transform:rotate(-2deg);box-shadow:0 18px 30px -16px rgba(0,0,0,.5)">Cover it, move money, or start fresh</span></div>
{cta('#FFFDF6',GD,'ADHD BUDGET PLANNER · SHOP NOW')}''')

if __name__=='__main__': print(render(posts))
