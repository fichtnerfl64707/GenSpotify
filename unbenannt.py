

import json
import requests

CLIENT_ID = 'e1018b965d0348cf9ab9df8fcb5bf2c1'
CLIENT_SECRET = '39197de95da642dcbfd830323392ed92'

AUTH_URL = 'https://accounts.spotify.com/api/token'

# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# convert the response to JSON
auth_response_data = auth_response.json()

if 'access_token' in auth_response_data:
    # save the access token
    access_token = auth_response_data['access_token']
    print("Anmeldung bei Spotify erfolgreich.")
else:
    print("Fehler bei der Anmeldung bei Spotify.")

# Verwende den Zugriffstoken, um Song-Informationen abzurufen (hier ein Dummy-Song)
# song_id = '11dFghVXANMlKmJXsNCbNl'  # Ersetze SPOTIFY_SONG_ID durch die tatsächliche Song-ID
SPOTIFY_API_URL = "https://api.spotify.com/v1/me/player/currently-playing"
#f'https://api.spotify.com/v1/tracks/{song_id}'

headers = {
    'Authorization': f'Bearer {access_token}',
}

#test

response = requests.get(SPOTIFY_API_URL, headers=headers)

song_info = response.json()

if 'album' in song_info and 'images' in song_info['album']:
    cover_url = song_info['album']['images'][0]['url']
    response = requests.get(cover_url)
    if response.status_code == 200:
        with open('cover_image.jpg', 'wb') as f:
            f.write(response.content)
        print("Cover-Image wurde gespeichert.")
    else:
        print("Fehler beim Herunterladen des Cover-Images.")
else:
    print("Album-Informationen oder Cover-Image nicht verfügbar.")
