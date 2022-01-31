import re
import requests
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://guigui:1234@cluster0.eeflg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = cluster["leagueoflegends"]
collection = db["counters"]

def counter(*champion):
    #f = open("demofile3.txt", "a")
    champion = " ".join(champion)
    champ = champion.split()
    if len(champ) == 0:
        return("", "", "", "")
    perso = champ[0]
    poste = ""
    count = 0
    counters = []
    URL = 'https://www.leagueofgraphs.com/fr/champions/counters/'
    URL = URL + champion
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
    res = requests.get(url = URL, headers = headers)
    tab = list(res.text.split())

    gagnecontre = 0
    perdcontre = 0
    compteur = 0
    compteur_true = False
    compteur_perdant_true = False
    counter = ""
    counter_gold = ""
    loser = ""
    loser_gold = ""
    loserinformation = []
    loserinformationgold = []
 
    counters_informations = []
    counter_golds_informations = []
    for i in tab:   
        if ("gagne" in i and gagnecontre == 0):
            compteur_true = True

        if (compteur_true == True):
            compteur += 1
            if ("alt" in i):
                counter = i
                counter = counter.replace("alt=", "").replace("\"", "")
                

            if ("data-sort-value" in i):
                counter_gold = i
                counter_gold = counter_gold.replace("data-sort-value=", "").replace("\"", "").replace(">","")

                counter_gold = float(counter_gold)
                counter_gold = int(counter_gold)
                counters_informations.append(counter)
                counter_golds_informations.append(counter_gold)

                counter = ""
                counter_gold = ""

        if ("perd" in i and perdcontre == 0):
            compteur = 0
            compteurr = 0

            compteur_true = False
            gagnecontre = 1


        if gagnecontre == 1 and perdcontre == 0:
            compteur_true = False
            compteur_perdant_true=True


        if (compteur_perdant_true == True):
            compteurr += 1
            if ("alt" in i):
                loser = i
                loser = loser.replace("alt=", "").replace("\"", "")


            if ("data-sort-value" in i):
                loser_gold = i
                loser_gold = loser_gold.replace("data-sort-value=", "").replace("\"", "").replace(">","")

                loser_gold = float(loser_gold)
                loser_gold = int(loser_gold)
                loserinformation.append(loser)
                loserinformationgold.append(loser_gold)

                loser = ""
                loser_gold = ""



        if ("meilleur" in i and gagnecontre == 1):
            perdcontre = 1
            compteur_perdant_true = False
    
    try:
        collection.update_one({"_id" : 0 }, {"$set" : {"winner" : loserinformation}})
        collection.update_one({"_id" : 1 }, {"$set" : {"loser" : counters_informations}})
    except Exception : 
        pass

    return(counters_informations, counter_golds_informations, loserinformation, counter_golds_informations)



def main(champion):
    counter_name = []
    counter_golds =[]
    iscountered_name = []
    iscountered_golds =[]

    iscountered_name, iscountered_golds, counter_name, counter_golds =  counter(champion)

    # print(iscountered_name)
    # print(counter_name)
