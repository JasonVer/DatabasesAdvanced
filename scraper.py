#import
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd
import time
import logging


#variables
times = []
usd = []
btcoin = []
hashes = []
usd_array = []
hashes_array = []
times_array = []
btc_array = []
results = []

#url site
url = "https://www.blockchain.com/btc/unconfirmed-transactions"
#read site
site = uReq(url)
html = site.read()
site.close()
page_soup = soup(html, "html.parser")
containers = page_soup.find_all("div",{"class":"sc-1g6z4xm-0 hXyplo"})


def calculatrix(times,usd,btcoin,hashes):
    for container in containers:
        rwHash = container.find_all('a',{'class':'sc-1r996ns-0 fLwyDF sc-1tbyx6t-1 kCGMTY iklhnl-0 eEewhk d53qjk-0 ctEFcK'})
        hashes = rwHash[0].text

        rwTime = container.find_all('span', {'class':'sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC'})
        times = rwTime[0].text

        rwBtc = container.find_all('span',{'class':'sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC'})
        btc = rwBtc[1].text

        rwUcd = container.find_all('span',{'class':'sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC'})
        usd = rwUcd[2].text
        
        usd_array.append(usd)
        btc_array.append(btc)    
        hashes_array.append(hashes)
        times_array.append(times)

results.append(calculatrix(times,usd,btcoin,hashes))

#get highest price
maxUcd = max(usd_array)
usd.append(maxUcd)
index = usd.index(maxUcd)
maxBts = max(btc_array)
btcoin.append(maxBts)
maxTime = max(times_array)
times.append(maxTime)
maxHash = max(hashes_array)
hashes.append(maxHash)

#put in dataframe and put in file (print) 

df = pd.DataFrame(data = {'Hash':hashes,'Time':times,'BTC':btcoin,'USD':usd})
#df.head(1).to_csv("file.log", header="Hash", index=None, sep='\t', mode='a')
#df.head(1).to_csv("all.log", header="Hash", index=None, sep='\t', mode='a')
#print(df)


#timer
while True:
    time.sleep(60)
    calculatrix(times,usd,btcoin,hashes)
    #file met alle lijnen van refreshen
    df.head(1).to_csv("all.log", header="Hash", index=None, sep='\t', mode='a')
    #grootste van voorbije minuut, 1 lijn
    df.head(1).to_csv("highest.log", header="Hash", index=None, sep='\t', mode='w') 
