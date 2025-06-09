import requests
from bs4 import BeautifulSoup
import logging
import time
import random
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

BASE_URL = "https://quotes.toscrape.com/page/{}/"

def get_session():
    session = requests.Session()
    retries = Retry(total=3, backoff_factor=0.5, status_forcelist=[500, 502, 503, 504])
    session.mount('https://', HTTPAdapter(max_retries=retries))
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    })
    return session

def scrape_quotes(max_pages=5, delay_range=(1, 2)):
    session = get_session()
    all_quotes = []

    for page in range(1, max_pages + 1):
        url = BASE_URL.format(page)
        logging.info(f"Scraping page {page}: {url}")

        try:
            response = session.get(url, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            logging.warning(f"Request failed: {e}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all("div", class_="quote")
        if not quotes:
            logging.info("No more quotes found.")
            break

        for q in quotes:
            text = q.find("span", class_="text").get_text(strip=True)
            author = q.find("small", class_="author").get_text(strip=True)
            tags = [tag.get_text() for tag in q.find_all("a", class_="tag")]
            all_quotes.append({"text": text, "author": author, "tags": tags})

        time.sleep(random.uniform(*delay_range))

    return all_quotes
