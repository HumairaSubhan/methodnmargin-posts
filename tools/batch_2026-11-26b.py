import sys,os; sys.path.insert(0,os.path.dirname(__file__))
from lib import *
def tag(x,y,t,bg,fg,ic,z=7):
    return f'<div class="a" style="left:{x}px;top:{y}px;z-index:{z};display:flex;align-items:center;gap:12px;background:{bg};color:{fg};border-radius:18px;padding:14px 22px 14px 14px;font-size:23px;font-weight:700;box-shadow:0 18px 30px -16px rgba(0,0,0,.5)">{check(ic,bg,32)}{t}</div>'
posts={}
# A — Budget: bills calendar (dark green)
posts['2026-11-26-budget-bills']=page(f'''<div class="a" style="inset:0;background:radial-gradient(circle at 30% 20%,#2C5520,{GD} 70%)"></div>
{brand('#B9CFA6')}
<div class="a" style="left:70px;top:110px;width:940px;z-index:5;color:#fff">
 <div style="display:inline-block;background:{LIME};color:{GD};border-radius:999px;padding:10px 24px;font-size:20px;font-weight:700;letter-spacing:.16em">ADHD BUDGET PLANNER</div>
 <div style="font-family:L;font-weight:700;font-size:92px;line-height:98px;letter-spacing:-.02em;margin-top:24px">Bills sneaking up?</div>
 <div style="font-family:L;font-style:italic;font-weight:600;font-size:96px;line-height:104px;color:{LIME};letter-spacing:-.02em">Not anymore.</div>
 <div style="font-size:29px;line-height:40px;font-weight:500;color:#DCE8D2;margin-top:14px">Every bill on one calendar, so nothing surprises you.</div>
</div>
{lap(B+'d-bills.png',110,560,860,z=3,frame='#0E1A0A')}
{tag(50,1030,'Autopay ticks itself off','#FFFDF6',INK,G)}
{tag(560,1080,'Paid bills crossed out','#FFFDF6',INK,G)}
{cta(LIME,GD,'ADHD BUDGET PLANNER · SHOP NOW')}''')
# B — Paycheck: cool-off list (cream)
pill=lambda t,bg,fg: f'<span style="background:{bg};color:{fg};border-radius:999px;padding:14px 28px;font-size:26px;font-weight:700">{t}</span>'
posts['2026-11-26-paycheck-cooloff']=page(f'''<div class="a" style="inset:0;background:{CRM}"></div>
<div class="a" style="left:-160px;top:620px;width:560px;height:560px;border-radius:50%;background:#ECE3CF"></div>
{brand('#5A5F6B')}
<div class="a" style="left:60px;right:60px;top:110px;text-align:center;z-index:5;color:#141B2D">
 <div style="display:inline-block;background:{NV};color:#fff;border-radius:999px;padding:10px 24px;font-size:20px;font-weight:700;letter-spacing:.16em">ADHD PAYCHECK PLANNER</div>
 <div style="font-family:L;font-weight:700;font-size:88px;line-height:96px;letter-spacing:-.02em;margin-top:24px">The “I’ll think</div>
 <div style="font-family:L;font-style:italic;font-weight:600;font-size:92px;line-height:100px;color:#B8862F;letter-spacing:-.02em">about it” list.</div>
 <div style="font-size:29px;line-height:40px;font-weight:500;color:#4A4F5C;margin-top:14px">Park the impulse buy. Decide when the wait is over.</div>
</div>
{img(P+'e-cooloff-c.png',265,530,550,r=26,z=4)}
<div class="a" style="left:60px;right:60px;top:{530+h(P+'e-cooloff-c.png',550)+30}px;display:flex;justify-content:center;gap:14px;z-index:5">{pill('Buy it',NV,'#fff')}{pill('Wait longer','#fff',NV)}{pill('Let it go',GOLD,NV)}</div>
{cta(NV,'#fff','ADHD PAYCHECK PLANNER · SHOP NOW')}''')
# C — Budget: no-spend streaks (light lime)
posts['2026-11-26-budget-nospend']=page(f'''<div class="a" style="inset:0;background:#EEF3E2"></div>
<div class="a" style="left:520px;top:420px;width:700px;height:700px;border-radius:50%;background:#DCE8C8"></div>
{brand('#4A5641')}
<div class="a" style="left:70px;top:230px;width:520px;z-index:5;color:{INK}">
 <div style="font-family:L;font-weight:700;font-size:96px;line-height:100px;letter-spacing:-.02em">Small wins</div>
 <div style="font-family:L;font-style:italic;font-weight:600;font-size:100px;line-height:108px;color:{G};letter-spacing:-.02em">count.</div>
 <div style="font-size:29px;line-height:41px;font-weight:500;color:#3A4632;margin-top:20px">Tap a day with no spending. Watch your streak grow.</div>
 <div style="margin-top:34px;background:{G};color:#fff;border-radius:24px;padding:26px 28px;font-family:L;font-style:italic;font-size:34px;line-height:44px;font-weight:600">“A missed day never erases the ones before it.”</div>
 <div style="margin-top:22px;display:inline-block;background:#fff;border:1.5px solid #C9D8B4;color:{G};border-radius:999px;padding:10px 22px;font-size:20px;font-weight:700;letter-spacing:.14em">ADHD BUDGET PLANNER</div>
</div>
{phone(B+'p-habits.png',640,230,360,rot=4,z=4,frame='#14200F')}
{cta(GD,'#fff','ADHD BUDGET PLANNER · SHOP NOW')}''')
# D — Paycheck: savings jars (navy)
posts['2026-11-26-paycheck-goals']=page(f'''<div class="a" style="inset:0;background:linear-gradient(180deg,#1B3766,{NV})"></div>
{brand('#AFC0DD')}
<div class="a" style="left:60px;right:60px;top:110px;text-align:center;z-index:5;color:#fff">
 <div style="display:inline-block;background:{GOLD};color:{NV};border-radius:999px;padding:10px 24px;font-size:20px;font-weight:700;letter-spacing:.16em">ADHD PAYCHECK PLANNER</div>
 <div style="font-family:L;font-weight:700;font-size:92px;line-height:98px;letter-spacing:-.02em;margin-top:24px">Watch your savings</div>
 <div style="font-family:L;font-style:italic;font-weight:600;font-size:100px;line-height:108px;color:{GOLD};letter-spacing:-.02em">fill up.</div>
 <div style="font-size:29px;line-height:40px;font-weight:500;color:#D5DEEE;margin-top:14px">Every goal is a jar. A little goes in each payday.</div>
</div>
{lap(P+'d-goals.png',110,580,860,z=3,frame='#0A1122')}
{tag(60,1060,'Automatic top-ups each payday','#fff',NV,GOLD)}
{cta(GOLD,NV,'ADHD PAYCHECK PLANNER · SHOP NOW')}''')
if __name__=='__main__': print(render(posts))
