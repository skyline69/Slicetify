import PySimpleGUI as sg
import app as app
from pydub import AudioSegment
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# file and folder information
audio_path, ffmpeg_path, output_path = '','',''
# spotify information
sp_pl, sp_id, sp_se = '','',''

# local variables
songlist = []
song = ''

credentials = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

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
        # spotify
        sp_pl = str(values['-PLAYLIST_ID-'])
        sp_id = 'spotify:playlist:' + str(values['-CLIENT_ID-'])
        sp_se = str(values['-CLIENT_SECRET-'])

        if output_path == '' or sp_pl == '' or ffmpeg_path == '' or audio_path == '':
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
        app.getSongList(songlist, sp_pl, credentials)
        app.cutAndNameSongs(songlist, song, credentials, output_path)

# close window #
window.close()