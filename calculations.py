import sqlite3
import requests
import json
import re
import os

# CALCULATIONS

fname = "Hot100calc.txt"
fname2 = "Popcalc.txt"
fname3 = "Altcalc.txt"

conn = sqlite3.connect('Music.db') 
cur = conn.cursor() 

def Hot100avg():
    cur.execute("SELECT Hot100.title, Hot100.artist, Hot100Valence.valence, Hot100Valence.danceability FROM Hot100 JOIN Hot100Valence ON Hot100.rank = Hot100Valence.rank")
    
    # lst = []
    with open(fname, "w") as f:
        for row in cur:
            title = row[0]
            artist = row[1]
            val = row[2]
            # print(val)
            dance = row[3]
            # print(dance)

            _sum = val + dance
            _avg = _sum/2.0
            # print(_avg)
            # lst.append(_avg)
            f.write(f"The average between valence and danceability for {title} by {artist} is {_avg}.\n")
    
    # f = open(fname, "r")
    # print(f.read())

    # return lst

def Popavg():
    cur.execute("SELECT Pop.title, Pop.artist, PopValence.valence, PopValence.danceability FROM Pop JOIN PopValence ON Pop.rank = PopValence.rank")
    
    # lst = []
    with open(fname2, "w") as f:
        for row in cur:
            title = row[0]
            artist = row[1]
            val = row[2]
            # print(val)
            dance = row[3]
            # print(dance)

            _sum = val + dance
            _avg = _sum/2.0
            # print(_avg)
            # lst.append(_avg)
            f.write(f"The average between valence and danceability for {title} by {artist} is {_avg}.\n")
    
    f = open(fname2, "r")
    print(f.read())

def Altavg():
    cur.execute("SELECT Alt.title, Alt.artist, AltValence.valence, AltValence.danceability FROM Alt JOIN AltValence ON Alt.rank = AltValence.rank")
    
    # lst = []
    with open(fname3, "w") as f:
        for row in cur:
            title = row[0]
            artist = row[1]
            val = row[2]
            # print(val)
            dance = row[3]
            # print(dance)

            _sum = val + dance
            _avg = _sum/2.0
            # print(_avg)
            # lst.append(_avg)
            f.write(f"The average between valence and danceability for {title} by {artist} is {_avg}.\n")
    
    f = open(fname3, "r")
    print(f.read())



# VISUALIZATIONS

def 

def main():
    Hot100avg()
    Popavg()
    Altavg()
    


if __name__ == '__main__':
    main()