# Poli-Filter-Rules - Personal Content Blocker Filter List

[![Version](https://img.shields.io/badge/version-1.0--alpha5-blue.svg)](https://github.com/poli0981/Poli-Filter-Rules)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Updates](https://img.shields.io/badge/updates-every%203%20days-orange.svg)](https://github.com/poli0981/my-content-blocker/commits/main)

## Overview

- A highly modular, auto-generated, and meticulously organized personal adblock filter list designed for Brave, AdGuard, uBlock Origin, and any AdBlock Plus-compatible extension.
- Built as a solo project with heavy AI assistance (Grok 4.1 Thinking - Beta), this list focuses on real-world annoyances: aggressive ads, trackers, cookie banners, app download nags, chatbots, Facebook widgets, and full-domain blocks for particularly toxic sites.
- Version 1.0-alpha1 marks the transition to fully English documentation and a professional repository structure suitable for international use.

## Features

- Raw → auto-generated workflow (no manual sorting ever again)
- Full-domain blocking with reasons & tags
- Per-site CSS hiding rules, automatically organized by domain
- Exception list for over-blocking protection
- Scripts for generation & organization included
- All legal docs (EULA, ToS, Privacy Policy, etc.)

## Current Version
- Version: 1.0-alpha1
- Release Date: November 21, 2025
- Changelog: [CHANGELOG.md](CHANGELOG.md)

## Update Frequency
- Update frequency: every 3–5 days (may be earlier or delayed due to health, file loss, or real-life issues)

## Repository Structure
```text
.
├── autoscript/
│   ├── generate-blocking.py      # raw → full-block-domains.txt + advanced-block.txt
│   └── organize-hiding.py        # hiding-raws.txt → organized-hiding.txt (grouped by domain)
├── blocks/
│   ├── raws.txt                  # plain domain list with optional tags "[tracker][popup][full]"
│   ├── full-block-domains.txt    # auto-generated ||domain^$important,...
│   └── advanced-block.txt        # manual complex blocking rules
├── Hide/
│   ├── hiding-raws.txt           # raw CSS selectors (free-form input)
│   └── organized-hiding.txt      # auto-generated, grouped & sorted by domain
├── Exception/
│   └── exception.txt
├── docs/
│   ├── ACKNOWLEDGEMENTS.md
│   ├── DISCLAIMER.md
│   ├── EULA.md
│   ├── PrivacyPolicy.md
│   └── ToS.md
├── LICENSE                       # MIT License
└── README.md
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

2. Or subscribe to the whole repo as multiple custom lists in your preferred adblocker.

Auto-update works instantly on GitHub raw URLs.

## Auto Scripts (Super Convenient)

```bash
# Blocking rules
python autoscript/generate-blocking.py

# Hiding rules (run after adding to hiding-raws.txt)
python autoscript/organize-hiding.py
```
_Just commit the raw files → run scripts → commit generated files. Zero manual sorting forever._


## Development Stack

- ***IDEs***: PyCharm 2025.3 EAP + Visual Studio Code
- ***AI Assistant***: Grok 4.1 Thinking - Beta (xAI) – ~50% of documentation, script logic, rule suggestions, debugging, and organization ideas
- Human: prompt engineering, rule writing, testing, final decisions, health management :)

## Contributing

- This is primarily a solo project, but contributions are very welcome!
- Fork → add rules to raw files → run scripts → open PR with both raw + generated files.
- Please include reason in comments and test on real sites.
- Issues & suggestions are always appreciated.

## Legal & Privacy

- **License**: MIT (permissive – use anywhere)
- _No data collection_ whatsoever (static files only)
- Full docs in `/docs` folder:
- [EULA](docs/EULA.md) | [ToS](docs/ToS.md) | [Privacy Policy](docs/PrivacyPolicy.md)
- [Disclaimer](docs/DISCLAMER.md) | [Acknowledgements](docs/ACKNOWLEDGEMENTS.md)


## Acknowledgements

- Special thanks to _Grok 4.1 Thinking - Beta_ for being an incredible co-pilot: writing documentation, fixing bugs in seconds, suggesting smart script architecture, and keeping the project moving even when I was tired or sick.
- Couldn't have reached 1.0-alpha1 this fast without you, bro.

Built with passion, automation, and a bit of AI magic.
Feedback? Open an issue – let's make the web suck less, together.

**Last updated:** _November 21, 2025._
