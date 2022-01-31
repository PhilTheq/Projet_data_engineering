import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://guigui:1234@cluster0.eeflg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = cluster["leagueoflegends"]
collection = db["personnageslol"]


post1 = {"_id" : 0, "Counters" : "No value"}
post2 = {"_id" : 1, "Stats_blue_red" : "No value"}
post3 = {"_id" : 2, "Name" : "No value"}
post4 = {"_id" : 3, "Rank_Lp" : "No value"}
post5 = {"_id" : 4, "Wins_winrate" : "No value"}



collection.insert_many([post1, post2, post3, post4, post5])

# result = collection.update_one({"_id" : 1}, {"$set":{"Best_players":"df_merged"}})

# result = collection.update_one({"_id" : 0}, {"$inc":{"test":5}})




#collection.update({"_id" : 0 }, {"$set" : {"name" :"guigui"}})