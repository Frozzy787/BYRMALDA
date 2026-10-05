import sqlite3
import requests
from bs4 import BeautifulSoup

connection = sqlite3.connect("weather.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS weather (date_time TEXT, temperature TEXT)")

url = "https://weathermetro.com/weather/dnipro"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

temperature = soup.find("h1").text.split("°")[0]
date_time = datetime.now().strftime("%d.%m.%Y %H:%M")

cursor.execute("INSERT INTO weather VALUES (?, ?)", (date_time, temperature))

connection.commit()
connection.close()

print("Temperature:", temperature)