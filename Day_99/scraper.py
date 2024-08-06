import requests #type:ignore
from bs4 import BeautifulSoup #type:ignore


#Have built a set to track titles that have already been scraped, without creating lists or dictionaries for removing duplicates
seen_titles = set()


def scrape():
    url = "https://replit.com/community-hub"
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")

    titles = soup.find_all("span", {"class": "css-scxoy8"}) #Title of event
    links = soup.find_all("a", {"class": "css-epm014"}) #Link of event

    #Scraped the 3 titles and links which always appear under the <h2> Latest </h2> on page
    latest_titles = titles[1:4]
    latest_links = links[1:4]

    if len(latest_titles) != len(latest_links):
        return "Mismatch between titles and links count"


    formatted_output=""

    for title, link in zip(latest_titles, latest_links): #Aggregate elements from the two iterables
        title_text = title.get_text(strip = True)
        link_url = link.get("href", "")

        if title_text not in seen_titles:

            seen_titles.add(title_text)
            formatted_output += f"Title: {title_text}\nLink: {link_url}\n\n" #Pretty print the output

    return formatted_output
