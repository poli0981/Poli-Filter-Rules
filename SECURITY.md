# Security Policy

**Custom Adblock Filter List** – Version 1.0.0-beta0  
**Last Updated: November 26, 2025**

Oh, someone actually reading this? :)) Wild. I thought security policies were for fancy repos with VCs and bug bounties. This is just a tired dev's text files + Python scripts fighting ads on a wheezing laptop. But hey, beta means we're pretending to be responsible – so here's the deal.

## Reporting Vulnerabilities (The "Don't Panic" Guide)

If you find a hole (e.g., script that leaks your raw list to the moon, or a rule that accidentally blocks your bank login – oops), don't freak. Report it chill:

1. **Where?** Open a GitHub issue labeled "security" (or just say "SECURITY BUG" in title – I'll spot it).
2. **What to Include?** 
   - Description: What breaks? (e.g., "Duplicate checker writes to /tmp without perms").
   - Steps to Reproduce: Code snippet or command that triggers it.
   - Impact: "Crashes on Windows" or "Exposes domains? Nah, just local".
   - Your Setup: OS, Python version, adblocker (if relevant).
3. **Keep It Private?** For real nukes (e.g., if scripts had remote calls – spoiler: they don't), email [lopop05905@proton.me] first. I'll triage quietly, fix, then credit you in changelog (or anonymously if you want ninja mode).

No bounties here – my wallet's emptier than my social life. But credit + eternal gratitude? Yours.

## What We Do About It (The "I Got This" Promise)

- Triage: Within 3–5 days (or faster if caffeine hits right).
- Fix: Patch in next release (beta's iterative – might hotfix if critical).
- Disclose: Coordinated if needed (no drama, just "hey, fixed that thing").
- Scripts Specifics: All run local (no net calls). Raw files? Your machine only. Filters? Adblocker handles – blame them for leaks.

Beta caveat: Optimizations like wildcard merges are powerful but user-tested – if they nuke too much, that's a "feature" until reported.

Thanks for caring (or stumbling here). You're already 0.01% safer than most repos. Make the web secure(ish).

– The dev who's shocked you read this far :)) (Now back to noodles)

---
**Version**: 1.0.0-beta0  
**Last Updated**: November 26, 2025  
**Contact**: [your.email@gmail.com] for private reports
