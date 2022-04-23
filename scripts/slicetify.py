import PySimpleGUI as sg
import sys
from pydub import AudioSegment
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

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
                         for subsubsubelements in subsubelements[1::2]:
                             list.append(subsubsubelements)

# cuts and names songs based on the list of songs it gets
# one argument (list of songs from (getSonglist()))
def cutAndNameSongs(list, song_file, spotifyClientCredentials, output_folder):

    # variables
    counter = 0
    # length of the audio file that will be slice (in ms)
    songfilelength = len(song_file)
    # Time at which the next song will be sliced (starting at 0)
    # --> Configurable if audio is not in sync with playlist
    songstarttime = 0

    # iterates given list (previously filled with getSongList() )
    for songs in list:
        # no idea what this does, but it says so in the spotipy docs lmao
        if len(sys.argv) > 1:
            urn = sys.argv[1]
        # otherwise get the current song in the loop, get the duration and slice it accordingly 
        else:
            urn = 'spotify:track:' + songs
            counter +=1
            # song_data contains all song information (probably type(dict)) 
            song_data = spotifyClientCredentials.track(urn)
            song_duration_spotify = song_data["duration_ms"]
            # self explainatory: gets time in seconds and minutes of the iterated song
            sec = round((song_duration_spotify/1000) % 60)
            min = int(song_duration_spotify/1000/60)

            # debug print to check for current song 
            #print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            #print("fetching song: " + str(song_data["name"]) + "\n" + "duration: "
            #+ str(min) + " Minuten " + str(sec) + " Sekunden" +"\n" + "converting... " )
            #print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            
            # calculates song length based on the difference of the whole audio file
            song_duration = len(song_file) - (songfilelength - song_duration_spotify)
            # specifies the start and end time of the song that needs to be sliced of the audio file
            output = song_file[songstarttime:song_duration]
            # exports the sliced file and formats it after the name that was fetched from the Spotify API
            output.export(output_folder + "/" + str(song_data["name"]) + ".mp3", format="mp3")
            # recalculates the new time of variables
            songfilelength -= song_duration_spotify
            songstarttime += song_duration_spotify

# file and folder information
audio_path, ffmpeg_path, output_path = '','',''
# spotify information
sp_pl, sp_id, sp_se = '','',''
credentials = ''

# audio file and list of songs in that audio file
song = ''
songlist = []

# default configuration of every UI element #
sg.set_options(
    font="FiraCode 12", 
    background_color="#24292E", 
    text_element_background_color="#24292E",
    )

layout = [

    # Customized title bar (Spotify / GitHub themed)
    [sg.Titlebar(
        title = "Slicetify",
        icon = 'C:\\Users\\vince\\Documents\\GitHub\\Slicetify\\.github\\images\\logo_small.png',
        text_color ='#1ED760',
        font='FiraCode 18 bold',
        background_color = '#24292E',
        key = 'Titlebar',)],

    # HeadLine #
    [
        sg.Text(
            text="Folder Setup", 
            justification='left', 
            expand_x=True, 
            font='FiraCode 12 bold underline', 
            text_color='#1ED760'),
        sg.Push(),
        sg.Text(
            text="Log", 
            justification='right', 
            expand_x=True, 
            font='FiraCode 12 bold underline', 
            text_color='#1ED760'),
    ],

    # AUDIO FILE BROWSER #
    [ 
        sg.FileBrowse(
            button_text ='audio file',
            key = '-AUDIO_BROWSER-',
            size=(10,1),
            file_types = (('MP3 Files', '*.mp3'),)),
        sg.InputText(size=(30, 1), key='-AUDIO_INPUT-')
    ],

    # FFMPEG FILE BROWSER #
    [
        sg.FolderBrowse(
            button_text ='ffmpeg folder',
            key = '-FFMPEG_BROWSER-',
            size=(10,1)),
        sg.InputText(size=(30, 1), key='-FFMPEG_INPUT-')
    ],

    # OUTPUT FILE BROWSER #
    [
        sg.FolderBrowse(
            button_text ='output folder',
            key = '-OUTPUT_BROWSER-',
            size=(10,1)),
        sg.InputText(size=(30, 1), key='-OUTPUT_INPUT-')
    ],
    
    # Spotify Playlist/ID/SECRET setup #
    [sg.Text("Spotify Setup", font='FiraCode 12 bold underline', text_color='#1ED760')],
    # SPOTIFY PLAYLIST_ID #
    [
        sg.Button(
        key='-PLAYLIST_ID_SAVE-',
        button_text='playlist_id', 
        size=(10,1)),
        sg.Input(
        key='-PLAYLIST_ID-',
        size=(30,2))
    ],
    # SPOTIFY CLIENT_ID #
    [
        sg.Button(
        key='-CLIENT_ID_SAVE-',
        button_text='client_id',
        size=(10,1)),
        sg.Input(
        key='-CLIENT_ID-',
        size=(30,2))
    ],
    # SPOTIFY CLIENT_SECRET #
    [
        sg.Button(
        key='-CLIENT_SECRET_SAVE-',
        button_text='client_secret',
        size=(10,1)), 
        sg.Input(
        key='-CLIENT_SECRET-',
        size=(30,2))
    ],
    
    # SLICE AND PROGRESSBAR #
    [sg.Button(
        button_text='SAVE', 
        font='FiraCode 14 bold',
        button_color='#1ED760',
        key='-SAVE-',
        size=(31, 1))
    ],
    [sg.Button(
        button_text='SLICE', 
        disabled=True,
        font='FiraCode 20 bold',
        button_color='#1ED760',
        key='-SLICE-',
        size=(22, 1))
    ]
    #[sg.ProgressBar(max_value=100, key='progressbar',orientation='h', size=(29.5, 40), visible=False)]
]

# display window #
window = sg.Window("", layout)

# window loop #
while True:

    # open / close window
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    # save input to variables for further processing (no check yet if valid!!!)
    if event == '-SAVE-': 
        # paths
        audio_path = values['-AUDIO_INPUT-']
        ffmpeg_path = values['-FFMPEG_INPUT-']
        output_path = values['-OUTPUT_INPUT-']
        # sets spotify information for API to work
        sp_pl = values['-PLAYLIST_ID-'] 
        sp_id = values['-CLIENT_ID-']
        sp_se = values['-CLIENT_SECRET-']
            
        credentials = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=str(sp_id), client_secret=str(sp_se)))

        if output_path == '' or sp_pl == '' or ffmpeg_path == '' or audio_path == '' or sp_id == '' or sp_se == '':
            window['-SLICE-'].update(disabled=True)
        else:
        # enable slice button
            window['-SLICE-'].update(disabled=False)

        # custom path
        song = AudioSegment.from_file(audio_path)
        converter = ffmpeg_path + '/bin/ffmpeg.exe'
        ffmpeg = ffmpeg_path + '/bin/ffmpeg.exe'
        probe = ffmpeg_path + '/bin/probe.exe'

        #window['progressbar'].update(visible=True)
    if event == '-SLICE-':
        window['-SLICE-'].update(disabled=True)
        getSongList(songlist, sp_pl, credentials)
        cutAndNameSongs(songlist, song, credentials, output_path)

# close window #
window.close()