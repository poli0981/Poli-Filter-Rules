# sort-raws-block.py - Sort raws.txt alphabetically (domains first, keep comments/tags)
import pathlib
from datetime import datetime

RAW_FILE = pathlib.Path('../blocks/raws.txt')  # Adjust path as needed
SORTED_FILE = RAW_FILE.with_name('raws_sorted.txt')

def parse_raw_line(line):
    """Parse line: domain [tag] # comment → (domain, tag, comment, full_line)"""
    line = line.strip()
    if not line or line.startswith(('#', '!')):
        return None, None, None, line  # Comment/full comment
    # Split tag/comment
    parts = line.split('#', 1)
    domain_part = parts[0].strip()
    comment = (' # ' + parts[1].strip()) if len(parts) > 1 else ''
    # Split domain [tag]
    if '[' in domain_part and ']' in domain_part:
        domain, tag_part = domain_part.rsplit('[', 1)
        tag = '[' + tag_part.split(']', 1)[0] + ']'
    else:
        domain = domain_part
        tag = ''
    return domain.lower(), tag, comment, line

def main():
    if not RAW_FILE.exists():
        print(f"File {RAW_FILE} not found!")
        return

    # Group: non-domain lines first, then domains sorted
    comments = []
    domain_entries = []  # (domain_key, full_line)

    with open(RAW_FILE, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            domain_key, tag, comment, full_line = parse_raw_line(line)
            if domain_key is None:
                comments.append(full_line.rstrip())
            else:
                domain_entries.append((domain_key, full_line.rstrip()))

    # Sort domains A-Z
    domain_entries.sort(key=lambda x: x[0])

    # Write sorted
    with open(SORTED_FILE, 'w', encoding='utf-8') as out:
        out.write('! Sorted Raws – Generated from raws.txt\n')
        out.write(f'! Sorted on: {datetime.now().strftime("%Y-%m-%d %H:%M")}\n\n')
        # Comments first
        for comment in comments:
            out.write(comment + '\n')
        out.write('\n')
        # Sorted domains
        for _, full_line in domain_entries:
            out.write(full_line + '\n')

    total_domains = len(domain_entries)
    print(f"✅ Sorted {total_domains} domains! Output: {SORTED_FILE}")
    print("Preview (first 5 lines):")
    with open(SORTED_FILE, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            if i > 5:
                break
            print(f"  {i}: {line.rstrip()}")

if __name__ == "__main__":
    main()