import argparse
import logging
from scraper_utils import scrape_quotes
from output_utils import save_to_csv, save_to_json

def main():
    parser = argparse.ArgumentParser(description="Scrape quotes.toscrape.com")
    parser.add_argument('--pages', type=int, default=5, help='Number of pages to scrape')
    parser.add_argument('--out', type=str, default='quotes.csv', help='Output file name')
    parser.add_argument('--format', choices=['csv', 'json'], default='csv', help='Output format')
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format='%(asctime)s — %(levelname)s — %(message)s')

    quotes = scrape_quotes(max_pages=args.pages)

    if args.format == 'csv':
        save_to_csv(quotes, args.out)
    else:
        save_to_json(quotes, args.out)

if __name__ == '__main__':
    main()