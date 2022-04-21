import PySimpleGUI as sg

# work in progress, funktionalität und konfigurationsmöglichkeit muss noch ergänzt werden

layout = [
    [sg.Titlebar(
        title = "Slicetify",
        icon = 'C:\\Users\\vince\\Documents\\GitHub\\Slicetify\\.github\\images\\logo_small.png',
        text_color ='#1ED760',
        background_color = '#24292E',
        font = 'FiraCode 20 bold',
        key = 'Titlebar',)],
    [sg.Text('Select your ffmpeg folder:', font='FiraCode 12 italic')],
    [sg.Combo(sorted(sg.user_settings_get_entry('-filenames-', [])), 
        default_value=sg.user_settings_get_entry('-last filename-', ''), 
        size=(50, 1), 
        key='-FILENAME0-'), sg.FileBrowse(), sg.B('Clear History')],
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    [sg.Text('Select your audio file:', font='FiraCode 12 italic')],
    [sg.Combo(sorted(sg.user_settings_get_entry('-filenames-', [])), 
        default_value=sg.user_settings_get_entry('-last filename-', ''), 
        size=(50, 1), 
        key='-FILENAME1-'), sg.FileBrowse(), sg.B('Clear History')],
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    [sg.Text('Select your output folder:', font='FiraCode 12 italic')],
    [sg.Combo(sorted(sg.user_settings_get_entry('-filenames-', [])), 
        default_value=sg.user_settings_get_entry('-last filename-', ''), 
        size=(50, 1), 
        key='-FILENAME2-'), sg.FileBrowse(), sg.B('Clear History')],
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    [sg.Text('Enter your Spotify CLIENT_ID and CLIENT_SECRET:', font='FiraCode 12 italic')],
    [sg.Text('CLIENT_ID:', font='FiraCode 12 italic'), sg.Input(font='FiraCode 12')],
    [sg.Text('CLIENT_SECRET:', font='FiraCode 12 italic'), sg.Input(font='FiraCode 12')],
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    [sg.Button('Slice', expand_x=True)]
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