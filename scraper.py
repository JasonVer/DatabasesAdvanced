#import
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd
import time
import logging

#variables
timet = []
ucdt = []
btct = []
hasht = []
ucd_array = []
hash_array = []
time_array = []
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


def calculatrix(timet,ucdt,btct,hasht):
    for container in containers:
        rawHash = container.find_all('a',{'class':'sc-1r996ns-0 fLwyDF sc-1tbyx6t-1 kCGMTY iklhnl-0 eEewhk d53qjk-0 ctEFcK'})
        hashed = rawHash[0].text

        rawTime = container.find_all('span', {'class':'sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC'})
        time = rawTime[0].text

        rawBtc = container.find_all('span',{'class':'sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC'})
        btc = rawBtc[1].text

        rawUcd = container.find_all('span',{'class':'sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC'})
        ucd = rawUcd[2].text
        
        ucd_array.append(ucd)
        btc_array.append(btc)    
        hash_array.append(hashed)
        time_array.append(time)

results.append(calculatrix(timet,ucdt,btct,hasht))

#get highest price
maxUcd = max(ucd_array)
ucdt.append(maxUcd)
index = ucdt.index(maxUcd)
maxBts = max(btc_array)
btct.append(maxBts)
maxTime = max(time_array)
timet.append(maxTime)
maxHash = max(hash_array)
hasht.append(maxHash)

#put in dataframe and put in file (print) 

df = pd.DataFrame(data = {'Hash':hasht,'Time':timet,'BTC':btct,'USD':ucdt})
#df.head(1).to_csv("file.log", header="Hash", index=None, sep='\t', mode='a')
#print(df)

#timer
while True:
    time.sleep(60)
    calculatrix(timet,ucdt,btct,hasht)
    #file met alle lijnen van refreshen
    df.head(1).to_csv("all.log", header="Hash", index=None, sep='\t', mode='a')
    #grootste van voorbije minuut, 1 lijn
    df.head(1).to_csv("highest.log", header="Hash", index=None, sep='\t', mode='w') 
