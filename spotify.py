import sqlite3
import requests
import json
import re
import os

#Setting up Spotify API
CLIENT_ID = '435102e52d714c9699a84c12478e6133'
CLIENT_SECRET = 'af46a8c61b724d6c9f2920bf54733416'

AUTH_URL = 'https://accounts.spotify.com/api/token'
# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})
# convert the response to JSON
auth_response_data = auth_response.json()
# save access token
access_token = auth_response_data['access_token']

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

#Takes in a table and Returns a list of tuples (track, artist)
def read_from_db(table):
    conn = sqlite3.connect('Music.db') 
    cur = conn.cursor() 
    cur.execute(f'SELECT * FROM {table}')
    #puts (title, artist, rank) for all items in list
    data = cur.fetchall()
    return data

#Takes in a list of tuples and Returns a list of tuples with the ID code for each song in the Pop Table
def track_id_lstPop(data_lst):
    BASE_URL = 'https://api.spotify.com/v1/search?'
    count = 0
    id_lst = []

    for item in data_lst:
        title = item[0]
        artist = item[1]
        rank = item[2]
        feat = "Featuring "
        #Differences between Spotify song titles and Billboard API titles result in hardcode to modify certain titles and artists
        if feat in item[1] and count < 2:
            if item[1] == "Ellie Goulding X Diplo Featuring Swae Lee":
                artist = artist.replace("Ellie Goulding X Diplo Featuring Swae Lee", "Ellie Goulding & Diplo")
                q= f"q=track:{title}%20artist:{artist}&type=track"
                r = requests.get(BASE_URL + q, headers=headers)
                txt = r.text
                obj = json.loads(txt)
                ids = obj['tracks']['items'][1]['id']
                id_lst.append((title, artist, ids, rank))
            else:
                artist = item[1].replace(feat, '')
                q= f"q=track:{title}%20artist:{artist}&type=track"
                r = requests.get(BASE_URL + q, headers=headers)
                txt = r.text
                obj = json.loads(txt)
                ids = obj['tracks']['items'][0]['id']
                id_lst.append((title, artist, ids, rank))
        else:
            q= f"q=track:{title}%20artist:{artist}&type=track"
            r = requests.get(BASE_URL + q, headers=headers)
            txt = r.text
            obj = json.loads(txt)
            ids = obj['tracks']['items'][1]['id']
            id_lst.append((title, artist, ids, rank))
    return id_lst

#Takes in a list of tuples and Returns a list of tuples with the ID code for each song in the Hot100 Table
def track_id_lstHot100(data_lst):
    BASE_URL = 'https://api.spotify.com/v1/search?'
    count = 0
    id_lst = []

    for item in data_lst:
        title = item[0]
        artist = item[1]
        rank = item[2]
        feat = "Featuring "
        #Differences between Spotify song titles and Billboard API titles result in hardcode to modify certain titles and artists
        if item[0] == 'Bury A Friend':
            q= f"q=track:Bury A Friend%20artist:Billie Eilish&type=track"
            r = requests.get(BASE_URL + q, headers=headers)
            txt = r.text
            lst = []
            obj = json.loads(txt)
            ids = obj['tracks']['items'][0]['id']
            id_lst.append((title, artist, ids, rank))
        elif feat in item[1]:
            if item[1] == "Ellie Goulding X Diplo Featuring Swae Lee":
                artist = artist.replace("Ellie Goulding X Diplo Featuring Swae Lee", "Ellie Goulding & Diplo")
                q= f"q=track:{title}%20artist:{artist}&type=track"
                r = requests.get(BASE_URL + q, headers=headers)
                txt = r.text
                obj = json.loads(txt)
                ids = obj['tracks']['items'][1]['id']
                id_lst.append((title, artist, ids, rank))
            else:
                artist = item[1].replace(feat, '')
                q= f"q=track:{title}%20artist:{artist}&type=track"
                r = requests.get(BASE_URL + q, headers=headers)
                txt = r.text
                obj = json.loads(txt)
                ids = obj['tracks']['items'][0]['id']
                id_lst.append((title, artist, ids, rank))
        elif item[1] == "Gucci Mane X Bruno Mars X Kodak Black":
                artist = artist.replace("Gucci Mane X Bruno Mars X Kodak Black", "Gucci Mane Bruno Mars Kodak Black")
                q= f"q=track:{title}%20artist:{artist}&type=track"
                r = requests.get(BASE_URL + q, headers=headers)
                txt = r.text
                obj = json.loads(txt)
                ids = obj['tracks']['items'][1]['id']
                id_lst.append((title, artist, ids, rank))
        elif item[0] == "Ran$om":
                title = title.replace("Ran$om", "Ransom")
                q= f"q=track:{title}%20artist:{artist}&type=track"
                r = requests.get(BASE_URL + q, headers=headers)
                txt = r.text
                obj = json.loads(txt)
                ids = obj['tracks']['items'][1]['id']
                id_lst.append((title, artist, ids, rank))
        else:
            q= f"q=track:{title}%20artist:{artist}&type=track"
            r = requests.get(BASE_URL + q, headers=headers)
            txt = r.text
            obj = json.loads(txt)
            ids = obj['tracks']['items'][1]['id']
            id_lst.append((title, artist, ids, rank))
    return id_lst

#Takes in a list of tuples and Returns a list of tuples with the ID code for each song in the Alt Table
def track_id_lstAlt(data_lst):
    BASE_URL = 'https://api.spotify.com/v1/search?'
    count = 0
    id_lst = []

    for item in data_lst:
        title = item[0]
        artist = item[1]
        rank = item[2]
        feat = "Featuring "
        apos = "'"
        #Differences between Spotify song titles and Billboard API titles result in hardcode to modify certain titles and artists
        if feat in item[1]:
            if item[0] == "You're Somebody Else":
                title = title.replace("You're Somebody Else", "Youre Somebody Else")
                q= f"q=track:{title}%20artist:{artist}&type=track"
                r = requests.get(BASE_URL + q, headers=headers)
                txt = r.text
                obj = json.loads(txt)
                ids = obj['tracks']['items'][1]['id']
                id_lst.append((title, artist, ids, rank))
            else:
                artist = item[1].replace(feat, '')
                q= f"q=track:{title}%20artist:{artist}&type=track"
                r = requests.get(BASE_URL + q, headers=headers)
                txt = r.text
                obj = json.loads(txt)
                ids = obj['tracks']['items'][0]['id']
                id_lst.append((title, artist, ids, rank))
        elif apos in item[0]:
            title = title.replace(apos, "")
            q= f"q=track:{title}%20artist:{artist}&type=track"
            r = requests.get(BASE_URL + q, headers=headers)
            txt = r.text
            obj = json.loads(txt)
            ids = obj['tracks']['items'][0]['id']
            id_lst.append((title, artist, ids, rank))
        else:
            q= f"q=track:{title}%20artist:{artist}&type=track"
            r = requests.get(BASE_URL + q, headers=headers)
            txt = r.text
            obj = json.loads(txt)
            ids = obj['tracks']['items'][0]['id']
            id_lst.append((title, artist, ids, rank))
    return id_lst

#A test method to see if IDS are correct (NOT NEEDED)
def check_tracks(id_lst):
    lst = []
    #list of ids
    for x in id_lst:
        t_id = x[2]
        lst.append(t_id)
    #BASE URL FOR SPOTIFY API
    BASE_URL = 'https://api.spotify.com/v1/tracks/'
    count = 0
    for x in lst:
        r = requests.get(BASE_URL + x, headers=headers)
        txt = r.text
        obj = json.loads(txt)
        track_name = obj['name']

#Takes in a list and uses ID's to find the audio features for songs: Valence & Danceability 
#Creates tables for the audio features of the songs
def setuphot100valence(lst):
    BASE_URL = 'https://api.spotify.com/v1/'
    conn = sqlite3.connect('Music.db')
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS Hot100Valence
        (title TEXT, artist TEXT, valence FLOAT, danceability FLOAT, rank INTEGER)''')
    title_lst = []
    count = 0
    data = cur.execute('''SELECT title FROM Hot100Valence''')
    for x in data:
        title_lst.append(x[0])
    for song in lst:
        #song info
        title = song[0]
        artist = song[1]
        track_id = song[2]
        rank = song[3]
        #getting valence
        r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)
        txt = r.text
        obj = json.loads(txt)
        # print(obj)
        val = obj['valence']
        dan = obj['danceability']
        tup = title, artist, val, dan, rank
        if count == 25:
            break
        if tup[0] in title_lst:
            continue
        else:
            cur.execute("INSERT OR IGNORE INTO Hot100Valence(title, artist, valence, danceability, rank) VALUES (?,?,?,?, ?)", (title, artist, val, dan, rank))
            count += 1
    conn.commit()
    conn.close()

#Use ID's to find the audio features for songs: Valence & Danceability 
#Creates tables for the audio features of the songs
def setupaltvalence(lst):
    BASE_URL = 'https://api.spotify.com/v1/'
    conn = sqlite3.connect('Music.db')
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS AltValence
        (title TEXT, artist TEXT, valence FLOAT, danceability FLOAT, rank INTEGER)''')
    title_lst = []
    count = 0
    data = cur.execute('''SELECT title FROM AltValence''')
    for x in data:
        title_lst.append(x[0])
    for song in lst:
        #song info
        title = song[0]
        artist = song[1]
        track_id = song[2]
        rank = song[3]
        #getting valence & danceability
        r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)
        txt = r.text
        obj = json.loads(txt)
        val = obj['valence']
        dan = obj['danceability']
        tup = title, artist, val, dan, rank
        if count == 25:
            break
        if tup[0] in title_lst:
            continue
        else:
            cur.execute("INSERT OR IGNORE INTO AltValence(title, artist, valence, danceability, rank) VALUES (?,?,?,?,?)", (title, artist, val, dan, rank))
            count += 1
    conn.commit()
    conn.close()

#Use ID's to find the audio features for songs: Valence & Danceability 
#Creates tables for the audio features of the songs
def setuppopvalence(lst):
    BASE_URL = 'https://api.spotify.com/v1/'
    conn = sqlite3.connect('Music.db')
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS PopValence
        (title TEXT, artist TEXT, valence FLOAT, danceability FLOAT, rank INTEGER)''')
    title_lst = []
    count = 0
    data = cur.execute('''SELECT title FROM PopValence''')
    for x in data:
        title_lst.append(x[0])
    for song in lst:
        #song info
        title = song[0]
        artist = song[1]
        track_id = song[2]
        rank = song[3]
        #getting valence & danceability
        r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)
        txt = r.text
        obj = json.loads(txt)
        val = obj['valence']
        dan = obj['danceability']
        tup = title, artist, val, dan, rank
        if count == 25:
            break
        if tup[0] in title_lst:
            continue
        else:
            cur.execute("INSERT OR IGNORE INTO PopValence(title, artist, valence, danceability, rank) VALUES (?,?,?,?,?)", (title, artist, val, dan, rank))
            count += 1
    conn.commit()
    conn.close()


def main():
    #Pop
    a = read_from_db('Pop')
    pop_lst = track_id_lstPop(a)
    setuppopvalence(pop_lst)
    # check_tracks(lst)

    #Alt
    b = read_from_db('Alt')
    alt_lst = track_id_lstAlt(b)
    setupaltvalence(alt_lst)
    # check_tracks(lst)
    
    #Hot100
    c = read_from_db('Hot100')
    lst = track_id_lstHot100(c)
    setuphot100valence(lst)
    # check_tracks(lst)


if __name__ == '__main__':
    main()



#sample testing for song code:
            # q= f"q=track:{title}%20artist:{artist}&type=track"
            # r = requests.get(BASE_URL + q, headers=headers)
            # txt = r.text
            # obj = json.loads(txt)
            # ids = obj['tracks']['items'][0]['album']['artists'][0]['id']
            # id_lst.append((title, artist, ids, rank))
