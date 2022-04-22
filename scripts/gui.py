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
    [
    sg.Combo(sg.user_settings_get_entry('-filenames1-', []), 
        default_value=sg.user_settings_get_entry('-last filename1-', ''), 
        size=(50, 1), 
        key='-FILENAME1-'),
        
        sg.FileBrowse(
        button_text ='Browse audio file',
        key = 'audio_file',
        size=(30,1),
        file_types = (('MP3 Files', '*.mp3'),))],

    # FFMPEG FILE BROWSER #
    [
    sg.Combo(sg.user_settings_get_entry('-filenames2-', []), 
        default_value=sg.user_settings_get_entry('-last filename2-', ''), 
        size=(50, 1), 
        key='-FILENAME2-'),
        
        sg.FileBrowse(
        button_text ='Browse ffmpeg folder',
        key = 'ffmpeg_folder',
        size=(30,1),
        file_types = (('ALL Files', '*.* *'),))],

    # OUTPUT FILE BROWSER #
    [
    sg.Combo(sg.user_settings_get_entry('-filenames3-', []), 
        default_value=sg.user_settings_get_entry('-last filename3-', ''), 
        size=(50, 1), 
        key='-FILENAME3-'),
    
    sg.FileBrowse(
        button_text ='Browse output folder',
        key = 'output_folder',
        size=(30,1),
        file_types = (('ALL Files', '*.* *'),))],
    [
    sg.Button('Save'), sg.B('Clear')
    ],
    
    # SPOTIFY #
    [sg.Text(
        text='Spotify CLIENT_ID:',
        justification='left',
        expand_x=True)], 
    [sg.Input(
         size=(30,2))],
    [sg.Text(
        text='Spotify CLIENT_SECRET:', 
        justification='left', 
        expand_x=True)],
    [sg.Input(
         size=(30,2))],

    # SLICE AND PROGRESSBAR #
    [sg.Button('Slice', 
        key='slice',
        size=(30, 2))
    ],
    [sg.ProgressBar(
        max_value=100, 
        key='progressbar',
        orientation='h', 
        size=(25, 20), 
        expand_x=True,
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

    # save and clear button
    if event == 'Save':
        # audio
        sg.user_settings_set_entry('-filenames1-', list(set(sg.user_settings_get_entry('-filenames1-', []) + [values['-FILENAME1-'], ])))
        sg.user_settings_set_entry('-last filename1-', values['-FILENAME1-'])
        window['-FILENAME1-'].update(values=list(set(sg.user_settings_get_entry('-filenames-', []))))
        # ffmpeg
        sg.user_settings_set_entry('-filenames2-', list(set(sg.user_settings_get_entry('-filenames2-', []) + [values['-FILENAME2-'], ])))
        sg.user_settings_set_entry('-last filename2-', values['-FILENAME2-'])
        window['-FILENAME1-'].update(values=list(set(sg.user_settings_get_entry('-filenames2-', []))))
        # output
        sg.user_settings_set_entry('-filenames3-', list(set(sg.user_settings_get_entry('-filenames3-', []) + [values['-FILENAME3-'], ])))
        sg.user_settings_set_entry('-last filename3-', values['-FILENAME3-'])
        window['-FILENAME3-'].update(values=list(set(sg.user_settings_get_entry('-filenames-', []))))
    elif event == 'Clear':
        #audio
        sg.user_settings_set_entry('-filenames-', [])
        sg.user_settings_set_entry('-last filename-', '')
        window['-FILENAME-'].update(values=[], value='')
        #ffmpeg
        sg.user_settings_set_entry('-filenames-', [])
        sg.user_settings_set_entry('-last filename-', '')
        window['-FILENAME-'].update(values=[], value='')
        #output
        sg.user_settings_set_entry('-filenames-', [])
        sg.user_settings_set_entry('-last filename-', '')
        window['-FILENAME-'].update(values=[], value='')

# close window #
window.close()