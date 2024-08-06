import requests #type:ignore
from bs4 import BeautifulSoup #type:ignore
import random

def getQuote():
    url = "https://eu.usatoday.com/story/life/2023/11/30/positive-quotes-to-inspire/11359498002/"

    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")

    quotes = soup.find_all("li")
    quotes_texts = []

    for quote in quotes:
        quote_text = quote.get_text()
        quotes_texts.append(quote_text)

    if quotes_texts:
        random_quote = random.choice(quotes_texts)
        return random_quote