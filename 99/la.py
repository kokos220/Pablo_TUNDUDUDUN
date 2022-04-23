import sqlite3
import datetime
import requests
from bs4 import BeautifulSoup

url = 'https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%82%D0%B5%D1%80%D0%BD%D0%BE%D0%BF%D0%BE%D0%BB%D1%8C'

source = requests.get(url)
main_text = source.text
soup = BeautifulSoup(main_text)

p = soup.find('div', {'class': 'main loaded'})
o = p.find('div', {'class': 'temperature'})
i = o.find('div', {'class': 'min'})
u = i.find('span')
u = u.text
a = datetime.datetime.today().strftime("%d.%m.%Y")
b = datetime.datetime.today().strftime("%H:%M:%S")
b = b[:5]

connection = sqlite3.connect('las_DB.sl3', 5)
cur = connection.cursor()
#cur.execute('''CREATE TABLE tuble (date TEXT, time TEXT, temp TEXT)''')

cur.execute(f"INSERT INTO tible (date, time, temp) VALUES (('{a}'), ('{b}'), ('{u}'))")
connection.commit()
connection.close()