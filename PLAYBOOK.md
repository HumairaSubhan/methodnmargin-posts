# Method & Margin: daily Instagram playbook

Shop: https://www.etsy.com/shop/MethodNMargins · Instagram: @methodnmargin
Metricool brand id (blogId): 7266413 · timezone Asia/Riyadh

## Daily routine (what the scheduled run does)
1. `git pull`. Read this file and `LOG.md`.
2. **5 posts per day.** Daily slots (Asia/Riyadh): **10:00, 12:00, 14:00, 17:00, 19:00** (from Metricool best-time data). Make sure every slot of **tomorrow and the day after** has a post (check `LOG.md` and Metricool `getScheduledPosts`). Create only the missing slots (normally 5 per run, at most 10).
3. For each missing slot: alternate products slot by slot (P, B, P, B, P one day, then B, P, B, P, B the next), pick a hook/feature that is not yet in `LOG.md` (all 5 posts of a day must use different features and different layouts), write `tools/batch_YYYY-MM-DD.py` with all the day's posts (copy the style of `tools/batch_2026-11-26.py`, `from lib import *`), run it → `posts/YYYY-MM-DD-<product>-<slug>.jpg`.
4. Look at the rendered image (Read it) before publishing: no overlaps, no cut-off text, no text running off the edge, headline ≤ 2 lines, nothing repeated inside one image (e.g. the same number shown twice), every claim true (see facts below).
5. Commit + push (`git -c push.negotiate=true push`). Image URL = `https://raw.githubusercontent.com/HumairaSubhan/methodnmargin-posts/main/posts/<file>.jpg`. Check it returns 200 with curl before scheduling.
6. Schedule with Metricool `createScheduledPost`: network instagram, type POST, the image URL, caption, publicationDate `{dateTime:"YYYY-MM-DDTHH:00:00", timezone:"Asia/Riyadh"}` at the slot time. autoPublish true.
7. Add a line to `LOG.md`, commit, push.

## Hard rules
- **One product per image. Never put both planners in one image, never compare them.**
- Shop link `etsy.com/shop/MethodNMargins` printed on every image (use `cta()`), caption says "Link in bio".
- Only real features (lists below). No prices (they change with sales). No "works on phone" claim for the Paycheck Planner.
- 1080×1350 canvas (rendered at 2×), brand line "METHOD & MARGIN" at top, big Lora headline (≤ 2 lines, roughly ≤ 22 characters per line at 96px), Poppins for everything else, high contrast, large text.
- Each post a different layout/hook from the last 15 in `LOG.md`; reuse a feature only after 10+ days and then with a new angle. Mix formats: bold hook + mockup, relatable quote, "3 things", myth vs fact, before/after (text only, no fake data), checklist, single feature close-up, question post.
- Paycheck Planner = navy `NV` + gold `GOLD` + cream `CRM`. Budget Planner = green `G`/`GD` + cream `BG` + lime `LIME` (clay `CL` accent ok).
- Captions: 2–4 short lines, hook first, one emoji max per line, "🛒 Link in bio", 5–7 hashtags (#adhd #adhdadults + topic tags). Ask a question or "comment X" sometimes for engagement.

## Product facts — ADHD Paycheck Planner (assets/paycheck/)
Offline single-file app in the browser, pay once, no account, no subscription, data stays on device, free demo in listing.
Home: "Left to spend" until payday with daily amount and days-to-payday ring; "What should I do right now?" = 3 next steps ("Just do these 3"); Focus / Full view; Log spending; Add bill.
Pages: Paycheck (where every dollar of this paycheck goes), Bills (per paycheck, still to cover, mark paid), Plan (spending plan per category), Insights, Monthly review, Savings & goals (jars), Debts, Net worth, Tools.
Tools/features: Can I afford this?, Cool-off list (wait before you buy, then decide), Spending log, Catch up, Import bank CSV, Undo + History, themes (emerald, graphite, ocean, rose, sapphire, dark modes), number styles.
Sample data: paycheck $610, set aside $385, spending plan $190, left to spend $225.00, $37.50 a day, payday Dec 11.
Good shots: e-hero, e-now, e-cooloff(-c), s-afford, s-catchup, p-bills, p-plan, p-paycheck, p-spending, p-goals, d-home, d-paycheck, d-goals, d-debts, d-worth, d-insights, t-* themes.

## Product facts — ADHD Budget Planner (assets/budget/)
Offline, pay once, no account, no subscription, works offline, data stays on device, free demo in listing.
Safe to spend today (everyday envelope money left ÷ days left; spend less today, tomorrow gets more); Focus view + Customize Today; envelope budget (everyday vs planned, leftovers roll over, move money); plan next month early; set aside first (bills, subscriptions, sinking funds, goals, debt payments); money not given a job; "I spent…" quick log; spending search; bank CSV import; spreadsheet import; Can I afford this?; cool-off list (48 hours); gentle overspending help; bills calendar (calendar/list, autopay); subscriptions (monthly + yearly, renewal dates); sinking funds; savings goals; debts (APR, payoff month, update from statement); no-spend day streaks ("a missed day never erases the ones before it"); weekly check-in (~2 min, 4 steps); 7 themes + dark mode, text size, easier-to-read font, higher contrast, hide amounts, calm animations, currency & date formats; backup & restore; undo & recent changes.
NOT in the app (never claim): charts/insights, CSV/PDF export, reminders/notifications, calendar export, voice logging, automatic backup.
Sample data: safe to spend $46.93, money in $4,200, set aside $1,781.99, in envelopes $1,010.
Good shots: e-hero, e-envelopes, e-setaside, e-goal, e-debt, e-sub1/2, e-fund1/2, s-afford, s-cooloff, s-logspend, s-checkin, s-recovery, s-usedup, p-today, p-focus, p-budget, p-bills, p-habits, p-th-* themes, d-today, d-bills, d-budget.
