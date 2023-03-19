import requests
from bs4 import BeautifulSoup

URL = "https://www.olx.ua/d/uk/obyavlenie/blok-tavrya-slavuta-1-1-IDQB9Rp.html"

res = requests.get(URL)

if res.status_code == 200:
  soup = BeautifulSoup(res.text, features="html.parser")
  info = soup.find_all("h3", "css-ddweki er34gjf0")
  price = info[0].getText()
  print(price)


  URL = "https://www.olx.ua/d/uk/obyavlenie/blok-tavrya-slavuta-1-1-IDQB9Rp.html"

res = requests.get(URL)

if res.status_code == 200:
  soup = BeautifulSoup(res.text, features="html.parser")
  info = soup.find_all("h1", "css-1soizd2 er34gjf0")
  price = info[0].getText()
  print(price)







