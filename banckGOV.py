import requests
from bs4 import BeautifulSoup


class Converter:
    def __init__(self, kurs):
        self.kurs = kurs

    def convert(self, amount):
        return amount / self.kurs


url = "https://bank.gov.ua/ua/markets/exchangerates"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

for row in soup.find_all("tr"):
    cells = row.find_all("td")
    if cells and "USD" in cells[0].text:
        kurs = float(cells[3].text.replace(",", "."))
        break

amount = float(input("Введіть суму в гривнях: "))

converter = Converter(kurs)

print("Доларів:", round(converter.convert(amount), 2))
