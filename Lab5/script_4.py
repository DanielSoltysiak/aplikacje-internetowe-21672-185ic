import requests
from bs4 import BeautifulSoup
import csv

def script( soup ):
    films = []

    items = soup.select("div.simplePoster")
    for elem in items:
        title = elem.select("h3")[0].text.strip()
        year = elem.find_all("div", class_="simplePoster__year")[0].text.strip()
        image = elem.select('img')[0].get('src')

        films.append({
            "title": title,
            "year": year,
            "image": image
        })


    keys = films[0].keys()
    print("keys = ", keys)

    with open('items.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(films)