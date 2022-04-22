import PySimpleGUI as sg

# work in progress, funktionalität und konfigurationsmöglichkeit muss noch ergänzt werden
sg.set_options(
    font="FiraCode 12", 
    background_color="#24292E", 
    text_element_background_color="#24292E",
    element_padding=(10,5)
    )

layout = [
    [sg.Titlebar(
        title = "Slicetify",
        icon = 'C:\\Users\\vince\\Documents\\GitHub\\Slicetify\\.github\\images\\logo_small.png',
        text_color ='#1ED760',
        font='FiraCode 18 bold',
        background_color = '#24292E',
        key = 'Titlebar',)],
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    [sg.Text('Select your ffmpeg folder:')],
    [sg.Combo(sorted(sg.user_settings_get_entry('-filenames0-', [])), 
        default_value=sg.user_settings_get_entry('-last filename-', ''), 
        size=(50, 1), 
        key='-FILENAME0-'), 
     sg.FileBrowse()],
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    [sg.Text('Select your audio file:')],
    [sg.Combo(sorted(sg.user_settings_get_entry('-filenames1-', [])), 
        default_value=sg.user_settings_get_entry('-last filename-', ''), 
        size=(50, 1), 
        key='-FILENAME1-'), 
     sg.FileBrowse()],
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    [sg.Text('Select your output folder:')],
    [sg.Combo(sorted(sg.user_settings_get_entry('-filenames-', [])), 
        default_value=sg.user_settings_get_entry('-last filename2-', ''), 
        size=(50, 1), 
        key='-FILENAME2-'), 
     sg.FileBrowse()],
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    [sg.Text('Enter your Spotify CLIENT_ID and CLIENT_SECRET:')],
    [sg.Text('CLIENT_ID:'), sg.Input(justification='right', expand_x=True)],
    [sg.Text('CLIENT_SECRET:'), sg.Input(justification='right', expand_x=True)],
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    [sg.B('Slice', 
        key='slice',
        expand_x=True)
    ],
    [sg.ProgressBar(1000, 
        key='progressbar',
        orientation='h', 
        size=(20, 20), 
        expand_x=True, 
        pad=(10,10)),
     sg.Text('x / y', 
        pad=(0,10))]
]

window = sg.Window("", layout)

while True:
    # open / close window
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    # Demo_Combo_Filechooser_With_History_And_Clear
    if event == 'Ok':
        # If OK, then need to add the filename to the list of files and also set as the last used filename
        sg.user_settings_set_entry('-filenames-', list(set(sg.user_settings_get_entry('-filenames-', []) + [values['-FILENAME-'], ])))
        sg.user_settings_set_entry('-last filename-', values['-FILENAME-'])
        break
    elif event == 'Clear History':
        sg.user_settings_set_entry('-filenames-', [])
        sg.user_settings_set_entry('-last filename-', '')
        window['-FILENAME-'].update(values=[], value='')

# close window
window.close()