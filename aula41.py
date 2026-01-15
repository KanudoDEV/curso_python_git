""" while/else """

string = 'valor qualquer'

i = 0

while i < len(string):
    letra = string[1]

    print(letra)
    i += 1
else:
    print('O else foi executado.')

print('Fora do while.')