# ------------------- The New Way with history and clear -------------------
import PySimpleGUI as sg

layout = [
[sg.Combo(sg.user_settings_get_entry('-filenames-', []), 
    default_value=sg.user_settings_get_entry('-last filename-', ''), 
    size=(50, 1), 
    key='-FILENAME-'),
 sg.FileBrowse()],
[sg.Button('Save'), sg.B('Clear')]
]

window = sg.Window('Filename History Clearable', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    if event == 'Save':
        sg.user_settings_set_entry('-filenames-', list(set(sg.user_settings_get_entry('-filenames-', []) + [values['-FILENAME-'], ])))
        sg.user_settings_set_entry('-last filename-', values['-FILENAME-'])
        window['-FILENAME-'].update(values=list(set(sg.user_settings_get_entry('-filenames-', []))))
    elif event == 'Clear':
        sg.user_settings_set_entry('-filenames-', [])
        sg.user_settings_set_entry('-last filename-', '')
        window['-FILENAME-'].update(values=[], value='')