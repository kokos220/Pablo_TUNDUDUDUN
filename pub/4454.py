import requests
from bs4 import BeautifulSoup

url = 'https://minfin.com.ua/currency/nbu/'

source = requests.get(url)
main_text = source.text
soup = BeautifulSoup(main_text)

table = soup.find('table', {'class': 'sc-1mi6rpw-1 gnPEbq'})
tb = table.find('tbody')
tr = tb.find('tr', {'class': 'sc-1mi6rpw-4 imXKsz'})
td = tr.find('td', {'class': 'sc-1mi6rpw-8 gYhawK'})
p = td.find('p', {'class': 'sc-1mi6rpw-9 kdhvRG'})
p = p.text
p = p[:2]
print(p)
