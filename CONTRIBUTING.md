# Contributing Guide

**Poli-Filter-Rules**  
**Last Updated: November 26, 2025**

Hey, you want in? Cool – this solo + AI repo appreciates the company (humans are rare here). Beta means we're polished but still raw: Fork, tweak, PR. No hand-holding, but I'll merge if it's solid. Read Wiki/FAQ first (seriously, 90% of "help" is there).

## Ways to Contribute

- **Rules/Scripts**: Add to raw files (raws.txt for blocking, hiding-raws.txt for hiding), run scripts (generate/organize/clean), PR both raw + generated.
- **Optimizations**: Suggest wildcard merges or dup fixes – learned from Dandelion Sprout, so bring that energy.
- **Docs/Bug Hunts**: Tweak README/Wiki, or hunt glitches (details below).
- **Stars/Forks**: Silent support? That's 50% of my motivation (the other 50% is spite).

PR Tips:
- Branch: `feature/add-gambling-nukes` (descriptive, not "update").
- Commit: "Add 50 gambling domains + wildcard merge for *.co.com".
- Test: Run scripts, subscribe in your adblocker, verify no breakage.
- Why? Include rationale (e.g., "These popups ruined my Reels scroll").

## Bug Reporting (The "Help Me Fix This" Section)

Bugs keep me up at night (more than ads). Report 'em straight – no essays, no fluff. Joy in my life? When this runs smooth and someone (you?) uses it without cursing my name.

### 1. Script Errors (e.g., Dup Checker Crashes)
Provide:
- IDE (PyCharm/VS Code?).
- Python version (e.g., 3.12).
- Detailed error (copy-paste traceback or screenshot).
- OS (Windows 11? Linux Mint?).
- Adblocker tool (Brave? uBlock? – if relevant).

Example: "Ran `check_duplicates.py --remove on Windows 11/Python 3.11/VS Code. Error: 'pathlib.Path not found'`. Screenshot attached."

### 2. URL Conflicts (Wrong Block/Hide – My Hardcore Rules Bite Back)
My rules can be aggressive (wildcard nukes, anyone?). If a site breaks:
- Exact URL (e.g., https://shopee.vn/cart – not "shopping site").
- Selector/component affected (e.g., ".cart-button hidden" or "login form blocked").
- Screenshot (optional, but gold – upload to issue).

Example: "https://tiki.vn/login blocked login form. Selector: #login-div. Screenshot: [img]. Using AdGuard on Android."

### General Rules for Reports
- **Straight to the Point**: No "hi, hope you're well" – jump in. Irrelevant chit-chat = ignore (society's fake enough; let's keep it real).
- **Toxic OK (Kinda)**: Trash me/project? Fine – I'm numb/emotionally scarred (family/school/university vibes). But toxic to others? Rethink your life, kindly. +1 ignore, no debate.
- **Non-Devs Welcome**: If you're not tech-savvy, report anyway – I'll guide. Devs? Detail like above (you're better than my trash self – use it).
- **No Repeats**: Wiki/FAQ covers 99%. Duplicate issue? Closed with love (and RTFM).

Open issues/PRs on GitHub. I'll respond in 3–5 days (or when coffee hits). Thanks – your fix might save my sanity.

– The dev who lives for bug-free runs (rare, but golden)