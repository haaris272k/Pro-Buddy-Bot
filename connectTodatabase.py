from constants import *
from pymongo import MongoClient
import urllib.parse


try:
    username = urllib.parse.quote_plus(MONGODB_ATLAS_UNAME)
    password = urllib.parse.quote_plus(MONGODB_ATLAS_PW)
    client = MongoClient(
        "mongodb+srv://%s:%s@cluster.v2uyhil.mongodb.net/?retryWrites=true&w=majority"
        % (username, password)
    )
    db = client["ProBuddyBot"]
    collection = db["DataForBot"]
    print("Connected to the Database!")

except:
    print("Error")
