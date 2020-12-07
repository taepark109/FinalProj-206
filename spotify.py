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
BASE_URL = 'https://api.spotify.com/v1/search?'


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
                ids = obj['tracks']['items'][0]['album']['artists'][0]['id']
                id_lst.append((title, artist, ids, rank))
            else:
                artist = item[1].replace(feat, '')
                q= f"q=track:{title}%20artist:{artist}&type=track"
                r = requests.get(BASE_URL + q, headers=headers)
                txt = r.text
                obj = json.loads(txt)
                ids = obj['tracks']['items'][0]['album']['artists'][0]['id']
                id_lst.append((title, artist, ids, rank))
        else:
            q= f"q=track:{title}%20artist:{artist}&type=track"
            r = requests.get(BASE_URL + q, headers=headers)
            txt = r.text
            obj = json.loads(txt)
            ids = obj['tracks']['items'][0]['album']['artists'][0]['id']
            id_lst.append((title, artist, ids, rank))
    print(id_lst)
    return id_lst

def track_id_lstHot100(data_lst):
    # count = 0
    id_lst = []
    for item in data_lst:
        title = item[0]
        artist = item[1]
        rank = item[2]
        feat = "Featuring "
        if feat in item[1]:
            if item[1] == "Ellie Goulding X Diplo Featuring Swae Lee":
                artist = artist.replace("Ellie Goulding X Diplo Featuring Swae Lee", "Ellie Goulding & Diplo")
                q= f"q=track:{title}%20artist:{artist}&type=track"
                r = requests.get(BASE_URL + q, headers=headers)
                txt = r.text
                obj = json.loads(txt)
                ids = obj['tracks']['items'][0]['album']['artists'][0]['id']
                id_lst.append((title, artist, ids, rank))
            else:
                artist = item[1].replace(feat, '')
                q= f"q=track:{title}%20artist:{artist}&type=track"
                r = requests.get(BASE_URL + q, headers=headers)
                txt = r.text
                obj = json.loads(txt)
                ids = obj['tracks']['items'][0]['album']['artists'][0]['id']
                id_lst.append((title, artist, ids, rank))
        elif item[1] == "Gucci Mane X Bruno Mars X Kodak Black":
                artist = artist.replace("Gucci Mane X Bruno Mars X Kodak Black", "Gucci Mane Bruno Mars Kodak Black")
                q= f"q=track:{title}%20artist:{artist}&type=track"
                r = requests.get(BASE_URL + q, headers=headers)
                txt = r.text
                obj = json.loads(txt)
                ids = obj['tracks']['items'][0]['album']['artists'][0]['id']
                id_lst.append((title, artist, ids, rank))
        elif item[0] == "Ran$om":
                title = title.replace("Ran$om", "Ransom")
                q= f"q=track:{title}%20artist:{artist}&type=track"
                r = requests.get(BASE_URL + q, headers=headers)
                txt = r.text
                obj = json.loads(txt)
                ids = obj['tracks']['items'][0]['album']['artists'][0]['id']
                id_lst.append((title, artist, ids, rank))
        else:
            q= f"q=track:{title}%20artist:{artist}&type=track"
            r = requests.get(BASE_URL + q, headers=headers)
            txt = r.text
            obj = json.loads(txt)
            ids = obj['tracks']['items'][0]['album']['artists'][0]['id']
            id_lst.append((title, artist, ids, rank))

    print(id_lst)
    return id_lst

def track_id_lstAlt(data_lst):
    count = 0
    id_lst = []
    for item in data_lst:
        title = item[0]
        artist = item[1]
        rank = item[2]
        feat = "Featuring "
        apos = "'"
        if feat in item[1] and count < 2:
            if item[0] == "You're Somebody Else":
                title = title.replace("You're Somebody Else", "Youre Somebody Else")
                q= f"q=track:{title}%20artist:{artist}&type=track"
                r = requests.get(BASE_URL + q, headers=headers)
                txt = r.text
                obj = json.loads(txt)
                ids = obj['tracks']['items'][0]['album']['artists'][0]['id']
                id_lst.append((title, artist, ids, rank))
            else:
                artist = item[1].replace(feat, '')
                q= f"q=track:{title}%20artist:{artist}&type=track"
                r = requests.get(BASE_URL + q, headers=headers)
                txt = r.text
                obj = json.loads(txt)
                ids = obj['tracks']['items'][0]['album']['artists'][0]['id']
                id_lst.append((title, artist, ids, rank))
        elif apos in item[0]:
            title = title.replace(apos, "")
            q= f"q=track:{title}%20artist:{artist}&type=track"
            r = requests.get(BASE_URL + q, headers=headers)
            txt = r.text
            obj = json.loads(txt)
            ids = obj['tracks']['items'][0]['album']['artists'][0]['id']
            id_lst.append((title, artist, ids, rank))
        else:
            q= f"q=track:{title}%20artist:{artist}&type=track"
            r = requests.get(BASE_URL + q, headers=headers)
            txt = r.text
            obj = json.loads(txt)
            ids = obj['tracks']['items'][0]['album']['artists'][0]['id']
            id_lst.append((title, artist, ids, rank))

    print(id_lst)
    return id_lst
def main():
    Pop function works
    a = read_from_db('Pop')
    track_id_lstPop(a)
    a = read_from_db('Hot100')
    track_id_lstHot100(a)
    a = read_from_db('Alt')
    track_id_lstAlt(a)


if __name__ == '__main__':
    main()



#sample testing for song code:
            # q= f"q=track:{title}%20artist:{artist}&type=track"
            # r = requests.get(BASE_URL + q, headers=headers)
            # txt = r.text
            # obj = json.loads(txt)
            # ids = obj['tracks']['items'][0]['album']['artists'][0]['id']
            # id_lst.append((title, artist, ids, rank))
