import sys,os; sys.path.insert(0,os.path.dirname(__file__))
from lib import *
def crop(p,x,y,w,cx,cy,cw,ch,r=26,z=4,rot=0):
    W,H=sz(p); s=w/cw; hh=round(ch*s)
    return f'<div class="a" style="left:{x}px;top:{y}px;width:{w}px;height:{hh}px;border-radius:{r}px;overflow:hidden;z-index:{z};transform:rotate({rot}deg);{SH};background:url(file://{p}) no-repeat;background-size:{round(W*s)}px {round(H*s)}px;background-position:-{round(cx*s)}px -{round(cy*s)}px"></div>'
def strip(p,w,cy,ch):
    W,H=sz(p); s=w/W
    return f'<div style="width:{w}px;height:{round(ch*s)}px;background:url(file://{p}) no-repeat;background-size:{w}px {round(H*s)}px;background-position:0 -{round(cy*s)}px"></div>'
pillsty='border-radius:999px;padding:10px 24px;font-size:20px;font-weight:700;letter-spacing:.16em;display:inline-block'
def tag(x,y,t,bg,fg,ic,z=7,rot=0):
    return f'<div class="a" style="left:{x}px;top:{y}px;z-index:{z};display:flex;align-items:center;gap:12px;background:{bg};color:{fg};border-radius:18px;padding:14px 22px 14px 14px;font-size:24px;font-weight:700;transform:rotate({rot}deg);box-shadow:0 18px 30px -16px rgba(0,0,0,.5)">{check(ic,bg,32)}{t}</div>'
posts={}

# 10:00 — Paycheck: debts, bold hook left-aligned + laptop + 2 tags (navy)
posts['2026-11-29-paycheck-debt-free-date']=page(f'''<div class="a" style="inset:0;background:linear-gradient(160deg,#1E3C70,{NV} 65%)"></div>
{brand('#AFC0DD')}
<div class="a" style="left:70px;top:120px;width:940px;z-index:5;color:#fff">
 <div style="{pillsty};background:{GOLD};color:{NV}">ADHD PAYCHECK PLANNER</div>
 <div style="font-family:L;font-weight:700;font-size:94px;line-height:100px;letter-spacing:-.02em;margin-top:26px">Debt feels lighter</div>
 <div style="font-family:L;font-style:italic;font-weight:600;font-size:100px;line-height:108px;color:{GOLD};letter-spacing:-.02em">with a date.</div>
 <div style="font-size:29px;line-height:40px;font-weight:500;color:#D5DEEE;margin-top:16px">See your debt-free month and the order to pay things off.</div>
</div>
{lap(P+'d-debts.png',110,500,860,z=3,frame='#0A1122')}
{tag(50,985,'Smallest balance or highest interest','#fff',NV,GOLD)}
{tag(440,1080,'Extra payments move your date','#fff',NV,GOLD)}
{cta(GOLD,NV,'ADHD PAYCHECK PLANNER · SHOP NOW')}''')

# 14:00 — Paycheck: plan spending, before/after text cards left + phone right (cream)
ba=lambda lab,lc,bg,fg,body: f'<div style="background:{bg};color:{fg};border-radius:26px;padding:26px 30px;margin-top:24px;box-shadow:0 20px 34px -22px rgba(0,0,0,.35)"><div style="font-size:20px;font-weight:700;letter-spacing:.2em;color:{lc}">{lab}</div>{body}</div>'
posts['2026-11-29-paycheck-plan-spending']=page(f'''<div class="a" style="inset:0;background:{CRM}"></div>
<div class="a" style="right:-200px;top:330px;width:700px;height:700px;border-radius:50%;background:#ECE3CF"></div>
{brand('#5A5F6B')}
<div class="a" style="left:60px;right:60px;top:120px;text-align:center;z-index:5;color:#141B2D">
 <div style="{pillsty};background:{NV};color:#fff">ADHD PAYCHECK PLANNER</div>
 <div style="font-family:L;font-weight:700;font-size:92px;line-height:98px;letter-spacing:-.02em;margin-top:26px">Plan it before</div>
 <div style="font-family:L;font-style:italic;font-weight:600;font-size:96px;line-height:104px;color:#B8862F;letter-spacing:-.02em">payday spends it.</div>
</div>
<div class="a" style="left:60px;top:455px;width:560px;z-index:5">
 {ba('BEFORE','#8A8F9C','#fff','#141B2D','<div style="font-family:L;font-style:italic;font-weight:600;font-size:38px;line-height:48px;margin-top:10px">“I’ll just wing it<br>this week.”</div>')}
 <div style="text-align:center;margin-top:18px;font-size:44px;color:#B8862F;line-height:44px">↓</div>
 {ba('AFTER',GOLD,NV,'#fff','<div style="font-size:28px;line-height:40px;font-weight:500;margin-top:12px;color:#E4EAF5">Groceries, transport, eating out: each gets its number for this paycheck.</div><div style="font-family:L;font-style:italic;font-weight:700;font-size:34px;line-height:44px;color:'+GOLD+';margin-top:14px">Safe to spend updates live.</div>')}
</div>
{phone(P+'p-plan.png',660,450,350,rot=3,z=4,frame='#0A1122')}
{cta(NV,'#fff','ADHD PAYCHECK PLANNER · SHOP NOW')}''')

# 17:00 — Budget: envelopes roll over + move money, annotated card with callouts (light lime)
posts['2026-11-29-budget-envelopes']=page(f'''<div class="a" style="inset:0;background:#EEF3E2"></div>
{brand('#4A5641')}
<div class="a" style="left:60px;right:60px;top:120px;text-align:center;z-index:5;color:{INK}">
 <div style="{pillsty};background:{G};color:#fff">ADHD BUDGET PLANNER</div>
 <div style="font-family:L;font-weight:700;font-size:94px;line-height:100px;letter-spacing:-.02em;margin-top:26px">Leftovers don’t</div>
 <div style="font-family:L;font-style:italic;font-weight:600;font-size:100px;line-height:108px;color:{G};letter-spacing:-.02em">disappear.</div>
 <div style="font-size:29px;line-height:40px;font-weight:500;color:#3A4632;margin-top:16px">Money left in an envelope rolls over to next month.</div>
</div>
<div class="a" style="left:60px;top:560px;width:960px;z-index:4;border-radius:26px;overflow:hidden;{SH}">{strip(B+'e-envelopes.png',960,0,200)}{strip(B+'e-envelopes.png',960,326,128)}</div>
{img(B+'s-move.png',570,810,450,rot=3,r=26,z=5)}
<div class="a" style="left:60px;top:900px;z-index:6;background:{GD};color:#fff;border-radius:22px;padding:18px 26px;transform:rotate(-2deg);box-shadow:0 20px 34px -18px rgba(0,0,0,.6)"><div style="font-size:19px;font-weight:700;letter-spacing:.16em;color:{LIME}">RAN SHORT SOMEWHERE?</div><div style="font-family:L;font-style:italic;font-weight:700;font-size:34px;line-height:42px">Move money<br>between envelopes.</div></div>
{cta(GD,'#fff','ADHD BUDGET PLANNER · SHOP NOW')}''')

# 19:00 — Paycheck: monthly review, giant "5" stat poster + cropped review card (navy/gold)
li=lambda t: f'<div style="display:flex;gap:16px;align-items:center;margin-top:26px">{check(GOLD,NV,40)}<span style="font-size:31px;line-height:38px;font-weight:500;color:#E4EAF5">{t}</span></div>'
posts['2026-11-29-paycheck-monthly-review']=page(f'''<div class="a" style="inset:0;background:radial-gradient(circle at 20% 35%,#22437E,{NV} 70%)"></div>
{brand('#AFC0DD')}
<div class="a" style="left:60px;right:60px;top:120px;text-align:center;z-index:5;color:#fff">
 <div style="{pillsty};background:{GOLD};color:{NV}">ADHD PAYCHECK PLANNER</div>
 <div style="font-family:L;font-weight:700;font-size:92px;line-height:98px;letter-spacing:-.02em;margin-top:26px">End of the month?</div>
 <div style="font-family:L;font-style:italic;font-weight:600;font-size:96px;line-height:104px;color:{GOLD};letter-spacing:-.02em">Take five.</div>
</div>
<div class="a" style="left:70px;top:470px;width:440px;z-index:5;color:#fff">
 <div style="font-family:L;font-weight:700;font-size:300px;line-height:260px;color:{GOLD};letter-spacing:-.04em">5</div>
 <div style="font-size:30px;font-weight:700;letter-spacing:.18em;color:#fff;margin-top:6px">CALM MINUTES</div>
 {li('What went well')}
 {li('Your month in numbers')}
 {li('One small thing to try')}
</div>
{crop(P+'d-review.png',530,520,490,560,480,1200,820,r=26,z=4,rot=2)}
<div class="a" style="left:520px;top:930px;width:500px;z-index:6;background:#fff;color:{NV};border-radius:24px;padding:22px 26px;transform:rotate(-2deg);box-shadow:0 20px 34px -18px rgba(0,0,0,.6)"><div style="font-family:L;font-style:italic;font-weight:700;font-size:32px;line-height:40px">“It’s never a grade.”</div><div style="font-size:22px;line-height:31px;font-weight:500;color:#4A5468;margin-top:6px">The score is about habits you control, and you can turn it off.</div></div>
{cta(GOLD,NV,'ADHD PAYCHECK PLANNER · SHOP NOW')}''')

if __name__=='__main__': print(render(posts))
