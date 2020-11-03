import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.ikea.com/us/en/p/nilsove-norna-chair-with-chair-pad-rattan-white-laila-natural-s69304122/")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"class": "range-revamp-price__integer"})
string_price = element.text.strip()

price = float(string_price)

if price < 200:
    print("Buy the Item")
    print("The current price is: {} USD".format(price))
else:
    print("Don't buy the item!")
# price_without_symbol = string_price[1:] get everything from string except the first
# <span class="range-revamp-price__integer">96</span>
