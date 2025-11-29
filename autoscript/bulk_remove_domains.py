# bulk_remove_domains.py - Updated: Multi-pattern bulk remove (up to 10 wildcards at once)
import pathlib
import fnmatch
import sys
from datetime import datetime

RAW_FILE = pathlib.Path('../blocks/raws_sorted.txt')  # Adjust path as needed
CLEAN_FILE = RAW_FILE.with_name(RAW_FILE.stem + '_clean.txt')

def extract_domain(line):
    """Extract domain from raw line (ignore comments/tags)"""
    line = line.strip()
    if not line or line.startswith(('#', '!')):
        return None
    # Remove comment after #
    if '#' in line:
        line = line.split('#', 1)[0].strip()
    # Remove tags like [full] at end
    line = line.rstrip(']').rstrip('[').strip()
    # Take domain (first word, handle wildcards if any)
    domain = line.split()[0].strip() if line else None
    return domain

def main():
    if not RAW_FILE.exists():
        print(f"File {RAW_FILE} not found! Fix path.")
        return

    lines = RAW_FILE.read_text(encoding='utf-8').splitlines(keepends=True)
    print(f"Loaded {len(lines)} lines from {RAW_FILE}. Ready for multi-pattern hunt (max 30).\n")

    while True:
        patterns_input = input("Enter comma-separated patterns (e.g. '*.com, *.abc.xyz, abc.*') or 'quit': ").strip()
        if patterns_input.lower() == 'quit':
            print("Bye! Raw list stays as is.")
            break
        if not patterns_input:
            print("No patterns? Try again.")
            continue

        patterns = [p.strip() for p in patterns_input.split(',') if p.strip()]
        if len(patterns) > 30:
            print("⚠️ Too many patterns (max 30). Shorten and try again.")
            continue
        if len(patterns) == 0:
            print("No valid patterns. Try again.")
            continue

        matched_lines = {}  # {pattern: [(line_num, line)]}
        all_matched = 0
        no_match_patterns = []

        for pattern in patterns:
            matched = []
            for line_num, line in enumerate(lines, 1):
                domain = extract_domain(line)
                if domain and fnmatch.fnmatch(domain, pattern):
                    matched.append((line_num, line.rstrip('\n')))
            matched_lines[pattern] = matched
            count = len(matched)
            all_matched += count
            if count == 0:
                no_match_patterns.append(pattern)

        if no_match_patterns:
            print(f"❌ Some patterns no match: {', '.join(no_match_patterns)}")
            retry = input("Check spelling/wildcards and retry these? (y/n/skip all): ").strip().lower()
            if retry == 'y':
                continue  # Loop to re-input
            elif retry == 'n':
                print("Skipping all. No changes.\n")
                continue
            else:  # skip all
                pass

        if all_matched == 0:
            print("No matches at all. Check patterns and try again.\n")
            continue

        # List all matches grouped by pattern
        print(f"\n✅ Found {all_matched} total matches across {len(patterns)} patterns:")
        for pattern, matches in matched_lines.items():
            if matches:
                print(f"  Pattern '{pattern}': {len(matches)} matches")
                for line_num, line in matches:
                    print(f"    Line {line_num}: {line}")
            else:
                print(f"  Pattern '{pattern}': 0 matches (skipped)")

        confirm = input(f"\nDelete these {all_matched} lines across all patterns? (y/n): ").strip().lower()
        if confirm != 'y':
            print("Skipped. No changes made.\n")
            continue

        # Backup
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = RAW_FILE.with_name(f"{RAW_FILE.stem}_backup_{timestamp}.txt")
        backup_name.write_text(''.join(lines), encoding='utf-8')
        print(f"💾 Auto-backup created: {backup_name}")

        # Collect all line_nums to remove (unique)
        remove_nums = set()
        for matches in matched_lines.values():
            for line_num, _ in matches:
                remove_nums.add(line_num)

        # Clean
        clean_lines = [line for line_num, line in enumerate(lines, 1) if line_num not in remove_nums]
        CLEAN_FILE.write_text(''.join(clean_lines), encoding='utf-8')
        removed = len(remove_nums)
        print(f"\n🧹 Removed {removed} unique lines across patterns. Clean file saved to {CLEAN_FILE}")
        print("Clean file preview (first 10 lines):")
        preview = CLEAN_FILE.read_text(encoding='utf-8').splitlines()[:10]
        for i, pline in enumerate(preview, 1):
            print(f"  {i}: {pline}")
        print(f"\nTotal lines now: {len(clean_lines)} (was {len(lines)}). Commit this if happy!\n")

if __name__ == "__main__":
    main()