import sqlite3
import requests
import json
import re
import os
import matplotlib
import matplotlib.pyplot as plt

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

def hot100xy():
    valences = []
    ranks = []
    cur.execute("SELECT rank, valence FROM Hot100Valence")
    for row in cur:
        rank = row[0]
        valence = row[1]
        ranks.append(rank)
        valences.append(valence)

    xvals = ranks
    yvals = valences
 

    tup = ranks,valences
    return tup

def popxy():
    valences = []
    ranks = []
    cur.execute("SELECT rank, valence FROM PopValence")
    for row in cur:
        rank = row[0]
        valence = row[1]
        ranks.append(rank)
        valences.append(valence)

    xvals = ranks
    yvals = valences

    tup = xvals, yvals
    return tup

def altxy():
    valences = []
    ranks = []
    cur.execute("SELECT rank, valence FROM AltValence")
    for row in cur:
        rank = row[0]
        valence = row[1]
        ranks.append(rank)
        valences.append(valence)

    xvals = ranks
    yvals = valences

    tup = xvals, yvals
    return tup

def dancehot100xy():
    dances = []
    ranks = []
    cur.execute("SELECT rank, danceability FROM Hot100Valence")
    for row in cur:
        rank = row[0]
        dance = row[1]
        ranks.append(rank)
        dances.append(dance)

    xvals = ranks
    yvals = dances
 

    tup = ranks,dances
    return tup

def dancepopxy():
    dances = []
    ranks = []
    cur.execute("SELECT rank, danceability FROM PopValence")
    for row in cur:
        rank = row[0]
        dance = row[1]
        ranks.append(rank)
        dances.append(dance)

    xvals = ranks
    yvals = dances

    tup = xvals, yvals
    return tup

def dancealtxy():
    dances = []
    ranks = []
    cur.execute("SELECT rank, danceability FROM AltValence")
    for row in cur:
        rank = row[0]
        dance = row[1]
        ranks.append(rank)
        dances.append(dance)

    xvals = ranks
    yvals = dances

    tup = xvals, yvals
    return tup


def visualize():

    hot100x = hot100xy()[0]
    hot100y = hot100xy()[1]

    popx = popxy()[0]
    popy = popxy()[1]

    altx = altxy()[0]
    alty = altxy()[1]

    _hot100x = dancehot100xy()[0]
    _hot100y = dancehot100xy()[1]

    _popx = dancepopxy()[0]
    _popy = dancepopxy()[1]

    _altx = dancealtxy()[0]
    _alty = dancealtxy()[1]

    fig = plt.figure()
    
    
    ax = fig.add_subplot(231)
    ax.scatter(hot100x, hot100y)
    ax.set_xlabel("Ranks")
    ax.set_ylabel("Valence")
    ax.set_title("Valence of the Top Hot100 Songs in 2019")

    ax2 = fig.add_subplot(232)
    ax2.scatter(popx, popy)
    ax2.set_xlabel("Ranks")
    ax2.set_ylabel("Valence")
    ax2.set_title("Valence of the Top Pop Songs in 2019")

    ax3 = fig.add_subplot(233)
    ax3.scatter(altx, alty)
    ax3.set_xlabel("Ranks")
    ax3.set_ylabel("Valence")
    ax3.set_title("Valence of the Top Alt Songs in 2019")

    ax4 = fig.add_subplot(234)
    ax4.scatter(_hot100x, _hot100y)
    ax4.set_xlabel("Ranks")
    ax4.set_ylabel("Danceability")
    ax4.set_title("Danceability of the Top Hot100 Songs in 2019")

    ax5 = fig.add_subplot(235)
    ax5.scatter(_popx, _popy)
    ax5.set_xlabel("Ranks")
    ax5.set_ylabel("Danceability")
    ax5.set_title("Danceability of the Top Pop Songs in 2019")

    ax6 = fig.add_subplot(236)
    ax6.scatter(_altx, _alty)
    ax6.set_xlabel("Ranks")
    ax6.set_ylabel("Danceability")
    ax6.set_title("Danceability of the Top Alt Songs in 2019")

    plt.show()




def main():
    Hot100avg()
    Popavg()
    Altavg()
    dancepopxy()
    visualize()
    
    


if __name__ == '__main__':
    main()