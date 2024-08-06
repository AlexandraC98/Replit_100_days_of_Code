import requests
from bs4 import BeautifulSoup

for no in range(1, 6):
  url = f"https://news.ycombinator.com/?p={no}"
  response = requests.get(url)
  html = response.text

  soup = BeautifulSoup(html, "html.parser")

  myLinks = soup.find_all("a")

  print(f"\nPage {no} has {len(myLinks)} links\n")
  
  for link in myLinks:
    link_text = link.text.lower()
    if "replit" in link_text or "python" in link_text:
        print(link.text)
