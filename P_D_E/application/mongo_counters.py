import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://guigui:1234@cluster0.eeflg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = cluster["leagueoflegends"]
collection = db["counters"]


post1 = {"_id" : 0, "winner" : "No value"}
post2 = {"_id" : 1, "loser" : "No value"}




collection.insert_many([post1, post2])

# result = collection.update_one({"_id" : 1}, {"$set":{"Best_players":"df_merged"}})

# result = collection.update_one({"_id" : 0}, {"$inc":{"test":5}})




#collection.update({"_id" : 0 }, {"$set" : {"name" :"guigui"}})