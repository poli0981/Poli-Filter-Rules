# Custom Adblock Filter List

[![Version](https://img.shields.io/badge/version-1.0--alpha0-blue.svg)](https://github.com/poli0981/my-content-blocker)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Updates](https://img.shields.io/badge/updates-every%203%20days-orange.svg)](https://github.com/poli0981/my-content-blocker/commits/main)

## Overview
This repository contains a personal collection of adblock filters designed to block advertisements, trackers, and hide unwanted CSS elements (such as footers, promotions, cookie notices, chatbots, and more) on various websites. It's compatible with tools like Brave Browser, AdGuard, uBlock Origin, and other adblockers that support AdBlock Plus (ABP) syntax.

This is an early-stage project (version 1.0-alpha0), built as a solo endeavor with AI assistance. It's based on personal web browsing experiences and may not suit everyone. Feel free to fork and customize!

## Features
- **Blocking Rules**: Filters to block ad/tracker domains and URLs (e.g., Google Ads, Facebook trackers).
- **Element Hiding**: CSS selectors to hide annoying elements like cookie banners, app download prompts, chatbots, and Facebook widgets (excluding facebook.com itself).
- **Modular Structure**: Filters are split into separate files for better management:
  - `blocking.txt`: Domain/URL blocking rules.
  - `hiding.txt`: CSS element hiding rules.
  - (Optional) `cosmetic.txt`: Advanced style modifications.
  - (Optional) `exceptions.txt`: Whitelists to prevent over-blocking.
- **Easy Integration**: Subscribe via raw GitHub URLs for auto-updates.

## How to Use
1. **Subscribe in Your Adblocker**:
   - Get the raw URL for each file (e.g., `https://raw.githubusercontent.com/yourusername/custom-adblock-list/main/blocking.txt`).
   - In Brave: Settings > Shields > Content Filtering > Add custom filter list.
   - In AdGuard: Settings > Filters > Custom > Add filter URL.
   - In uBlock Origin: Dashboard > Filter Lists > Import URL.

2. **Testing and Customization**:
   - Apply the lists and reload target websites.
   - Use browser DevTools (F12) to inspect elements and create new rules.
   - If a rule breaks a site, add exceptions in `exceptions.txt` (e.g., `@@||example.com^$document`).

3. **Updating**:
   - The repo will be updated approximately every 3 days (barring any issues).
   - Your adblocker should auto-pull changes if subscribed to raw URLs.

## Structure
- `/blocking.txt`: Rules for blocking ad/tracker requests.
- `/hiding.txt`: Rules for hiding CSS elements.
- `/LICENSE`: MIT License (or your chosen license).
- `/README.md`: This file.
- `/ACKNOWLEDGEMENTS.md`: Credits and contributions.
- `/DISCLAIMER.md`: Important disclaimers.

## Contributing
This is a personal project, but contributions are welcome! Fork the repo, add your rules, and submit a pull request. Please test changes and follow ABP syntax.

## Support
If you encounter issues, open an GitHub issue or tweak the rules yourself. For syntax help, refer to [AdBlock Plus Filter Syntax](https://help.eyeo.com/adblockplus/how-to-write-filters).

---
*Built with ❤️ by a solo developer with AI assistance.*