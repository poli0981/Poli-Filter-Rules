# organize_hiding.py - auto organize hiding rules from hiding.txt into grouped sections by domain
import pathlib
from datetime import datetime
import re

INPUT_FILE = pathlib.Path('../Hide/hiding-raws.txt')
OUTPUT_FILE = pathlib.Path('../Hide/organized-hiding.txt')

groups = {}  # key = domain lower, value = list (domain_display, original_rule)
header_comments = []  # save header comments

with INPUT_FILE.open('r', encoding='utf-8') as f:
    for line in f:
        stripped = line.strip()
        if not stripped or stripped.startswith('!'):
            header_comments.append(line.rstrip('\n'))
            continue

        # Detect separator: ## or #$# or ##+js or ##^ or @@##
        match = re.match(r'^(@@)? ?([^#$\n]*?) ?(##|\#$#|##\^|##\+js).*', stripped)
        if match:
            exception_prefix = match.group(1) or ''  # @@ if any
            domain_part = match.group(2).strip()  # domain or * or empty
            # If domain_part is empty, treat as global
            if not domain_part:
                domain_key = '*'
                domain_display = '*'
            else:
                domain_key = domain_part.lower()
                domain_display = domain_part

            groups.setdefault(domain_key, []).append((domain_display, stripped))
        else:
            # Rule not match or no domain specified, treat as global
            groups.setdefault('*', []).append(('*', stripped))

# Sort rules within each group A-Z
for key in groups:
    groups[key].sort(key=lambda x: x[1].lower())

# Sort domain: global (*) first, then A-Z
sorted_keys = sorted(groups.keys())
if '*' in sorted_keys:
    sorted_keys.remove('*')
    sorted_keys.insert(0, '*')

total_rules = sum(len(rules) for rules in groups.values())

with OUTPUT_FILE.open('w', encoding='utf-8') as out:
    out.write('! Organized Hiding Rules - Auto Generated\n')
    out.write(f'! Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M")}\n')
    out.write('! Source: hiding-raws.txt\n')
    out.write(f'! Total hiding rules: {total_rules}\n\n')

    # Header roots comments
    for comment in header_comments:
        out.write(comment + '\n')
    out.write('\n')

    # Global section
    for domain_display, rule in groups.get('*', []):
        out.write(rule + '\n')
    out.write('\n')  # blank line after global

    # Other domains
    for key in sorted_keys:
        if key == '*':
            continue
        out.write(f'! --- {groups[key][0][0]} ---\n')  # domain_display as header
        for _, rule in groups[key]:
            out.write(rule + '\n')
        out.write('\n')

print(f"Done! Generated {OUTPUT_FILE} with {total_rules} rules! 🚀")