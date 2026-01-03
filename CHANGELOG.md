# CHANGELOG.md  
**Poli Filter Rules** – From zero to hero (sort of)

All notable changes to this project will be documented in this file. Beta means alpha's rough edges sanded down – fewer dups, smarter wildcards, and docs that don't make you cry. Updates ~every 3–5 days (or when the dev's not napping on noodles).

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and we adhere to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 1.0.1 – Bug Fix Patch (January 03, 2026)

- Added "Fix Incorrect Rules" issue template – report bad/broken rules easily.
- Switched Actions to bash workflow – shorter, easier debug/fix (new bash knowledge test :v).
- Various bug fixes from Issues (UI breaks, wrong hides, etc. – details in Issues, templates for a reason :v).
- Minor tweaks (lazy list – check commits).

Light patch – repo tidier.

---

## 1.0.0 – 'New Year, New Loop, +1 Age' Official Release (January 2, 2026)

- **Fixes**: TikTok white page; Wrong filter names in finals; CSS hiding quote errors (noob strikes fixed).
- **Adds**: 6 Issue Templates (bug/feature/add-remove rule/feedback/off-topic); FUNDING.yml (donate nudge :))); 4 PR Templates (bug/update/add-remove rule); 1500+ porn rules; 10–30 $removeparam; 100+ gambling/scam sites; Love to every file (raws/hides/blocks beefed).
- **Move/Delete**: Personal-FAQ to personal repo (cleaner here).
- **Remake**: Full docs/legal (README/Wiki/ToS/EULA/Disclaimer) – polished for official.
- 3000+ total rules – from alpha trash to 1.0 "stable-ish."

Beta ends (kinda). Bugs? Life continues :v

---

## 1.0.0-beta0.7.0 – "Porn Wars & FB Rage" Bulk Nuke (December 13, 2025)

- Fixed over-aggressive hiding rules ('##[class=”overlay”], ##[id*=”social”]' etc. – broke Steam payments; specific names now).
- Removed duplicates in scattered rules.
- +160 gambling sites to full-domain-blocks.txt.
- +250 tracking rules.
- +~450 porn sites (total ~700 rules, ~800+ sites); removed '*jav*.$document' from anti-porn.txt.
- Advanced tweaks: Multi-site rules + $removeparam tests in advanced-block.txt.
- Revived generate-blocking.py for bulk porn site rules.
- Updated sort_and_count_everything_rules.py: Added EXPIRE_TIME = "3 days" for AdGuard auto-update.
- New Scripts (2 Toys):
  + DNS-level blocker for Windows (0.0.0.0 lines – no repeat drudgery).
  + Param/value extractor for $removeparam (file input, table output – endless domains? Solved).
- Re-ran sort_and_count for add/remove tweaks.
- Personal FAQ: Part 6 :D.
- Wiki Add: New page for 2 scripts.
- Blahblah fixes: Other errors (lazy list :v).

Porn/gambling bulk – beta fiercer.

---

## 1.0.0-beta0.6125 – Random Number Patch (December 07, 2025)

- Fixed over-aggressive footer rules (`##div[class*=”footer”]`,`##div[id*=”footer”]` – killed buttons; manual 
  tweaks now :D).
- Removed redundant/conflicting rules with experimental features.
- ***Updated README:*** Changed Structure, How to Use & Auto Script sections.
- ***Wiki Refresh:*** Added 3 new pages (experimental features explain, tracking block guide, FAQ updates :D); Fixed 
  'almost entire' Wiki.
- ***Cookie consent boost:*** More CDN/JS in cookie-consent-blocking.txt; extra CSS in cookie-consent-hiding.txt.
- ***Experimental Features (Volatile – Test Sandbox, No Pay :v)***:
  + *Cookie CSS hide (99.919%)*: `##[class*=”cookie”]`, `##[id*=”consent”]`, variants.
  + *Social/copyright nuke:* `##[id*=”copyright”]`, etc.
  + *Tracking block:* New `/blocks/block-tracking.txt` (`google-analytics.com`, classics).
  + *Download hide:* New `/blocks/download-blocking.txt` (Play/App nags). E.g., '`/*google-play*.svg$image,
  domain=~google.
    com|~play.google.com`.
  + *Third-party block/hide:* New `third-party-blocking.txt` (e.g., `||youtube.com^$third-party`).
  + *Anti-porn block:* New `blocks/anti-porn.txt` :D (If you wanna see, don't use this – me too :)))))).
- New Script: `sort_and_count_everything_rules.py` (original `sort_and_count_block.py` intent) – Adds pro headers *
  (Title, Description, GitHub link, author, blah blah :v)*; Sorts/counts rules for *both* Hiding and Blocking (Grok 
  is da best :)) ). Removed old scripts: `generate-blocking.py`, `organize-hiding.py`, and `sort-raws-block.py`.
- *Hiding:* More footers.
- *Blocking:* Dozens gambling/scams :))) (FB moderation fatigue).
- *Hiding:* Login/signup on `myanimelist.com`, `fandom.com`, etc.
- *Exceptions:* New whitelists.
- *No-One-Cares FAQ:* Part 5 – rants added :)))
- *Docs:* Experimental warnings everywhere.

Light tweaks – beta sharper.

---
## 1.0.0-beta0.5 – Fix & Optimization Patch (November 29, 2025)

- Added `sort-raws-block.py` – Alphabetizes raws.txt for clean reads.
- Optimized full-block-domains.txt to 200 rules (from ~800 – wildcard syntax saves lives).
- Advanced rules boost: Nuke 96.69% sites (e.g., `://*jun8*.$document` for variants).
- New files: cookie-consent-blocking.txt (CDN/JS kills) + cookie-consent-hiding.txt (CSS fallback).
- Exceptions for 'bet' sites (bet.com, bethesda.net – wildcard mercy).
- New domains to advanced + cookie CDN blocks.
- Hiding: Footers/cookie consent on sites + fixed selector misses.
- Personal FAQ: More "no-one-cares" Qs :)))
- README: Tree update, cookie paths :)), new script guide, version bump.
- Wiki: Sort script usage; "read or suffer" FAQs :D; Cookie paths.

Nothing major – just tweaks. Beta smoother.

---
## [1.0.0-beta0] – "From Alpha Trash to Beta Hope" Glow-Up (November 27, 2025)

- **Scripts Overhaul**: Added dup checkers (blocking/hiding, wildcard-proof), bulk domain remover (multi-pattern up to 10, e.g., *.com, abc.*).
- **Optimizations**: Merged similar subdomains (e.g., blah.co.com → ||co.com^$all), near-similar domains (://*abc*$document – learned this syntax from Dandelion Sprout, no more manual Ctrl+C/V hell).
- **Blocking Tweaks**: Added gambling/casino domains (200+).
- **Hiding Tweaks**: Added cookie consent/footer/signup/login nags; fixed noob rules like *##.footer → ##.footer (wtf, beta brain).
- **Docs Remake**: Polished ACKNOWLEDGEMENTS, ToS, EULA, README, Wiki (non-tech friendly), CONTACT bio, SECURITY.
- **FAQ Expansion**: More philosophical/silly Qs (e.g., "Why hate fake politeness?" – life's too short).
- 3 sleepless days + $50 wallet grind – worth it? You decide.

---
## [1.0-alpha5] – "5 Hours of My Life Gone: Gambling Ads & More Useless Crap Hidden" Mega Patch - 2025-11-25
- Added 200+ international gambling domains + advanced rules (UK/India/Middle East/Bangladesh nukes).  
- Hidden Postman chatbot/cookie; Twitch Turbo; Medium email/footer/membership; Footers on TikTok/Bluesky/Loaded/ether.fi/Chess.com.  
- 5 hours wasted – Node.js reinstall mid-grind (unrelated pain).

---
## [1.0-alpha2.5] - "Scam Emails & More Gambling Bullshit" - 2025-11-23
- Added 84+ gambling domains + advanced rules.  
- Hidden Itch.io/Reddit footers/legal; Brave/karate/Duolingo footers.  
- Duplicate domain removed (efficiency? Idk).
- Official war on scams and Facebook's garbage moderation
- 2 hours of my life wasted – worth it?

---
## [1.0-alpha2] - "I Hate Gambling Sites & HoYoverse" Emergency Patch - 2025-11-23
- Added 80+ gambling/casino domains + advanced rules.  
- Hidden Google/Instagram footers; HoYoLab annoyances nuked.  
- Deleted all HoYoverse games (-$200 goodbye).

---
## [1.0-alpha1] - "The International Mental Breakdown Release" - 2025-11-21
- Initial international release: Full docs, modular structure, raw → generate scripts, Wiki, savage legal suite.

---
## [1.0-alpha0] - "The Dumpster Fire Birth" - I Forgot When
- Initial alpha release: Basic rules, minimal docs.

---

Beta's milestone – from alpha dumpster to "maybe usable." Star if it blocks your pain (or pities mine). Feedback? Issues open (Wiki first).

– The dev who's one wildcard away from calling it "stable" (don't bet on it)

Last Updated: December 06, 2025