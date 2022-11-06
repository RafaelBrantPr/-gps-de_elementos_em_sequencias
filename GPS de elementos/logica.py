'''
Autor : Rafael Brant
Github : https://github.com/RafaelBrantPr
Últimas alterações : 11/05/2022
'''

tam_seq = 3
seq1 = int(input('digite o 1º elemento da seq: '))
seq2 = int(input('digite o 2º elemento da seq: '))
seq3 = int(input('digite o 3º elemento da seq: '))
calc = int(input('Digite a posição do elemento: '))
position = calc%tam_seq

if position == 0:
    position = seq3
elif position == 1:
    position = seq1
else:
    position = seq2

print(f"O elemento na {calc}º posição é: {position}")