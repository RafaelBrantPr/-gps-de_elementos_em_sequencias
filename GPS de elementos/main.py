'''
Author : Rafael Brant
Github profile : https://github.com/RafaelBrantPr
Últimas alterações : 12/03/2022
'''

from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')
# All the stuff inside your window.
layout = [  [sg.Text('1º element:'), sg.InputText(size=15, key='F_ele')],
    [sg.Text('2º element:'), sg.InputText(size=15, key='S_ele')],
    [sg.Text('3º element:'), sg.InputText(size=15, key='T_ele')],
    [sg.Text('Position'), sg.InputText(size=25, key='position')],
    [sg.Button('Calculate'), sg.Button('Quit')],#buttons to calc and leave the window
    [sg.Text('', key='Example')],#example of your sequence
    [sg.Text('', key='Output')]#output of the calc
]

# Create the Window
window = sg.Window('GPS of elements in sequences', layout)

# Code
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Quit':
        break
    if event == 'Calculate':
        seq1 = values['F_ele']
        seq2 = values['S_ele']
        seq3 = values['T_ele']
        position = int(values['position'])
        calc = position%3

        if calc == 0:
            calc = seq3
        elif calc == 1:
            calc = seq1
        else:
            calc = seq2
        window['Output'].update(f"The element at {position}º position is: {calc}")
        window['Example'].update(f"S=({seq1}, {seq2}, {seq3}, {seq1}, {seq2}, {seq3}, {seq1}, {seq2}, {seq3}....)")

window.close()