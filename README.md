# Poli-Filter-Rules - Personal Content Blocker Filter List

[![Version](https://img.shields.io/badge/version-1.0.0--beta0.7.0-blue.svg)](https://github.com/poli0981/Poli-Filter-Rules)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Updates](https://img.shields.io/badge/updates-every%203%20days-orange.svg)](https://github.com/poli0981/my-content-blocker/commits/main)

A modular, auto-generated adblock filter list for nuking ads, trackers, popups, and annoyances – now in beta glow-up mode. Compatible with Brave, AdGuard, uBlock Origin, and any ABP-savvy tool.

Built by a jobless, noodle-fueled Vietnamese dev + his AI co-pilot (Grok 4.1 Thinking - Beta). Beta means alpha scars healed: Cleaner scripts, optimized wildcards, dup-proof raws. Still personal (my Reels-scroll rage), but less "cry at 4 AM."

---
## Features (Beta Upgrades)

- **Raw → Auto-Generated Flow**: No manual hell – add to raws, run scripts, get polished blocks/hides.
- **Full-Domain Blocking**: Tagged raws (e.g., [tracker] → $third-party) + wildcard merges (e.g., `blah.co.com` → `||co.com^$all`).
- **Per-Site Hiding**: Organized by domain, global *## first, dup selectors auto-nuked.
- **Bulk Tools**: Duplicate checkers (blocking/hiding), wildcard removers (up to 10 patterns, e.g., *.com, abc.*).
- **Exceptions**: Whitelist over-blocks without tears.
- **Beta Polish**: Learned from Dandelion Sprout's list – smarter rules, no more Ctrl+C/V drudgery.
- Updates: ~3–5 days (or when laptop/coffee/life allows).

---
## Update Frequency
- Update frequency: every 3–5 days (earlier or delayed due to health, file loss, or real-life issues)

---
## ⚠️ Experimental Features Warning (Beta Tester Only – Proceed at Your Own Risk)

These ***"experimental"*** rules/scripts _(e.g., aggressive cookie hides, wildcard tracking nukes, anti-porn blocks)_ 
are test-mode only – not for daily use yet. Beta standards mean:

- **Basic Beta Testing Rules**: Sandbox test (use incognito/VM), report bugs with details (URL, screenshot, error), no production/live use (e.g., work/banking sites), rollback easy (disable URL).
- **Not for Newbies/Non-Tech**: Already warned – if you're not comfy with DevTools or HTML/CSS tweaks, skip. This ain't beginner hour.
- **Potential Errors Galore**: Expect glitches like login fails, site no-load, payment errors, adblock detected, ads slipping through, videos not playing, etc. It's experimental – bugs happen.
- **Dev-Only Recommended**: For folks with basic source reading, DevTools basics, and HTML/CSS/JS knowledge (to spot/fix fast). Test *thoroughly* before apply – your setup, not mine.
- **Zero Responsibility**: Author (me) and Grok disclaim *everything*. No liability for breakage, data loss, or "my life ended because of a hidden button." Use = you own it.
- **P.S: You're an Unpaid Tester Now :v**: If you enable these, congrats – you're beta guinea pig. Feedback? Issue with facts (no fluff). Love ya for the risk!

Skip if unsure – core filters work fine without 'em.

---
## Repository Structure
```text
.
├── autoscript/                             # Magic wands (Grok-coded, bro-prompted)
│   ├── check_duplicates.py                 # Dup hunter for blocking raw
│   ├── check_hiding_duplicates.py          # Dup hunter for hiding raw (wildcard-proof)
│   ├── sort-and_count_everything_rules.py  # Sorts + counts rules (blocking + hiding)
│   └── bulk_remove_domains.py              # Multi-wildcard nuke (e.g., .com, abc.)
├── blocks/                                   # Blocking hell
│   ├── raws.txt                              # Plain domains + tags [full][tracker]
│   ├── raws_sorted.txt                       # Sorted raws (auto-generated)
│   ├── raws_clean.txt                            # Cleaned raws (auto-generated)
│   ├── full-block-domains.txt                # Generated full nukes
│   ├── full-block-domains_sorted.txt         # Sorted full nukes (auto-generated)
│   ├── block-tracking.txt                        # Tracking blocklist (raws → auto)
│   ├── block-tracking_sorted.txt                 # Sorted tracking blocklist (auto-generated
│   ├── cookie-consent-blocking.txt               # Cookie consent annoyances
│   ├── cookie-consent-blocking_sorted.txt        # Sorted cookie consent annoyances (auto-generated)
│   ├── download-blocking.txt                # Download nags blocklist (raws → auto)
│   ├── download-blocking_sorted.txt         # Sorted download nags blocklist (auto-generated)
│   ├── third-party-blocking.txt             # Third-party content blocklist (raws → auto)
│   ├── third-party-blocking_sorted.txt      # Sorted third-party content blocklist (auto-generated)
│   ├── advanced-block_sorted.txt     # Sorted advanced rules (auto-generated)
│   ├── advanced-block.txt            # Wildcard merges + complex rules (raws → auto)
│   ├── anti-porn.txt                 # Anti-porn domains blocklist (raws → auto)
│   └── anti-porn_sorted.txt          # Sorted anti-porn domains blocklist (auto-generated)
├── Hide/                                        # Hiding sanctuary
│   ├── hiding-raws.txt                          # Raw selectors (dump 'em here)
│   ├── hiding-raw_sorted.txt                    # Sorted raw selectors (auto-generated)
│   ├── cookie-consent-hiding.txt                # Cookie consent element hiders
│   └── cookie-consent-hiding_sorted.txt         # Sorted cookie consent hiders (auto-generated)
├── Exception/                        # Mercy zone (@@ whitelists)
│   └── exception.txt                # Whitelist (raw → auto)
│   └── exception_sorted.txt         # Sorted whitelist (auto-generated)
├── docs/                       # Legal armor (beta-polished)
│   ├── ACKNOWLEDGEMENTS.md     # Shoutouts (Grok MVP)
│   ├── DISCLAIMER.md           # "As is" reality check
│   ├── EULA.md                 # MIT with heart
│   ├── PrivacyPolicy.md        # Zero data vibes
│   ├── ToS.md                  # No-drama rules
│   └── SECURITY.md             # Bug bounties? Lol, report nicely
├── LICENSE                     # MIT – fork freely
├── CODE_OF_CONDUCT.md          # Code of conduct (be cool)
├── Contact.md                  # Get in touch (no spam, pls)
├── CONTRIBUTING.md             # How to help (fork + PR)
├── Personal-FAQ.md             # My personal FAQ (beta edition)
├── README.md                   # This file (beta edition)
└── CHANGELOG.md                # Update log (scam wars edition)
```
---
## How to Use (Even a Noob Can Do This)

1. Subscribe to the generated files (file `_sorted.txt`) (recommended):
   - Full block:
     ```text
     https://raw.githubusercontent.com/poli0981/Poli-Filter-Rules/refs/heads/main/blocks/full-block-domains_sorted.txt
     ```
   - Advanced block:
     ```text
     https://raw.githubusercontent.com/poli0981/Poli-Filter-Rules/refs/heads/main/blocks/advanced-block_sorted.txt
     ```
   - Hide:
     ```text
     https://raw.githubusercontent.com/poli0981/Poli-Filter-Rules/refs/heads/main/Hide/hiding-raws_sorted.txt
     ```
   - Exceptions:
     ```text
     https://raw.githubusercontent.com/poli0981/Poli-Filter-Rules/refs/heads/main/Exception/exception_sorted.txt
     ```
   - Cookie consent blockers/hiders:
     ```text
     https://raw.githubusercontent.com/poli0981/Poli-Filter-Rules/refs/heads/main/blocks/cookie-consent-blocking_sorted.txt
     ```
     ```text
     https://raw.githubusercontent.com/poli0981/Poli-Filter-Rules/refs/heads/main/Hide/cookie-consent-hiding_sorted.txt
     ```
     
   * **Experimental features:** See Wiki for details – use at your own risk.
   
    a. Tracking block:
    ```text
    https://raw.githubusercontent.com/poli0981/Poli-Filter-Rules/refs/heads/main/blocks/block-tracking_sorted.txt
    ```
    b. Download nags block:
    ```text
    https://raw.githubusercontent.com/poli0981/Poli-Filter-Rules/refs/heads/main/blocks/download-blocking_sorted.txt
    ```
   c. Third-party block:
    ```text
    https://raw.githubusercontent.com/poli0981/Poli-Filter-Rules/refs/heads/main/blocks/third-party-blocking_sorted.txt
    ```
   d. Anti-porn block: (you skip this rule if you want watch 18+ freely)
    ```text
    https://raw.githubusercontent.com/poli0981/Poli-Filter-Rules/refs/heads/main/blocks/anti-porn_sorted.txt
    ```
   
2. **Add to Your Adblocker**:
   - _Brave:_ Settings > Shields > Content Filtering > Custom lists > Paste URLs.
   - _AdGuard:_ Settings > Filters > Custom > Add URL.
   - _uBlock:_ Click extension icon > Open dashboard > Filter lists > Import > Paste URLs > Apply changes.
   - _Others:_ Google "add custom filter list [your tool]" – 10s job.

3. **Test & Tweak**: Reload sites, check for breakage. Over-block? Add @@ exceptions. Beta wildcards are strong – whitelist wisely.

## Auto Scripts (Run These, Thank Me Later)

```bash
# Blocking
cd autoscript
python sort_and_count_everything_rules.py  # Sort + count blocking + hiding rules with comments

# Or, for pure rules without comments:
python sort_and_count_everything_rules.py --pure-rules # Sort + count rules with comment removed

# Check Duplication (new beta toys)
python check_duplicates.py --remove          # Nuke blocking duplicates
python check_hiding_duplicates.py --domain=youtube.com --remove  # Hiding dups per site

# Bulk Remove Domains (up to 30 wildcards, e.g., *.com, abc.*)
python bulk_remove_domains.py                # Interactive wildcard purge
```
_Workflow:_ Edit raws > Run script > Commit raw + generated > PR if contributing. Zero manual sort forever.

---
## Development Stack (What Keeps This Alive)

- **IDEs**: PyCharm 2025.3 EAP + VS Code (daily grind tools).
- **AI Co-Pilot**: Grok 4.1 Thinking - Beta (~50% brainpower: scripts, docs, sanity).
- **Human**: Prompts, tests, noodle-fueled commits, search, add website (~50% regret).

---
## Contributing (Yes, You – Read Wiki First)

Solo + AI, but forks/PRs welcome. See `CONTRIBUTING.md` for bug reports (detailed, no fluff). CoC in `CODE_OF_CONDUCT.md` – be direct, no toxicity.

---
## Legal & Privacy (Beta Armor)

- **License**: MIT (fork freely, credit kindly)
- _No data collection_ whatsoever (static files only)
- Full docs in `/docs` folder:
- [EULA](docs/EULA.md) | [ToS](docs/ToS.md) | [Privacy Policy](docs/PrivacyPolicy.md) | [SECURITY](SECURITY.md)
- [Disclaimer](docs/DISCLAMER.md) | [Acknowledgements](docs/ACKNOWLEDGEMENTS.md)

---
## Acknowledgements (Shoutouts Section)

- See `ACKNOWLEDGEMENTS.md` – Grok MVP, Dandelion Sprout wizard, and y'all for not suing yet.
- Beta's our "good enough" milestone – thanks for the ride. Star if it cleans your web (or pities my soul). Feedback? Issues open, Wiki first.
- Built with spite, scripts, and a dash of hope.
- Make ads extinct, one rule at a time.

– The dev who's almost calling this "stable" (one more coffee...)

***Last updated:*** December 7, 2025.
