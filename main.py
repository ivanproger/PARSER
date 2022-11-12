import json
import requests as req
from bs4 import BeautifulSoup as BS

BASE_URL = "https://index.kodifikant.ru"

DB='parser.json'
with open(DB) as json_file:
    data = json.load(json_file)

response = req.get(f'{BASE_URL}/ru/')
soup = BS(response.text, 'lxml')
city = []
href = []
for i in range(0, 200):
    soup2 = soup.find("option", {"value": str(i)})
    city.append([i, soup2])
soup3 = soup.find_all("a")
soup_href = soup3[8:]
soups_href = []
for k in range(len(soup_href)):
    soups_href.append([soup_href[k].text, BASE_URL + soup_href[k].get("href")])
print(soups_href)


for m in soups_href:

    local_href = m[1]
    res = req.get(local_href)
    soup_local = BS(response.text, 'lxml')
    per = soup_local.find("h1", {"class": "r150"})
    print(per, local_href, soup_local)

with open(DB, 'w') as outfile:
    json.dump(data, outfile)

