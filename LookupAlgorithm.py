from ConnectDatabase import *
import random


"""
A simple lookup algorithm that returns a random content of respective tag_type from the database.
A random id is generated and the content is fetched from the database corresponding to that id and tag_type.
All the stored items in the database have a unique id (eg - 1000), a tag (eg "joke") and the content (poem,joke,quote).
The id and the tag_type is matched with the input tag and the content is returned.

"""


def lookup(input_tag):
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
            query = collection.find_one({"id": id})
            return query[input_tag]
        else:
            query = collection.find_one({"_id": id})
            return query[input_tag]
    except:
        return "Some error occured!"
