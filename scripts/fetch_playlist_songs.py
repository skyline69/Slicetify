from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from pprint import pprint

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

# Edit playlist here     :xyzxyzxyzxyzxyzxyzxyz
pl_id = 'spotify:playlist:0OS0TpWHSXo7RCfBr2TfE4'
offset = 0

while True:
    response = sp.playlist_items(pl_id,
                                 offset=offset,
                                 fields='items.track.id,total',
                                 additional_types=['track'])
    
    if len(response['items']) == 0:
        break
    
    offset = offset + len(response['items'])
    pprint(response['items'])
    print(offset, "/", response['total'])
    print()
    for key in response['items']:
         print(key)