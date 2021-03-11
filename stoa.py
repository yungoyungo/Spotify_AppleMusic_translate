import sys
import requests
# import json

BASE_URL = 'https://api.spotify.com/v1/tracks/'
AUTHORIZATION_KEY = 'Bearer BQBYbVlR4XbHZI4MhnTzpLmK4E4ryks4D7OdXPK8UBgZ5YX8sA6zo-yiVZH6wrLP-SXrvtppbq8fLk2tNR06O3j5lePiQfXkq1VAmq7-_15ycQeeIsoVoyDH2jI5rGpvOddxT6yw3vY-a2gHCTwk4rJ4UnFiEEZkuR5uFd0'

if len(sys.argv) < 2:
    print('please url')
    sys.exit()

splitStr = sys.argv[1].split('/')
splitStr2 = splitStr[4].split('?')
track_id = splitStr2[0]
# print(track_id)
# sys.exit()

request_url = BASE_URL + track_id

get_header = {'Authorization': AUTHORIZATION_KEY}

response = requests.get(request_url, headers=get_header)

# print(response.text)

track = response.json()

for artist in track['artists']:
    print(artist['name'])
print(track['album']['name'])
print(track['name'])
