from turtle import pd
from application import app
from flask import render_template, url_for, request
import pandas as pd
import json
import plotly
import plotly_express as px

import sys

sys.path.append("../")
from P_D_E.application.getcounters import counter
from P_D_E.application.best_players import getbestplayers
from P_D_E.application.bluered import *

import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://guigui:1234@cluster0.eeflg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = cluster["leagueoflegends"]
collection_best_player = db["personnageslol"]
Counters_lol = db["counters"]
blue_red_lol = db["blue_red"]


@app.route('/GetCounters', methods=['POST'])
def callback_counter(champion):
    counter_name = []
    counter_golds =[]
    iscountered_name = []
    iscountered_golds = []

    iscountered_name, iscountered_golds, counter_name, counter_golds =  counter(champion)

@app.route("/")
def index():

    return render_template("index.html", title = "Home")

@app.route("/Counters", methods=['get','post'])
def Counters():
    
    # db base counters ~>
    db = Counters_lol.find_one({"_id": 1})
    db_1 = Counters_lol.find_one({"_id": 0})

    loser = db["loser"]
    winner = db_1["winner"]
    # db base counters <~
    
    champion_search = request.form.to_dict()

    counter_name = []
    counter_golds =[]
    iscountered_name = []
    iscountered_golds =[]

    if "counters" in champion_search:
        iscountered_name, iscountered_golds, counter_name, counter_golds =   counter(champion_search["counters"])
    else:
        iscountered_name, iscountered_golds, counter_name, counter_golds =   counter("")


    
    if len(counter_name) == 0:
        champs_counter_str = " "
    else:
        champs_counter_str = champion_search["counters"] + " is countered by : "

    for champs_1 in counter_name:
        champs_counter_str += champs_1 + " ."


    
    if len(iscountered_name) == 0:
        champs_countered_str = " "
    else:
        champs_countered_str = champion_search["counters"] + "  counter : "


    for champs in iscountered_name:
        champs_countered_str += champs + " ." 

    try:
        if len(loser and winner) < 0:
            print("return")
    except Exception:
        pass


    return render_template("counters.html", champion=champs_countered_str, champion_1 = champs_counter_str)


@app.route("/Dashboard")
def Dashboard():
    bestplayers = getbestplayers()
    return render_template("index.html", title = "Home")

@app.route("/Best Players")
def Best_players():
    
    test = getbestplayers()
    #print(test)

    return render_template("best_players.html", best_players=test)





@app.route("/blue-red")
def stats_blue_red():
    stats = stats_blue()


    #print(stats)    

    stats_blue
    return render_template("blue-red.html", stats_blue=stats)


