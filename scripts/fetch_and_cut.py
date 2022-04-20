from pydub import AudioSegment
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys

# things to configure: song path and ffmpeg path / Spotify Playlist ID
song = AudioSegment.from_file("C:\\Users\\vince\\Desktop\\pydub\\song.wav")
AudioSegment.converter = "C:\\ffmpeg\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffmpeg = "C:\\ffmpeg\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffprobe ="C:\\ffmpeg\\ffmpeg\\bin\\ffprobe.exe"

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

# get duration of 1 song in ms
if len(sys.argv) > 1:
    urn = sys.argv[1]
else:
    urn = 'spotify:track:'

song_data = sp.track(urn)
song_duration_spotify = song_data["duration_ms"]

# get songs in playlist
pl_id = 'spotify:playlist:45OOE0Q5yV9u3uRiSEFdpe'
offset = 0

while True:
    response = sp.playlist_items(pl_id,
                                 offset=offset,
                                 fields='items.track.id,total',
                                 additional_types=['track'])
    
    if len(response['items']) == 0:
        break
    
    offset = offset + len(response['items'])
    #pprint(response['items'])
    print(offset, "/", response['total'])
    print()
    for key in response['items']:
         print(key)

# cut 1 song
song_duration = len(song) - (len(song)-song_duration_spotify)
output = song[:song_duration]

output.export("C:/Users/vince/Desktop/pydub/output.mp3", format="mp3")