import requests
from bs4 import BeautifulSoup

url = 'https://minfin.com.ua/currency/nbu/'

source = requests.get(url)
main_text = source.text
soup = BeautifulSoup(main_text)

table = soup.find('table', {'class': 'sc-1mi6rpw-1 gnPEbq'})
tb = table.find('tbody')
tr = tb.find_all('tr', {'class': 'sc-1mi6rpw-4 imXKsz'})
ss = tr[3]
div = ss.find('p', {'class': 'sc-1mi6rpw-9 kdhvRG'})
div = div.text
div = div[:5]
print(div)
