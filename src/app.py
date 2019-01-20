import requests
from bs4 import BeautifulSoup

# Finds the price of the chair at the give website at our specified target location and converts to usable number

requests = requests.get("https://www.alza.cz/cougar-armor-s-gaming-chair-d5155172.htm")
content = requests.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"class": "bigPrice price_withVat"})
string_price = str(element.text.strip())
price_without_symbol = string_price[:-2]
number_price_1 = price_without_symbol.split()
number_price = number_price_1[0] + number_price_1[1]
price = float(number_price)

if price < 7000:
    print("You should buy!")
else:
    print("Do not buy!")
