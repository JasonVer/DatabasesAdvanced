#import
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd
import time
import logging
import pymongo as mongo


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
    hashes = list(map(str, connect.lrange("Hash", 0, -1)))
    time = list(map(str, connect.lrange("Time", 0, -1)))
    bitcoin = list(map(float, connect.lrange("Bitcoin", 0, -1)))
    usd = list(map(float, connect.lrange("US Dollar", 0, -1)))

    #Pass on values
    mon = max(usd)
    ind = toUsd.index(mon)
    hashin = hashes[index]
    times = time[index]
    bit = bitcoin[index]

    # total
    tot = {"Hash": hashin, "Time": times, "Amount(BTC)": bit, "Amount(USD)": mon }
    
    #Store in DB
    DataInBase.insert_one(tot)
    
# timer
while True:
    ToMongoDB(con, DataInBase)
    time.sleep(60)