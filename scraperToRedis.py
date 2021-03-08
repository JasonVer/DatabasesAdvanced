#import
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd
import time
import logging
import pymongo as mongo
import redis
import numpy as np

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

#Redis
con = redis.Redis()

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

#index = usd.index(maxUcd)
#maxHash = max(hashes_array)
#hashes.append(maxHash)
#maxTime = max(times_array)
#times.append(maxTime)
#maxBts = max(btc_array)
#btcoin.append(maxBts)
#maxUcd = max(usd_array)
#usd.append(maxUcd)

#values into redis
con.rpush("Hash", str(hashes_array.text))
con.rpush("Time", str(times_array.text))
con.rpush("Bitcoin", str(btc_array))
con.rpush("US Dollar", str(usd_array.text))


#mongoDB
client = mongo.MongoClient("mongodb://localhost:27017")

#connect to DB
database = client["ValueTable"]
DataInBase = database["values"]


#timer
while True:
    time.sleep(60)
    #function
    calculatrix(times,usd,btcoin,hashes)