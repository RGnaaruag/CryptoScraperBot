import requests
from bs4 import BeautifulSoup


print('build 1.0.0')
print('data from Yahoo Finance')
print('=============================================================================================================')
#Bitcoin
url_btc = 'https://finance.yahoo.com/quote/BTC-USD?p=BTC-USD'
req_btc = requests.get(url_btc)
soup_btc = BeautifulSoup(req_btc.text, 'html.parser')
btc = soup_btc.find('span',{'class': 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
print('Bitcoin, BTC-USD : '+btc)

#Ethereum
url_eth = 'https://finance.yahoo.com/quote/ETH-USD?p=ETH-USD'
req_eth = requests.get(url_eth)
soup_eth = BeautifulSoup(req_eth.text, 'html.parser')
eth = soup_eth.find('span',{'class': 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
print('Ethereum, ETH-USD : '+eth)

#Doge
url_doge = 'https://finance.yahoo.com/quote/DOGE-USD?p=DOGE-USD'
req_doge = requests.get(url_doge)
soup_doge = BeautifulSoup(req_doge.text, 'html.parser')
doge = soup_doge.find('span',{'class': 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
print('Dogecoin, DOGE-USD :'+doge)

#Cardano
url_ada = 'https://finance.yahoo.com/quote/ADA-USD?p=ADA-USD'
req_ada = requests.get(url_ada)
soup_ada = BeautifulSoup(req_ada.text, 'html.parser')
ada = soup_ada.find('span',{'class': 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
print('Cardano, ADA-USD : '+ada)

#Binance
url_bnb = 'https://finance.yahoo.com/quote/BNB-USD?p=BNB-USD'
req_bnb = requests.get(url_bnb)
soup_bnb = BeautifulSoup(req_bnb.text, 'html.parser')
bnb = soup_bnb.find('span',{'class': 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
print('Binance, BNB-USD : '+bnb)

print('=============================================================================================================')

while True:
    continue
