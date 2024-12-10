import requests
from bs4 import BeautifulSoup

url = "https://www.villagesoulofindia.com/app/order/menu"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

items = []
menu_cards = soup.find_all("h5")

for card in menu_cards:
    name = card.text.strip()
    price_div = card.find_next("div", class_="text-muted")
    price = price_div.text.strip() if price_div else "Price not available"
    items.append((name, price))

for item in items:
    print(f"Item: {item[0]}, Price: {item[1]}")