import re
import billboard
import sqlite3

SPOTIFY_REDIRECT_URL  = 'https://github.com/guoguo12/billboard-charts'

# Get Top 100 Pop Songs in 2019
def pop():
    chart = billboard.ChartData('pop-songs', year = 2019)
    return chart
# Get Top 100 Alternative Songs in 2019
def alt():
    chart = billboard.ChartData('alternative-songs', year=2019)
    return chart

# Get Hot 100 Rap Songs in 2019
def hot100():
    chart = billboard.ChartData('hot-100-songs', year = 2019)
    return chart


    
# Database implementation
# #Set up Hot100 chart in Music.db
def setuphot100():
    conn = sqlite3.connect('Music.db') 
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS Hot100(title TEXT, artist TEXT, rank INTEGER)")

    chart = hot100()
    for item in chart:
        _title = item.title
        _artist = item.artist
        _rank = item.rank
        cur.execute("INSERT OR IGNORE INTO Hot100(title, artist, rank) VALUES (?,?,?)", (_title, _artist, _rank))

    conn.commit()

#Set up Pop chart in Music.db
def setupPop():
    conn = sqlite3.connect('Music.db') 
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS Pop(title TEXT, artist TEXT, rank INTEGER)")

    chart = pop()
    for item in chart:
        _title = item.title
        _artist = item.artist
        _rank = item.rank
        cur.execute("INSERT OR IGNORE INTO Pop(title, artist, rank) VALUES (?,?,?)", (_title, _artist, _rank))

    conn.commit()

#Set up Alt chart in Music.db
def setupAlt():
    conn = sqlite3.connect('Music.db') 
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS Alt(title TEXT, artist TEXT, rank INTEGER)")

    chart = alt()
    for item in chart:
        _title = item.title
        _artist = item.artist
        _rank = item.rank
        cur.execute("INSERT OR IGNORE INTO Alt(title, artist, rank) VALUES (?,?,?)", (_title, _artist, _rank))
    conn.commit()


def main():
    print(pop())
    print(alt())
    print(hot100())
    
    setuphot100()
    setupAlt()
    setupPop()


if __name__ == '__main__':
    main()