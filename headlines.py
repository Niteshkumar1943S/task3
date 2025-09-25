import requests
from bs4 import BeautifulSoup

def get_bbc_headlines():
    url = "https://www.bbc.com/news"
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Failed to retrieve the page.")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    # BBC's headline class can change, but as of now:
    headlines = soup.find_all('h2')

    top_headlines = []
    for h in headlines:
        text = h.get_text(strip=True)
        if text and len(text) > 10:  # Skip too-short titles
            top_headlines.append(text)

    return top_headlines

if __name__ == "__main__":
    headlines = get_bbc_headlines()
    print("\nTop BBC News Headlines:\n")
    for i, headline in enumerate(headlines[:10], 1):  # Limit to top 10
        print(f"{i}. {headline}")
