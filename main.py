import requests
from bs4 import BeautifulSoup

URL = "https://coinmarketcap.com/"

res = requests.get(URL)

if res.status_code == 200:
  soup = BeautifulSoup(res.text, features="html.parser")
  info = soup.find_all("a", {"href":"/currencies/bnb/markets/"})
  price = info[0].getText()
  print(price)





  URL = "https://coinmarketcap.com/"

res = requests.get(URL)

if res.status_code == 200:
  soup = BeautifulSoup(res.text, features="html.parser")
  info = soup.find_all("p", "sc-e225a64a-0 ePTNty")
  price = info[3].getText()
  print(price)


