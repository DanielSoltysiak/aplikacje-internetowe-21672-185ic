import requests
from bs4 import BeautifulSoup



def script( soup ):
    films = []

    items = soup.select("div.simplePoster")
    print(len(items), "Polecane filmy")
    for elem in items:
        title = elem.select("h3")[0].text
        year = elem.find_all("div", class_="simplePoster__year")[0].text
        info = {"tytul": title.strip(), "rokWydania": year.strip()}
        films.append(info)

    print(films)