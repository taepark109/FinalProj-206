import sqlite3
import requests
import json
import re
import os


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

# base URL for all Spotify API endpoints



#write function to get a list of tuples (track, artist)
def read_from_db(table):
    #fill in code here
    #Get track and Artist
    #put into list of tuple
    conn = sqlite3.connect('Music.db') 
    cur = conn.cursor() 
    cur.execute(f'SELECT * FROM {table}')
    #puts (title, artist, rank) of all items in list
    data = cur.fetchall()
    return data

def track_id_lstPop(data_lst):
    BASE_URL = 'https://api.spotify.com/v1/search?'
    count = 0
    id_lst = []
    for item in data_lst:
        title = item[0]
        artist = item[1]
        rank = item[2]
        feat = "Featuring "
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
    # print(id_lst)
    return id_lst

def track_id_lstHot100(data_lst):
    BASE_URL = 'https://api.spotify.com/v1/search?'
    count = 0
    id_lst = []
    for item in data_lst:
        title = item[0]
        artist = item[1]
        rank = item[2]
        feat = "Featuring "
        if item[0] == 'Bury A Friend':
            q= f"q=track:Bury A Friend%20artist:Billie Eilish&type=track"
            r = requests.get(BASE_URL + q, headers=headers)
            txt = r.text
            lst = []
            obj = json.loads(txt)
            ids = obj['tracks']['items'][0]['id']
            # print(ids)
            id_lst.append((title, artist, ids, rank))
        elif feat in item[1]:
            if item[1] == "Ellie Goulding X Diplo Featuring Swae Lee":
                artist = artist.replace("Ellie Goulding X Diplo Featuring Swae Lee", "Ellie Goulding & Diplo")
                q= f"q=track:{title}%20artist:{artist}&type=track"
                r = requests.get(BASE_URL + q, headers=headers)
                txt = r.text
                obj = json.loads(txt)
                # print(obj)
                ids = obj['tracks']['items'][1]['id']
                # print(ids)
                id_lst.append((title, artist, ids, rank))
            else:
                artist = item[1].replace(feat, '')
                q= f"q=track:{title}%20artist:{artist}&type=track"
                r = requests.get(BASE_URL + q, headers=headers)
                txt = r.text
                obj = json.loads(txt)
                # ids = obj['tracks']['items'][0]['album']['artists'][0]['id']
                #Not sure if this gets the right link (next line)
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
            #problem lies here
            ids = obj['tracks']['items'][1]['id']
            # print(ids)
            # print(ids)
            id_lst.append((title, artist, ids, rank))

    # print(id_lst)
    return id_lst

def track_id_lstAlt(data_lst):
    BASE_URL = 'https://api.spotify.com/v1/search?'
    count = 0
    id_lst = []

    # q= f"q=track:Go%20artist:The Black Keys&type=track"
    # r = requests.get(BASE_URL + q, headers=headers)
    # txt = r.text
    # obj = json.loads(txt)
    # # print(obj)
    # ids = obj['tracks']['items'][1]['id']
    # print(ids)
    # id_lst.append((title, artist, ids, rank))
    for item in data_lst:
        title = item[0]
        artist = item[1]
        rank = item[2]
        feat = "Featuring "
        apos = "'"
        if feat in item[1]:
            if item[0] == "You're Somebody Else":
                title = title.replace("You're Somebody Else", "Youre Somebody Else")
                q= f"q=track:{title}%20artist:{artist}&type=track"
                r = requests.get(BASE_URL + q, headers=headers)
                txt = r.text
                obj = json.loads(txt)
                print(obj)
                ids = obj['tracks']['items'][1]['id']
                print(ids)
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

    # print(id_lst)
    return id_lst

def check_tracks(id_lst):
    lst = []
    #list of ids
    for x in id_lst:
        t_id = x[2]
        lst.append(t_id)
    # print(lst)
    
    BASE_URL = 'https://api.spotify.com/v1/tracks/'
    count = 0
    for x in lst:
        r = requests.get(BASE_URL + x, headers=headers)
        txt = r.text
        obj = json.loads(txt)
        track_name = obj['name']
        print(track_name)

#Use ID's to find the audio features for songs: Valence
def setupvalence(lst, track_name):
    BASE_URL = 'https://api.spotify.com/v1/'
    val_lst = []
    #loop through list and each time get the id

        #creating val_lst
        # val_lst.append((title, artist, val, rank))
    #put into database
    conn = sqlite3.connect('Music.db')
    cur = conn.cursor()
    #is using an fstring okay for this?
    cur.execute(f'''CREATE TABLE IF NOT EXISTS {track_name}
        (title TEXT, artist TEXT, valence FLOAT, rank INTEGER)''')
    title_lst = []
    count = 0
    data = cur.execute(f'''SELECT title FROM {track_name}''')
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
        val = obj['valence']
        tup = title, artist, val, rank
        if count == 25:
            break
        if tup[0] in title_lst:
            continue
        else:
            cur.execute("INSERT OR IGNORE INTO Hot100(title, artist, valence, rank) VALUES (?,?,?, ?)", (title, artist, val, rank))
            count += 1
    conn.commit()
    conn.close()


    #get the valence and append it to the val list ((track, artist, valence, rank))


    # Track ID from the URI
    #test track below:
    # track_id = '17C1AVZVh5jhJU4eAcovpl'

    # actual GET request with proper header

    
    # conn = sqlite3.connect('Music.db')
    # cur = conn.cursor()


def main():
    # a = read_from_db('Pop')
    # lst = track_id_lstPop(a)
    # check_tracks(lst)
    # check_tracks(lst)
    # a = read_from_db('Alt')
    # lst = track_id_lstAlt(a)
    # check_tracks(lst)
    a = read_from_db('Hot100')
    lst = track_id_lstHot100(a)
    setupvalence(lst)

if __name__ == '__main__':
    main()



#sample testing for song code:
            # q= f"q=track:{title}%20artist:{artist}&type=track"
            # r = requests.get(BASE_URL + q, headers=headers)
            # txt = r.text
            # obj = json.loads(txt)
            # ids = obj['tracks']['items'][0]['album']['artists'][0]['id']
            # id_lst.append((title, artist, ids, rank))
