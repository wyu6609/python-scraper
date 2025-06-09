import requests
from bs4 import BeautifulSoup
import csv
import time
import random

BASE_URL = "https://quotes.toscrape.com/page/{}/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def scrape_quotes(max_pages=5, delay_range=(1, 3)):
    all_quotes = []

    for page_num in range(1, max_pages + 1):
        url = BASE_URL.format(page_num)
        print(f"Scraping: {url}")

        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"⚠️ Request failed: {e}")
            break

        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("div", class_="quote")

        if not quotes:
            print("No more quotes found. Stopping.")
            break

        for quote in quotes:
            text = quote.find("span", class_="text").get_text(strip=True)
            author = quote.find("small", class_="author").get_text(strip=True)
            tags = [tag.get_text() for tag in quote.find_all("a", class_="tag")]
            all_quotes.append({"text": text, "author": author, "tags": ", ".join(tags)})

        # Be polite
        time.sleep(random.uniform(*delay_range))

    return all_quotes

def save_to_csv(quotes, filename="quotes.csv"):
    if not quotes:
        print("No quotes to save.")
        return

    with open(filename, mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ["text", "author", "tags"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(quotes)
    print(f"✅ Saved {len(quotes)} quotes to {filename}")

if __name__ == "__main__":
    quotes = scrape_quotes(max_pages=10)  # You can change the page limit
    save_to_csv(quotes)