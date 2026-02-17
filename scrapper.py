import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"
OUTPUT_FILE = "headlines.txt"


def fetch_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Not a bot, just learning Python)"
    }
    response = requests.get(url, headers=headers, verify=False)

    response.raise_for_status()
    return response.text


def extract_headlines(html):
    soup = BeautifulSoup(html, "html.parser")
    headlines = []

    for tag in soup.find_all("h2"):
        text = tag.text.strip()
        if text:
            headlines.append(text)

    return headlines


def save_headlines(headlines):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        for headline in headlines:
            file.write(headline + "\n")


def main():
    try:
        print("Fetching news headlines... because reading manually is overrated.")
        html = fetch_html(URL)
        headlines = extract_headlines(html)

        if not headlines:
            print("No headlines found. Website probably changed its mood.")
            return

        save_headlines(headlines)
        print(f"Saved {len(headlines)} headlines to {OUTPUT_FILE}. Go feel productive.")

    except requests.exceptions.RequestException as e:
        print("Something went wrong while fetching the website.")
        print(e)


if __name__ == "__main__":
    main()
