from pydub import AudioSegment
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
from datetime import datetime

totalruntime=datetime.now()

# Sometime I replace it with a proper config file
song = AudioSegment.from_file("C:\\Users\\vince\\Desktop\\pydub\\song.mp3")
AudioSegment.converter = "C:\\ffmpeg\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffmpeg = "C:\\ffmpeg\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffprobe ="C:\\ffmpeg\\ffmpeg\\bin\\ffprobe.exe"

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

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
    for lists in response['items']:
         for elements in lists.items():
             for subelements in elements:
                 if isinstance(subelements, str):
                     continue
                 for subsubelements in subelements.items():
                     for x in subsubelements[1::2]:
                         songlist.append(x)

# I really need to comment that

counter = 0
songfilelength = len(song)
songstarttime = 0
for songs in songlist:
    if len(sys.argv) > 1:
        urn = sys.argv[1]
    else:
        urn = 'spotify:track:' + songs
        counter +=1
        song_data = sp.track(urn)
        song_duration_spotify = song_data["duration_ms"]
        sec = round((song_duration_spotify/1000) % 60)
        min = int(song_duration_spotify/1000/60)
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("fetching song: " + str(song_data["name"]) + "\n" + "duration: "
        + str(min) + " Minuten " + str(sec) + " Sekunden" +"\n" + "converting... " 
        + str(counter), "/ " + str(response['total']) + " have been processed")
        song_duration = len(song) - (songfilelength - song_duration_spotify)
        output = song[songstarttime:song_duration]
        output.export("C:/Users/vince/Desktop/pydub/" + str(song_data["name"]) + ".mp3", format="mp3")
        songfilelength -= song_duration_spotify
        songstarttime += song_duration_spotify

print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("finished: ", offset, "/", response['total'], "have been processed. It took\n" 
+ str(datetime.now()-totalruntime) + " seconds to process all songs.")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")