#import
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd
import time as timer
import logging
import pymongo as mongo
import redis

#Redis
con = redis.Redis()

#mongoDB
client = mongo.MongoClient("mongodb://localhost:27017")

#connect to DB
database = client["ValueTable"]
DataInBase = database["values"]

# variables
hashes = []
time = []
bitcoin = []
usd = []

# function
def ToMongo(con, DataInBase):

    #Fill in variables
    hashes = list(map(str, con.lrange("Hash", 0, -1)))
    time = list(map(str, con.lrange("Time", 0, -1)))
    bitcoin = list(map(str, con.lrange("Bitcoin", 0, -1)))
    usd = list(map(str, con.lrange("US Dollar", 0, -1)))

    #Pass on values
    mon = max(usd)
    ind = usd.index(mon)
    hashin = hashes[ind]
    times = time[ind]
    bit = bitcoin[ind]

    # total
    tot = {"Hash": hashin, "Time": times, "Amount(BTC)": bit, "Amount(USD)": mon }
    
    #Store in DB
    DataInBase.insert_one(tot)
    
# timer
while True:
    ToMongo(con, DataInBase)
    timer.sleep(60)
