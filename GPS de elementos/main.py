'''
Autor : Rafael Brant
Github : https://github.com/RafaelBrantPr
Últimas alterações : 11/05/2022
'''

from PySimpleGUI import PySimpleGUI as sg

#layout
sg.theme('Reddit')
layout = [
    ['Qtd. de Elementos',['2','3','4']],
    [sg.Text('1º item:'), sg.Input(size=(2), key='Prim.ele')],
    [sg.Text('2º item:'), sg.Input(size=(2), key='Segd.ele')],
    [sg.Text('3º item:'), sg.Input(size=(2), key='Terc.ele')],
    [sg.Text('Posição'), sg.Input(size=(30),key='posicao')],
    [sg.Button('Calcular'), sg.Text(key='saida')],
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
        seq1 = valores['Prim.ele']
        seq2 = valores['Segd.ele']
        seq3 = valores['Terc.ele']
        tam_seq = 3
        position = posicao%tam_seq
        if position == 0:
            position = seq3
        elif position == 1:
            position = seq1
        else:
            position = seq2
        janela['saida'].update(f"O elemento na {posicao}º posição é: {position}")

janela.close()