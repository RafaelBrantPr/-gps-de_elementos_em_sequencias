'''
Autor : Rafael Brant
Github : https://github.com/RafaelBrantPr
Últimas alterações : 11/05/2022
'''
#Just testing
from PySimpleGUI import PySimpleGUI as sg

#layout
sg.theme('Reddit')
layout = [
    [sg.Text('Posição'), sg.Input(key='posicao')],
    [sg.Button('Calcular')],
    [sg.Text(key='saida')]
]

#janela
janela = sg.Window("GPS de elementos em sequências", layout)

#Código
while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED:
        break
    if evento == 'Calcular':
        posicao = int(valores['posicao'])
        conta = posicao%3
        janela['saida'].update(f"O resto é: {conta}")

janela.close()