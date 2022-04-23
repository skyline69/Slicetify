from pydub import AudioSegment
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
from datetime import datetime

# fetches song id's from spotify playlist and puts them into a list
# two arguments (list that contains the song id's / playlist id (which contains the songs from your Spotify Playlist))
def getSongList(list, pl_id, spotifyClientCredentials):
    offset = 0
    while True:
        response = spotifyClientCredentials.playlist_items(pl_id,
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
def cutAndNameSongs(list, song_file, spotifyClientCredentials, output_folder):
    # variables
    counter = 0
    songfilelength = len(song_file)
    songstarttime = 0

    # iterates given list
    for songs in list:
        if len(sys.argv) > 1:
            urn = sys.argv[1]
        
        else:
            urn = 'spotify:track:' + songs
            counter +=1
            song_data = spotifyClientCredentials.track(urn)
            song_duration_spotify = song_data["duration_ms"]
            sec = round((song_duration_spotify/1000) % 60)
            min = int(song_duration_spotify/1000/60)

            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            print("fetching song: " + str(song_data["name"]) + "\n" + "duration: "
            + str(min) + " Minuten " + str(sec) + " Sekunden" +"\n" + "converting... " )
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            
            song_duration = len(song_file) - (songfilelength - song_duration_spotify)
            output = song_file[songstarttime:song_duration]
            output.export(output_folder + "/" + str(song_data["name"]) + ".mp3", format="mp3")
            songfilelength -= song_duration_spotify
            songstarttime += song_duration_spotify




