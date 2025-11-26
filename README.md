# Poli-Filter-Rules - Personal Content Blocker Filter List

[![Version](https://img.shields.io/badge/version-1.0.0-beta0-blue.svg)](https://github.com/poli0981/Poli-Filter-Rules)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Updates](https://img.shields.io/badge/updates-every%203%20days-orange.svg)](https://github.com/poli0981/my-content-blocker/commits/main)

#A modular, auto-generated adblock filter list for nuking ads, trackers, popups, and annoyances – now in beta glow-up mode. Compatible with Brave, AdGuard, uBlock Origin, and any ABP-savvy tool.

Built by a jobless, noodle-fueled Vietnamese dev + his AI co-pilot (Grok 4.1 Thinking - Beta). Beta means alpha scars healed: Cleaner scripts, optimized wildcards, dup-proof raws. Still personal (my Reels-scroll rage), but less "cry at 4 AM."

## Features (Beta Upgrades)

- **Raw → Auto-Generated Flow**: No manual hell – add to raws, run scripts, get polished blocks/hides.
- **Full-Domain Blocking**: Tagged raws (e.g., [tracker] → $third-party) + wildcard merges (e.g., blah.co.com → ||co.com^$all).
- **Per-Site Hiding**: Organized by domain, global *## first, dup selectors auto-nuked.
- **Bulk Tools**: Duplicate checkers (blocking/hiding), wildcard removers (up to 10 patterns, e.g., *.com, abc.*).
- **Exceptions**: Whitelist over-blocks without tears.
- **Beta Polish**: Learned from Dandelion Sprout's list – smarter rules, no more Ctrl+C/V drudgery.
- Updates: ~3–5 days (or when laptop/coffee/life allows).

## Update Frequency
- Update frequency: every 3–5 days (may be earlier or delayed due to health, file loss, or real-life issues)

## Repository Structure
```text
.
├── autoscript/                 # Magic wands (Grok-coded, bro-prompted)
│   ├── generate-blocking.py    # raws.txt → full/advanced blocks
│   ├── organize-hiding.py      # hiding-raws.txt → organized hides
│   ├── check_duplicates.py     # Dup hunter for blocking raw
│   ├── check_hiding_duplicates.py # Dup hunter for hiding raw (wildcard-proof)
│   └── bulk_remove_domains.py  # Multi-wildcard nuke (e.g., .com, abc.)
├── blocks/                     # Blocking hell
│   ├── raws.txt                # Plain domains + tags [full][tracker]
│   ├── full-block-domains.txt  # Generated full nukes
│   └── advanced-block.txt      # Wildcard merges + complex rules
├── Hide/                       # Hiding sanctuary
│   ├── hiding-raws.txt         # Raw selectors (dump 'em here)
│   └── organized-hiding.txt    # Generated, domain-grouped, dup-free
├── Exception/                  # Mercy zone
│   └── exception.txt           # @@ whitelists
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

## How to Use

1. Subscribe to the generated files (recommended):
   - Full block:
     ```text
     https://raw.githubusercontent.com/poli0981/Poli-Filter-Rules/refs/heads/main/blocks/full-block-domains.txt
     ```
   - Advanced block:
     ```text
     https://raw.githubusercontent.com/poli0981/Poli-Filter-Rules/refs/heads/main/blocks/advanced-block.txt
     ```
   - Organized hiding:
     ```text
     https://raw.githubusercontent.com/poli0981/Poli-Filter-Rules/refs/heads/main/Hide/organized-hiding.txt
     ```
   - Exceptions:
     ```text
     https://raw.githubusercontent.com/poli0981/Poli-Filter-Rules/refs/heads/main/Exception/exception.txt
     ```

2. **Add to Your Adblocker**:
   - Brave: Settings > Shields > Content Filtering > Custom lists > Paste URLs.
   - AdGuard: Settings > Filters > Custom > Add URL.
   - uBlock: Dashboard > My filters > Import.
   - Others: Google "add custom filter list [your tool]" – 10s job.

3. **Test & Tweak**: Reload sites, check for breakage. Over-block? Add @@ exceptions. Beta wildcards are strong – whitelist wisely.

## Auto Scripts (Super Convenient)
## Auto Scripts (Run These, Thank Me Later)

```bash
# Blocking
cd autoscript
python generate-blocking.py  # raws → blocks (after edits)

# Hiding
python organize-hiding.py    # raws → organized

# Cleaners (new beta toys)
python check_duplicates.py --remove          # Nuke blocking dups
python check_hiding_duplicates.py --domain=youtube.com --remove  # Hiding dups per site
python bulk_remove_domains.py                # Interactive wildcard purge
```
Workflow: Edit raws > Run script > Commit raw + generated > PR if contributing. Zero manual sort forever.

## Development Stack

- **IDEs**: PyCharm 2025.3 EAP + VS Code (daily grind tools).
- **AI Co-Pilot**: Grok 4.1 Thinking - Beta (~50% brainpower: scripts, docs, sanity).
- **Human**: Prompts, tests, noodle-fueled commits, search, add website (~50% regret).

## Contributing

Solo + AI, but forks/PRs welcome. See `CONTRIBUTING.md` for bug reports (detailed, no fluff). CoC in `CODE_OF_CONDUCT.md` – be direct, no toxicity.

## Legal & Privacy

- **License**: MIT (permissive – use anywhere)
- _No data collection_ whatsoever (static files only)
- Full docs in `/docs` folder:
- [EULA](docs/EULA.md) | [ToS](docs/ToS.md) | [Privacy Policy](docs/PrivacyPolicy.md)
- [Disclaimer](docs/DISCLAMER.md) | [Acknowledgements](docs/ACKNOWLEDGEMENTS.md)


## Acknowledgements

- See ACKNOWLEDGEMENTS.md – Grok MVP, Dandelion Sprout wizard, and y'all for not suing yet.
- Beta's our "good enough" milestone – thanks for the ride. Star if it cleans your web (or pities my soul). Feedback? Issues open, Wiki first.
- Built with spite, scripts, and a dash of hope.
- Make ads extinct, one rule at a time.

– The dev who's almost calling this "stable" (one more coffee...)

**Last updated:** _November 26, 2025._
