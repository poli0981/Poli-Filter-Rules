# sort_and_count_everything_rules.py - Updated: --pure-rules to skip comments entirely
import pathlib
from datetime import datetime
import argparse

# List files to process
FILES = [
    '/blocks/full-block-domains.txt',
    '/blocks/advanced-block.txt',
    '/blocks/download-blocking.txt',
    '/blocks/block-tracking.txt',
    '/blocks/cookie-consent-blocking.txt',
    '/blocks/third-party-blocking.txt',
    '/Hide/hiding-raws.txt',
    '/Hide/cookie-consent-hiding.txt',
    '/Exception/exception.txt',
    '/blocks/anti-porn.txt',
]

VERSION = "1.0.0-beta0.7.0"
TITLE = "Poli Filter Rules - [NaMe_of-List-Rules]"
AUTHOR = "poli0981 (with Grok's help)"
HOMEPAGE = "https://github.com/poli0981/Poli-Filter-Rules"
DESCRIPTION_LIST = "[Insert hErE] :v"
EXPIRE_TIME = "3 days"

def sort_and_count_file(input_path, output_path, pure_rules=False):
    """Sort lines (non-comment first), count pure rules, add header; --pure-rules skips comments"""
    if not input_path.exists():
        print(f"File {input_path} not found! Skipping.")
        return 0

    lines = input_path.read_text(encoding='utf-8').splitlines(keepends=True)
    comments = []
    rules = []  # Pure non-comment lines for sorting/count

    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith('!') or '!' in stripped:  # Strict: Ignore empty, ! start, or inline !
            if not pure_rules:
                comments.append(line)  # Keep if not pure
        else:
            rules.append(line.rstrip('\n'))  # Pure rule

    # Sort rules alphabetically (case-insensitive, keep original)
    rules.sort(key=lambda x: x.lower())

    # Write output
    with open(output_path, 'w', encoding='utf-8') as out:
        out.write(f'! Title: {TITLE}\n')
        out.write(f'! Version: {VERSION}\n')
        out.write(f'! Author: {AUTHOR}\n')
        out.write(f'! Generated: {datetime.now().strftime("%Y-%m-%d %H:%M")}\n')
        out.write(f'! Homepage: {HOMEPAGE}\n')
        out.write(f'! Expires: {EXPIRE_TIME}\n')
        out.write(f'! Description: {DESCRIPTION_LIST}\n')
        out.write(f'! Total Rules: {len(rules)} (non-comment only)\n')
        if pure_rules:
            out.write('! Mode: Pure rules (comments skipped)\n')
        out.write('\n')
        # Comments first (if not pure)
        if not pure_rules:
            for comment in comments:
                out.write(comment)
            out.write('\n')
        # Sorted rules
        for rule in rules:
            out.write(rule + '\n')

    return len(rules)

def main():
    parser = argparse.ArgumentParser(description="Sort & count block files – optional pure rules mode")
    parser.add_argument('--pure-rules', action='store_true', help="Skip comments entirely for clean rules-only output")
    args = parser.parse_args()

    print("Sorting & counting block files...")
    if args.pure_rules:
        print("(Pure mode: Comments skipped – rules only!)\n")
    total_rules = 0
    for file_path in FILES:
        path = pathlib.Path(file_path)
        output = path.with_name(path.stem + '_sorted.txt')
        count = sort_and_count_file(path, output, pure_rules=args.pure_rules)
        total_rules += count
        if count > 0:
            print(f"✅ {path.name}: {count} rules sorted → {output.name}")
        else:
            print(f"⚠️ {path.name}: No pure rules or file missing.")

    print(f"\nAll done! Total pure rules across files: {total_rules}")
    print("Tip: Run with --pure-rules for comment-free files. Commit _sorted.txt if clean!")

if __name__ == "__main__":
    main()