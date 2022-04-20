from pydub import AudioSegment
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys

# things to configure: song path and ffmpeg path / Spotify Playlist ID
song = AudioSegment.from_file("C:\\Users\\vince\\Desktop\\pydub\\song.mp3")
AudioSegment.converter = "C:\\ffmpeg\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffmpeg = "C:\\ffmpeg\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffprobe ="C:\\ffmpeg\\ffmpeg\\bin\\ffprobe.exe"

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# liste mit song id's / songlänge
songlist = []
songlength = []

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
    print()
    for lists in response['items']:
         for elements in lists.items():
             for subelements in elements:
                 if isinstance(subelements, str):
                     continue
                 for subsubelements in subelements.items():
                     for x in subsubelements[1::2]:
                         songlist.append(x)

for elements in songlist:
    print(elements)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# whyyyyyyyyyyyyyyyyyyyyyyy uwu
# get duration of 1 song in ms
counter = 0
songfilelength = len(song)
songstarttime = 0
for songs in songlist:
    if len(sys.argv) > 1:
        urn = sys.argv[1]
    else:
        urn = 'spotify:track:' + songs
        song_data = sp.track(urn)
        song_duration_spotify = song_data["duration_ms"]
        sec = round((song_duration_spotify/1000) % 60)
        min = int(song_duration_spotify/1000/60)
        print("fetching song: {artist} - {name}\n" + "duration: " + str(min) + " Minuten " + str(sec) + " Sekunden" +"\n" + "converting...")
        song_duration = len(song) - (songfilelength - song_duration_spotify)
        output = song[songstarttime:song_duration]
        output.export("C:/Users/vince/Desktop/pydub/output_" + str(counter) + ".mp3", format="mp3")
        songfilelength -= song_duration_spotify
        songstarttime += song_duration_spotify
        counter +=1
    print("finished: ", offset, "/", response['total'], "have been processed")