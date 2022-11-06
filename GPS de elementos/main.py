'''
Autor : Rafael Brant
Github : https://github.com/RafaelBrantPr
Últimas alterações : 11/05/2022
'''

from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')
# All the stuff inside your window.
layout = [  [sg.Text('1º elemento:'), sg.InputText(size=15, key='F_ele')],
            [sg.Text('2º elemento:'), sg.InputText(size=15, key='S_ele')],
            [sg.Text('3º elemento:'), sg.InputText(size=15, key='T_ele')],
            [sg.Text('Posição'), sg.InputText(size=25, key='posicao')],
            [sg.Button('Calcular'), sg.Button('Sair')],
            [sg.Text('', key='saida')] ]

# Create the Window
window = sg.Window('Window Title', layout)

# Code
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Sair':
        break
    if event == 'Calcular':
        seq1 = values['F_ele']
        seq2 = values['S_ele']
        seq3 = values['T_ele']
        posicao = int(values['posicao'])
        calc = posicao%3

        if calc == 0:
            calc = seq3
        elif calc == 1:
            calc = seq1
        else:
            calc = seq2
        window['saida'].update(f"O elemento na {posicao}º posição é: {calc}")

window.close()