# Security Policy

** Filter List** – Version 1.0  
**Last Updated: January 2, 2026**

Oh, someone actually reading the Security Policy? :)) Wild – I figured this page would collect dust forever. This repo's just text files + local Python scripts from a tired dev's laptop – no servers, no remote code, no fancy backend. 1.0 means it's "official" now, but security's still "don't run stupid stuff" level.

## Reporting Vulnerabilities (The "Thanks for Not Breaking It" Guide)

Found a hole? (E.g., script that deletes your homework, or rule that blocks your bank login – oops.) Report it nice – I'll fix fast(ish).

1. **Where?** Open GitHub issue with "security" label (title like "[Security] Dup checker writes wrong path").
2. **What to Include?**
   - Description: What/where (e.g., "sort_and_count crashes on Windows path").
   - Steps to Reproduce: Command + input.
   - Impact: "Deletes files?" (Spoiler: Scripts local only – no remote).
   - Setup: OS, Python version, adblocker if relevant.
3. **Private?** Super critical (unlikely – scripts don't phone home)? [Email here](mailto:coding201913@hotmail.com). 
   I'll triage quiet, fix, 
   credit (or anonymous ninja mode).

No bounties – wallet's $50 post-noodles. But gratitude + changelog shoutout? Yours.

## What Happens Next (My "I Got This" Promise)

- Triage: 3–5 days (faster if caffeine high).
- Fix: Patch next release (1.0 stable means quicker).
- Disclose: Coordinated if needed (no drama).
- Scripts Note: All local (your machine only). No net calls, no tracking. Raw files? Yours. Filters? Adblocker handles.

1.0 polish: Wildcards/scripts safer, but test sandbox (incognito/VM) – over-block = user tweak.

Thanks for caring (or stumbling here). Repo safer because of you.

– The dev shocked you read this far :)) (Now back to backlog regrets)