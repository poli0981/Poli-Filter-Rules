# check_duplicates.py  Better way to check for duplicate domains in raws.txt
import pathlib
import sys
from collections import Counter
from datetime import datetime

RAW_FILE = pathlib.Path('../blocks/raws_sorted.txt') # input file
BACKUP_FILE = RAW_FILE.with_suffix('.backup.txt') # backup if needed
OUTPUT_FILE = RAW_FILE.with_name(RAW_FILE.stem + '_clean.txt') # cleaned output

def extract_domain(line):
    """Extract domain from line, ignore comments/tags/spaces"""
    line = line.strip()
    if not line or line.startswith(('#', '!')):
        return None
    # Remove comment after #
    if '#' in line:
        line = line.split('#', 1)[0].strip()
    # Remove tags like [tracker] at end
    line = line.rstrip(']').rstrip('[').strip()
    # Take first word as domain
    parts = line.split()
    domain = parts[0].lower() if parts else None
    return domain

def main(remove_dups=False):
    if not RAW_FILE.exists():
        print(f"File {RAW_FILE} not found! Fix path.")
        return

    domains = []
    lines = RAW_FILE.read_text(encoding='utf-8').splitlines(keepends=True)  # Keep \n for spacing

    for line_num, line in enumerate(lines, 1):
        domain = extract_domain(line)
        if domain:
            domains.append((domain, line_num, line.rstrip('\n')))  # Store without trailing \n for print

    domain_counts = Counter(d[0] for d in domains)
    duplicates = {d: count for d, count in domain_counts.items() if count > 1}

    if duplicates:
        print(f"🚨 Found {len(duplicates)} duplicate domains in {RAW_FILE}:")
        for domain, count in sorted(duplicates.items()):
            line_nums = ', '.join(str(d[1]) for d in domains if d[0] == domain)
            print(f"  - {domain}: {count} times (lines: {line_nums})")
        print("\nOriginal lines with dups:")
        for domain, count in sorted(duplicates.items()):
            for d in [dd for dd in domains if dd[0] == domain]:
                print(f"  Line {d[1]}: {d[2]}")
    else:
        print("✅ No duplicates! Raw file is pristine (like my social life – non-existent).")

    if remove_dups and duplicates:
        # Backup original
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = RAW_FILE.with_name(f"{RAW_FILE.stem}_backup_{timestamp}.txt")
        backup_name.write_text(''.join(lines), encoding='utf-8')
        print(f"\n💾 Auto-backup created: {backup_name}")

        # Clean: Keep first occurrence + non-domain lines
        seen = set()
        clean_lines = []
        for line in lines:  # Keep original \n
            domain = extract_domain(line)
            if domain and domain not in seen:
                seen.add(domain)
                clean_lines.append(line)
            elif not domain:
                clean_lines.append(line)

        OUTPUT_FILE.write_text(''.join(clean_lines), encoding='utf-8')
        removed = len(lines) - len(clean_lines)
        print(f"\n🧹 Auto-removed {removed} duplicate lines. Clean file saved to {OUTPUT_FILE}")
        print(f"Clean file preview (first 10 lines):")
        preview = OUTPUT_FILE.read_text(encoding='utf-8').splitlines(keepends=False)[:10]
        for i, pline in enumerate(preview, 1):
            print(f"  {i}: {pline}")
        if len(preview) < 10:
            print(f"  (Total lines: {len(preview)})")
    elif remove_dups and not duplicates:
        print("\nℹ️ No dups to remove, but ran clean anyway. File unchanged.")
    else:
        print("\nℹ️ Run with --remove to auto-clean.")

if __name__ == "__main__":
    remove = len(sys.argv) > 1 and sys.argv[1] == '--remove'
    main(remove_dups=remove)