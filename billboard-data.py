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

# Get Hot 100 Songs in 2019
def hot100():
    chart = billboard.ChartData('hot-100-songs', year = 2019)
    return chart


    
# Database implementation
# #Set up Hot100 chart in Music.db
def setuphot100():
    #Hot100 is the only table with 100 tracks
    conn = sqlite3.connect('Music.db') 
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS Hot100
        (title TEXT, artist TEXT, rank INTEGER)''')
    title_lst = []
    chart = hot100()
    count = 0
    data = cur.execute('''SELECT title FROM Hot100''')
    for x in data:
        title_lst.append(x[0])
    for item in chart:
        _title = item.title
        _artist = item.artist
        _rank = item.rank
        tup = _title, _artist, _rank
        if count == 25:
            break
        if tup[0] in title_lst:
            continue
        else:
            cur.execute("INSERT OR IGNORE INTO Hot100(title, artist, rank) VALUES (?,?,?)", (_title, _artist, _rank))
            count += 1

    conn.commit()
    conn.close()


# Set up Pop music chart in Music.db
def setupPop():
    conn = sqlite3.connect('Music.db') 
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS Pop
        (title TEXT, artist TEXT, rank INTEGER)''')
    title_lst = []
    chart = pop()
    count = 0
    data = cur.execute('''SELECT title FROM Pop''')
    for x in data:
        title_lst.append(x[0])
    for item in chart:
        _title = item.title
        _artist = item.artist
        _rank = item.rank
        tup = _title, _artist, _rank
        if count == 25:
            break
        if tup[0] in title_lst:
            continue
        else:
            cur.execute("INSERT OR IGNORE INTO Pop(title, artist, rank) VALUES (?,?,?)", (_title, _artist, _rank))
            count += 1

    conn.commit()
    conn.close()

#Set up Alt chart in Music.db
def setupAlt():
    conn = sqlite3.connect('Music.db') 
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS Alt
        (title TEXT, artist TEXT, rank INTEGER)''')
    title_lst = []
    chart = alt()
    count = 0
    data = cur.execute('''SELECT title FROM Alt''')
    for x in data:
        title_lst.append(x[0])
    for item in chart:
        _title = item.title
        _artist = item.artist
        _rank = item.rank
        tup = _title, _artist, _rank
        if count == 25:
            break
        if tup[0] in title_lst:
            continue
        else:
            cur.execute("INSERT OR IGNORE INTO Alt(title, artist, rank) VALUES (?,?,?)", (_title, _artist, _rank))
            count += 1

    conn.commit()
    conn.close()


def main():
    # print(pop())
    # print(alt())
    # print(hot100())
    
    setuphot100()
    setupAlt()
    setupPop()


if __name__ == '__main__':
    main()