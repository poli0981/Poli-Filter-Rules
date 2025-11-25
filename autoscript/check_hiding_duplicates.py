# check_hiding_duplicates.py - Fixed: Wildcard domains (e.g. site.*) now match properly
import pathlib
import sys
import re
from collections import defaultdict, Counter
from datetime import datetime

RAW_FILE = pathlib.Path('../Hide/hiding-raws.txt')  # Input file path
BACKUP_FILE = RAW_FILE.with_suffix('.backup.txt')
OUTPUT_FILE = RAW_FILE.with_name(RAW_FILE.stem + '_clean.txt')

def parse_hiding_rule(line):
    """Parse domain and selector from hiding rule"""
    line = line.strip()
    if not line or line.startswith('!'):
        return None, None  # Comment/header, skip
    # Fixed regex: Allow * in domain (e.g. site.*##selector), stop at sep
    match = re.match(r'(?P<exception>@@)?\s*(?P<domain>[^##\s#$]+|\*)?\s*(?P<sep>##|\#$#|##\^|##\+js)\s*(?P<selector>.*)', line)
    if match:
        domain = match.group('domain') or '*'
        selector = match.group('sep') + match.group('selector')  # Keep sep + selector as key for dup check
        return domain.lower(), selector.strip()
    return None, None  # Invalid line, treat as non-rule

def main(domain_filter=None, remove_dups=False):
    if not RAW_FILE.exists():
        print(f"File {RAW_FILE} not found! Fix path.")
        return

    rules_by_domain = defaultdict(list)  # {domain: [(line_num, full_line, selector)]}
    lines = RAW_FILE.read_text(encoding='utf-8').splitlines(keepends=True)
    matched_rules = 0  # Counter for filtered domain

    domain_filter_lower = domain_filter.lower() if domain_filter else None  # Lower for case-insensitive match

    for line_num, line in enumerate(lines, 1):
        domain, selector = parse_hiding_rule(line)
        if domain:
            if domain_filter_lower and domain != domain_filter_lower:
                continue  # Skip if filtering specific domain
            rules_by_domain[domain].append((line_num, line.rstrip('\n'), selector))
            matched_rules += 1

    # Check if domain_filter set but no matches
    if domain_filter_lower and matched_rules == 0:
        print(f"❌ Domain '{domain_filter}' not found in list. Please check spelling and try again.")
        return

    dups_found = False
    for domain, rules in rules_by_domain.items():
        selector_counts = Counter(r[2] for r in rules)
        domain_dups = {sel: count for sel, count in selector_counts.items() if count > 1}
        if domain_dups:
            dups_found = True
            print(f"🚨 Domain '{domain}': {len(domain_dups)} duplicate selectors:")
            for sel, count in sorted(domain_dups.items()):
                line_nums = ', '.join(str(r[0]) for r in rules if r[2] == sel)
                print(f"  - '{sel}': {count} times (lines: {line_nums})")
            print(f"Original lines with dups for '{domain}':")
            for r in [rr for rr in rules if rr[2] in domain_dups]:
                print(f"  Line {r[0]}: {r[1]}")

    if not dups_found:
        if domain_filter:
            print(f"✅ No duplicate selectors for '{domain_filter}'! Clean as a whistle.")
        else:
            print("✅ No duplicate selectors! Hiding rules are clean (miracle).")
        return

    print(f"\nFound duplicates across {len(rules_by_domain)} domains. Total rules checked: {sum(len(r) for r in rules_by_domain.values())}")

    if remove_dups:
        # Backup
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = RAW_FILE.with_name(f"{RAW_FILE.stem}_backup_{timestamp}.txt")
        backup_name.write_text(''.join(lines), encoding='utf-8')
        print(f"\n💾 Auto-backup created: {backup_name}")

        # Clean: Keep first occurrence per selector per domain + non-rule lines
        seen_selectors = defaultdict(set)
        clean_lines = []
        for line in lines:
            domain, selector = parse_hiding_rule(line)
            if domain:
                if domain_filter_lower and domain != domain_filter_lower:
                    clean_lines.append(line)  # Keep if not filtering
                    continue
                if selector not in seen_selectors[domain]:
                    seen_selectors[domain].add(selector)
                    clean_lines.append(line)
                # Else: dup, skip
            else:
                clean_lines.append(line)  # Keep comments/empty

        OUTPUT_FILE.write_text(''.join(clean_lines), encoding='utf-8')
        removed = len(lines) - len(clean_lines)
        print(f"\n🧹 Auto-removed {removed} duplicate lines. Clean file saved to {OUTPUT_FILE}")
        print("Clean file preview (first 10 lines):")
        preview = OUTPUT_FILE.read_text(encoding='utf-8').splitlines()[:10]
        for i, pline in enumerate(preview, 1):
            print(f"  {i}: {pline}")
    else:
        print("\nℹ️ Run with --remove to auto-clean, or --domain=example.com to filter one site.")

if __name__ == "__main__":
    domain_filter = None
    remove = False
    for arg in sys.argv[1:]:
        if arg.startswith('--domain='):
            domain_filter = arg.split('=')[1]
        elif arg == '--remove':
            remove = True
    main(domain_filter=domain_filter, remove_dups=remove)