import requests
from bs4 import BeautifulSoup

url = 'https://minfin.com.ua/currency/nbu/'

source = requests.get(url)
main_text = source.text
soup = BeautifulSoup(main_text)

def conv ():
    print("**********************CONVENTOR**********************")
    print("What do you want to convert?")
    print("1. GRN - EUR")
    print("2. GRN - USD")
    print("3. GRN to PLN")
    a = int(input())
    if a == 1:
        print("Print your value")
        b = int(input())
        if b < 0:
            print("ERROR")
            conv()
        else:
            table = soup.find('table', {'class': 'sc-1mi6rpw-1 gnPEbq'})
            tb = table.find('tbody')
            tr = tb.find_all('tr', {'class': 'sc-1mi6rpw-4 imXKsz'})
            ss = tr[1]
            div = ss.find('p', {'class': 'sc-1mi6rpw-9 kdhvRG'})
            div = div.text
            div = int(div[:2])
            s = b/div

            print(round(s, 1), "Євро")
            conv()
    elif a == 2:
        print("Print your value")
        b = int(input())
        if b <= 0:
            print("ERROR")
            conv()
        else:
            table = soup.find('table', {'class': 'sc-1mi6rpw-1 gnPEbq'})
            tb = table.find('tbody')
            tr = tb.find('tr', {'class': 'sc-1mi6rpw-4 imXKsz'})
            td = tr.find('td', {'class': 'sc-1mi6rpw-8 gYhawK'})
            p = td.find('p', {'class': 'sc-1mi6rpw-9 kdhvRG'})
            p = p.text
            p = int(p[:2])
            s = b/p

            print(round(s, 1) , "Доларів")
            conv()
    elif a == 3:
        print("Print your value")
        b = int(input())
        if b < 0:
            print("ERROR")
            conv()

        else:
            table = soup.find('table', {'class': 'sc-1mi6rpw-1 gnPEbq'})
            tb = table.find('tbody')
            tr = tb.find_all('tr', {'class': 'sc-1mi6rpw-4 imXKsz'})
            ss = tr[2]
            div = ss.find('p', {'class': 'sc-1mi6rpw-9 kdhvRG'})
            div = div.text
            div = int(div[:1])

            s = b / div

            print(round(s, 1), "Злотих")
            conv()
    else:
        print("ERROR")
        conv()
conv()