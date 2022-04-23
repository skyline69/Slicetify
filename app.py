from pydub import AudioSegment
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
from datetime import datetime

# variable declaration
totalruntime=datetime.now()
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
playlist_songlist = []
songlength = []
playlist_id = 'spotify:playlist:45OOE0Q5yV9u3uRiSEFdpe'
song = AudioSegment.from_file("C:\\Users\\vince\\Desktop\\Slicetify\\song.mp3")
AudioSegment.converter = "C:\\ffmpeg\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffmpeg = "C:\\ffmpeg\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffprobe ="C:\\ffmpeg\\ffmpeg\\bin\\ffprobe.exe"

# fetches song id's from spotify playlist and puts them into a list
# two arguments (list that contains the song id's / playlist id (which contains the songs from your Spotify Playlist))
def getSongList(list, pl_id):
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
                             list.append(x)

# cuts and names songs based on the list of songs it gets
# one argument (list of songs from (getSonglist()))
def cutAndNameSongs(list):
    # variables
    counter = 0
    songfilelength = len(song)
    songstarttime = 0

    # iterates given list
    for songs in list:
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
            + str(min) + " Minuten " + str(sec) + " Sekunden" +"\n" + "converting... " )
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            
            song_duration = len(song) - (songfilelength - song_duration_spotify)
            output = song[songstarttime:song_duration]
            output.export("C:/Users/vince/Desktop/Slicetify/" + str(song_data["name"]) + ".mp3", format="mp3")
            songfilelength -= song_duration_spotify
            songstarttime += song_duration_spotify




