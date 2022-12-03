'''
Author : Rafael Brant
Github profile : https://github.com/RafaelBrantPr
Últimas alterações : 12/03/2022
'''

#Lógic behind the app
seq1 = (input('Enter the 1º element of the seq: '))
seq2 = (input('Enter the 2º element of the seq: '))
seq3 = (input('Enter the 3º element of the seq: '))
position = int(input('Enter the position of the element: '))
calc = position%3

if calc == 0:
    calc = seq3
elif calc == 1:
    calc = seq1
else:
    calc = seq2

print(f"S=({seq1}, {seq2}, {seq3}, {seq1}, {seq2}, {seq3}, {seq1}, {seq2}, {seq3}...)")
print(f"The element at {position}º position is: {calc}")