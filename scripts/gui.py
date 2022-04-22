import PySimpleGUI as sg

# work in progress, funktionalität und konfigurationsmöglichkeit muss noch ergänzt werden
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

    # AUDIO FILE BROWSER #
    [sg.Text("Folder Setup", font='FiraCode 12 bold underline', text_color='#1ED760')],
    [ 
        sg.FileBrowse(
            button_text ='audio file',
            key = 'audio_file',
            size=(10,1),
            file_types = (('MP3 Files', '*.mp3'),)),
        sg.InputText(size=(30, 1), key='audiokey')
    ],

    # FFMPEG FILE BROWSER #
    [
        sg.FolderBrowse(
            button_text ='ffmpeg folder',
            key = 'audio_file',
            size=(10,1)),
        sg.InputText(size=(30, 1), key='ffmpegkey')
    ],

    # OUTPUT FILE BROWSER #
    [
        sg.FolderBrowse(
            button_text ='output folder',
            key = 'audio_file',
            size=(10,1)),
        sg.InputText(size=(30, 1), key='outputkey')
    ],
    
    # Spotify Playlist/ID/SECRET setup #
    [sg.Text("Spotify Setup", font='FiraCode 12 bold underline', text_color='#1ED760')],
    # SPOTIFY PLAYLIST_ID #
    [
        sg.Button(
        button_text='playlist_id', 
        size=(10,1)),
        sg.Input(
        size=(30,2))
    ],
    # SPOTIFY CLIENT_ID #
    [
        sg.Button(
        button_text='client_id',
        size=(10,1)),
        sg.Input(
        size=(30,2))
    ],
    # SPOTIFY CLIENT_SECRET #
    [
        sg.Button(
        button_text='client_secret',
        size=(10,1)), 
        sg.Input(
        size=(30,2))
    ],
    
    # SLICE AND PROGRESSBAR #
    [sg.Button('Slice', 
        key='slice',
        size=(42, 2))
    ],
    [sg.ProgressBar(
        max_value=100, 
        key='progressbar',
        orientation='h', 
        size=(29.5, 40),
        visible=False)]
]

# display window #
window = sg.Window("", layout)

# window loop #
while True:

    # open / close window
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'slice':
        window['progressbar'].update(visible=True)

# close window #
window.close()