# CHANGELOG.md  
**Poli Filter Rules** – From zero to hero (sort of)

All notable changes to this project will be documented in this file. Beta means alpha's rough edges sanded down – fewer dups, smarter wildcards, and docs that don't make you cry. Updates ~every 3–5 days (or when the dev's not napping on noodles).

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and we adhere to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [1.0.0-beta0] – "From Alpha Trash to Beta Hope" Glow-Up (November 27, 2025)

- **Scripts Overhaul**: Added dup checkers (blocking/hiding, wildcard-proof), bulk domain remover (multi-pattern up to 10, e.g., *.com, abc.*).
- **Optimizations**: Merged similar subdomains (e.g., blah.co.com → ||co.com^$all), near-similar domains (://*abc*$document – learned from Dandelion Sprout, no more manual Ctrl+C/V hell).
- **Blocking Tweaks**: Added gambling/casino domains (200+).
- **Hiding Tweaks**: Added cookie consent/footer/signup/login nags; fixed noob rules like *##.footer → ##.footer (wtf, beta brain).
- **Docs Remake**: Polished ACKNOWLEDGEMENTS, ToS, EULA, README, Wiki (non-tech friendly), CONTACT bio, SECURITY.
- **FAQ Expansion**: More philosophical/silly Qs (e.g., "Why hate fake politeness?" – life's too short).
- 3 sleepless days + $50 wallet grind – worth it? You decide.

## [1.0-alpha5] – "5 Hours of My Life Gone: Gambling Ads & More Useless Crap Hidden" Mega Patch - 2025-11-25
- Added 200+ international gambling domains + advanced rules (UK/India/Middle East/Bangladesh nukes).  
- Hidden Postman chatbot/cookie; Twitch Turbo; Medium email/footer/membership; Footers on TikTok/Bluesky/Loaded/ether.fi/Chess.com.  
- 5 hours wasted – Node.js reinstall mid-grind (unrelated pain).

## [1.0-alpha2.5] - "Scam Emails & More Gambling Bullshit" - 2025-11-23
- Added 84+ gambling domains + advanced rules.  
- Hidden Itch.io/Reddit footers/legal; Brave/karate/Duolingo footers.  
- Duplicate domain removed (efficiency? Idk).
- Official war on scams and Facebook's garbage moderation
- 2 hours of my life wasted – worth it?

## [1.0-alpha2] - "I Hate Gambling Sites & HoYoverse" Emergency Patch - 2025-11-23
- Added 80+ gambling/casino domains + advanced rules.  
- Hidden Google/Instagram footers; HoYoLab annoyances nuked.  
- Deleted all HoYoverse games (-$200 goodbye).

## [1.0-alpha1] - "The International Mental Breakdown Release" - 2025-11-21
- Initial international release: Full docs, modular structure, raw → generate scripts, Wiki, savage legal suite.

## [1.0-alpha0] - "The Dumpster Fire Birth" - I Forgot When
- Initial alpha release: Basic rules, minimal docs.
---

Beta's milestone – from alpha dumpster to "maybe usable." Star if it blocks your pain (or pities mine). Feedback? Issues open (Wiki first).

– The dev who's one wildcard away from calling it "stable" (don't bet on it)