# param_extractor.py - Updated: File input (one URL/domain per line), pretty table for params
import pathlib
import requests
from urllib.parse import urlparse, parse_qs
import pandas as pd
from datetime import datetime
import argparse

DEFAULT_INPUT_FILE = pathlib.Path('../domain.txt')  # One URL/domain per line
OUTPUT_FILE = pathlib.Path('../autoscript/param_report.csv')  # CSV + console table

def extract_params(url):
    """Fetch URL, extract query params/values"""
    try:
        response = requests.get(url, timeout=10)
        parsed = urlparse(response.url)  # Final URL after redirects
        params = parse_qs(parsed.query)  # Dict param: [values]
        clean_domain = parsed.netloc  # e.g., abc.xyz from full URL
        param_names = ', '.join(params.keys()) if params else 'None'
        param_values = ', '.join([values[0] for values in params.values()]) if params else 'None'
        num_params = len(params)
        return {
            'Domain': clean_domain,
            'Num_Params': num_params,
            'Param_Names': param_names,
            'Param_Values': param_values
        }
    except Exception as e:
        return {'Domain': url, 'Num_Params': 0, 'Param_Names': 'Error', 'Param_Values': str(e)}

def main(input_file):
    if not input_file.exists():
        print(f"File {input_file} not found! Create with one URL/domain per line.")
        return

    urls = [line.strip() for line in input_file.read_text(encoding='utf-8').splitlines() if line.strip()]
    if not urls:
        print("No URLs in file! Add one per line.")
        return

    print(f"Extracting params for {len(urls)} URLs...\n")
    results = []
    for i, url in enumerate(urls, 1):
        result = extract_params(url)
        result['No.'] = i
        results.append(result)
        print(f"{i}: {url} → {result}")

    # Pretty table
    df = pd.DataFrame(results)
    print("\nFull Table:")
    print(df.to_string(index=False))

    # Save CSV
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"\nTable saved to {OUTPUT_FILE} (for Excel). Example $removeparam rule: ||{urls[0].split('/')[2]}^$removeparam={df['Param_Names'].iloc[0] if df['Num_Params'].iloc[0] > 0 else 'utm_source'}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract params from URL file")
    parser.add_argument('--input', type=pathlib.Path, default=DEFAULT_INPUT_FILE, help="Input file (one URL/line)")
    args = parser.parse_args()
    main(args.input)