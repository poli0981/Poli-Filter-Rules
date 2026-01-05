# Poli-Filter-Rules - Personal Content Blocker Filter List

[![Version](https://img.shields.io/badge/version-1.0.1-blue.svg)](https://github.com/poli0981/Poli-Filter-Rules)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Updates](https://img.shields.io/badge/updates-every%203%20days-orange.svg)](https://github.com/poli0981/Poli-Filter-Rules/commits/main)
[![Stars](https://img.shields.io/github/stars/poli0981/Poli-Filter-Rules?style=social)](https://github.com/poli0981/Poli-Filter-Rules)

A modular, auto-generated adblock filter list for nuking ads, trackers, popups, cookie banners, and whatever else annoys me on the web. Compatible with Brave, AdGuard, uBlock Origin, and any ABP tool.

Built by a jobless, noodle-powered Vietnamese dev (20-something, guess the age) + his AI best friend (Grok). 1.0 means we survived alpha chaos and beta tweaks – now "official" (or as official as a broke guy's spite project gets). Still personal (my rage at Facebook Reels gambling spam), but polished enough to call stable.

## Features (1.0 Glow-Up)

- **Raw → Auto-Magic**: Edit raws > Run scripts > Clean/sorted/generated files. No manual drudgery.
- **Full-Domain Blocking**: Tagged raws + wildcard merges (e.g., `||co.com^$all` for sub-spam).
- **Per-Site Hiding**: Domain-grouped, dup-free, global `*##` first.
- **Bulk Tools**: Dup checkers (blocks/hides), wildcard bulk remover (up to 10 patterns), param extractor for $removeparam.
- **Modules**: Cookie consent (block/hide), tracking, download nags, third-party embeds, anti-porn (toggle :D).
- **Experimental Toys**: Volatile extras (test sandbox – unpaid tester mode :v).
- **Auto-Updates**: GitHub Actions sort/count every ~3 days – always fresh.
- **1.0 Polish**: 3000+ rules, scripts streamlined, docs remade.

---
## Update Frequency
- **Update frequency:** every ~3 days via ***GitHub Actions*** (auto-sort/count).
- **Manual updates:** Fork, edit raws, run scripts, PR.
- **Non-tech users:** Subscribe to generated `_sorted.txt` files (URLs in "How to Use" section).

---

## Repository Structure
```text
.
├── autoscript/                             # Magic wands (Grok-coded, bro-prompted)
│   ├── check_duplicates.py                 # Dup hunter for blocking raw
│   ├── check_hiding_duplicates.py          # Dup hunter for hiding raw (wildcard-proof)
│   ├── sort-and_count_everything_rules.py  # Sorts + counts rules (blocking + hiding)
│   ├── param_extractor.py                  # $removeparam helper (file input)
│   ├── dns_block_generator.py              # Blocks for hosts file (0.0.0.0 default)
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
├── README.md                   # This file (beta edition)
└── CHANGELOG.md                # Update log (scam wars edition)
```

---
## How to Use (2 Minutes – Non-Tech OK)

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

3. **Test**: Reload sites. Ads gone? Yay. Break? Wiki/Troubleshooting (add exception).

**Modules**: Start core (full/advanced/hides/exceptions). Add extras (tracking/cookie) one-by-one – test each.

## Auto Scripts (Dev Toys – Optional Power)

Run in autoscript/ folder (Python 3 needed).

- `python sort_and_count_everything_rules.py` – Sorts/counts all rules, adds headers.
- `python check_duplicates.py --remove` – Dup hunt blocks.
- `python check_hiding_duplicates.py --remove` – Dup hunt hides.
- `python bulk_remove_domains.py` – Interactive wildcard purge.
- `python param_extractor.py` – $removeparam helper (file input).
- `python dns_block_generator.py` – 0.0.0.0 lines for hosts.

Non-tech? Skip – subscribe sorted URLs.

## Development Stack

- IDEs: PyCharm 2025.3 EAP + VS Code.
- AI Co-Pilot: Grok (Thinking Beta) – ~50% brain, scripts, docs, sanity.
- Human: Prompts, tests, noodle commits – ~50% regret.

## Contributing (Welcome – Read CONTRIBUTING.md)

Fork > Edit raws > Run scripts > Commit raw + generated > PR with template. Issues with template (bug/feature/add-remove/feedback/off-topic).

---
## Legal & Privacy

- **License**: MIT (fork freely, credit kindly)
- _No data collection_ whatsoever (static files only)
- Full docs in `/docs` folder:
- [EULA](docs/EULA.md) | [ToS](docs/ToS.md) | [Privacy Policy](docs/PrivacyPolicy.md) | [SECURITY](SECURITY.md)
- [Disclaimer](docs/DISCLAMER.md) | [Acknowledgements](docs/ACKNOWLEDGEMENTS.md)

---
## Acknowledgements

See [ACKNOWLEDGEMENTS.md](docs/ACKNOWLEDGEMENTS.md) – Grok MVP, inspirations, silent supporters.

1.0 shipped on "birthday" (+1 age, zero fanfare). Thanks for ride – web sucks less now.

Star if it helps (or pities). Feedback? Issues (Wiki first).

Built with spite, scripts, coffee, and hope. Ads extinct, one rule at a time.

– The dev who's "stable" now (lies :v)

---
Last Updated: January 2, 2026
