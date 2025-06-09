import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    url = 'https://quotes.toscrape.com'
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch page. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')

    for i, quote in enumerate(quotes, 1):
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        print(f"{i}. \"{text}\" — {author}")

if __name__ == '__main__':
    scrape_quotes()