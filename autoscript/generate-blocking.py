# generate_blocks.py - auto generate full domain blocking list from raw domains with tag(s)
import pathlib
from datetime import datetime

RAW_FILE = pathlib.Path('../blocks/raws_clean.txt')
OUTPUT_FILE = pathlib.Path('../blocks/full-block-domains.txt')

domains = []

with RAW_FILE.open('r', encoding='utf-8') as f:
    for raw_line in f:
        line = raw_line.strip()
        if not line or line.startswith(('#', '!')):
            continue

        # Split comment if any
        if '#' in line:
            domain_part, comment = line.split('#', 1)
            comment = '  ! ' + comment.strip()
        else:
            domain_part = line
            comment = ''

        domain_part = domain_part.strip()

        # Extract tag [tracker] / [popup] / [full]...
        tag = ''
        if '[' in domain_part and ']' in domain_part:
            # Use regex to find the last [...] at the end of the string
            import re

            match = re.search(r'\[([^]]+)\]$', domain_part)  # only last []
            if match:
                tag = match.group(1).strip().lower()
                # Delete the tag from domain_part
                domain_part = domain_part[:match.start()].strip()

        domain = domain_part.strip()
        if domain:
            domains.append((domain, tag, comment))

# Sort domains A-Z
domains.sort(key=lambda x: x[0])

with OUTPUT_FILE.open('w', encoding='utf-8') as out:
    out.write('! Full Domain Block List - Auto Generated\n')
    out.write(f'! Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M")}\n')
    out.write('! Source: raws.txt\n')
    out.write(f'! Total domains: {len(domains)}\n\n')

    for domain, tag, comment in domains:
        if tag == 'tracker':
            option = 'important,third-party'
        elif tag == 'popup':
            option = 'important,popup'
        elif tag == 'all':
            option  = 'all'
        elif tag == 'full' or not tag:
            option = 'important'
        else:
            option = 'important'  # fallback

        out.write(f'||{domain}^${option}{comment}\n')

print(f"Generated {OUTPUT_FILE} with {len(domains)} rules! 🚀")