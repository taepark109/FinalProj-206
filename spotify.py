import requests
import json

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
def track_search_lst(database):
    #fill in code here
    #Get track and Artist
    #put into list of tuple
def find_trackid(lst):
    #requires a db 
    #loop through db getting each title and author
    # Search by title/author on Spotify for id
    #in another function, use id to get the different audio features
    #loop through tuple list to input track and artist and then append that to a list
    #this list of ids will be used to find the audio features
    q= f"q=track:{title}%20artist:{artist}&type=track"

    # actual GET request with proper header
    r = requests.get(BASE_URL + q, headers=headers)
    txt = r.text
    obj = json.loads(txt)
    ids = obj['tracks']['items'][1]['album']['artists'][0]['id']
    # print(ids)
    return ids