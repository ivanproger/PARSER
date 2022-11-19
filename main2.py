import json
import requests as req
from bs4 import BeautifulSoup as BS

BASE_URL = "https://index.kodifikant.ru"

DB = 'parser.json'
data = {}
response = req.get(f'{BASE_URL}/ru/')
soup = BS(response.text, 'lxml')


# per-позваляет узнать точный td

per = 0
for a in range(0, len(soup.find_all("table"))):
    for i in soup.find_all("table")[a].find_all("td"):
        per += 1
        if per == 1:
            number=i.text  # number-its number og region
        if per==2:
            image=i.next.get("src")
        if per==3:
            reg=i.text
        if per==5:
            ocato=i.text
        if per>5:
            data[number]={"image":image,"region":reg,"ocato":ocato}
            per = 0
print(data)
with open(DB, 'w') as outfile:
    json.dump(data, outfile)