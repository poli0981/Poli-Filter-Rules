# dns_block_generator.py - Updated: File input (one domain per line)
import pathlib
from datetime import datetime
import argparse

DEFAULT_INPUT_FILE = pathlib.Path('../blocks/raws.txt')  # One domain per line
OUTPUT_FILE = pathlib.Path('../autoscript/dns_blocks.txt')  # Output lines for paste

def generate_dns_blocks(domains):
    """Generate 0.0.0.0 domain lines"""
    lines = [f"0.0.0.0 {domain}\n" for domain in domains if domain.strip()]
    header = f"! DNS Block List – Generated {datetime.now().strftime('%Y-%m-%d %H:%M')}\n! Paste to C:\\Windows\\System32\\drivers\\etc\\hosts (admin mode)\n! Backup hosts first!\n\n"
    return header + ''.join(lines)

def main(input_file):
    if not input_file.exists():
        print(f"File {input_file} not found! Create with one domain per line.")
        return

    domains = [line.strip() for line in input_file.read_text(encoding='utf-8').splitlines() if line.strip()]
    if not domains:
        print("No domains in file! Add one per line.")
        return

    content = generate_dns_blocks(domains)
    OUTPUT_FILE.write_text(content, encoding='utf-8')
    print(f"Generated {len(domains)} DNS blocks → {OUTPUT_FILE}")
    print("Preview (first 5 lines):")
    with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            if i > 5:
                break
            print(f"  {i}: {line.rstrip()}")
    print("\nWarning: Edit hosts as admin. Flush DNS (ipconfig /flushdns) after. Test ping domain.com = fail.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate DNS blocks from file")
    parser.add_argument('--input', type=pathlib.Path, default=DEFAULT_INPUT_FILE, help="Input file (one domain/line)")
    args = parser.parse_args()
    main(args.input)