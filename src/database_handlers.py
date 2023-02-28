from constants import *
from pymongo import MongoClient
import urllib.parse
import random

"""
This class has the methods which handle the database operations.
connect_to_database method is used to connect to the database,create a database and create a collection.
lookup method makes use of basic algorithm to fetch a random document from the database.

"""

class DatabaseHandlers:

    def __init__(self) -> None:

        """
        This is the constructor of the class.

        Args:
            self: The object of the class.

        Returns:
            None
        """
        pass

    def connect_database(self, MONGODB_ATLAS_UNAME, MONGODB_ATLAS_PW):

        """
        This method is used to connect to the database,create a database and create a collection.

        Args:
            self: The object of the class.

        Returns:
            None
        """
        try:
            username = urllib.parse.quote_plus(MONGODB_ATLAS_UNAME)
            password = urllib.parse.quote_plus(MONGODB_ATLAS_PW)
            client = MongoClient(
                "mongodb+srv://%s:%s@cluster.v2uyhil.mongodb.net/?retryWrites=true&w=majority"
                % (username, password)
            )
            self.db = client["ProBuddyBot"]
            self.collection = self.db["DataForBot"]
            return "Connected to the Database!"

        except:
            return "Error"

    def lookup(self, input_tag):

        """
        This method makes use of basic algorithm to fetch a random document from the database.

        Args:
            self: The object of the class.

        Returns:    
            None

        """
        try:
            idranges = {
                "joke": [1, 1000],
                "meme": [1391, 1840],
                "poem": [1163, 1187],
                "quote": [1007, 1148],
                "fact": [1203, 1388],
            }

            if input_tag in idranges:
                idrange = idranges[input_tag]
                id = random.randint(idrange[0], idrange[1])

            if input_tag == "meme":
                query = self.collection.find_one({"id": id})
                return query[input_tag]
            else:
                query = self.collection.find_one({"_id": id})
                return query[input_tag]
        except:
            return "Some error occured!"

# create an object of the class
dbhandler = DatabaseHandlers()