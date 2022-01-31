import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://guigui:1234@cluster0.eeflg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = cluster["leagueoflegends"]
collection = db["blue_red"]


post1 = {"_id" : 0, "blue_red" : "No value"}

collection.insert_one(post1)

# result = collection.update_one({"_id" : 1}, {"$set":{"Best_players":"df_merged"}})

# result = collection.update_one({"_id" : 0}, {"$inc":{"test":5}})




#collection.update({"_id" : 0 }, {"$set" : {"name" :"guigui"}})