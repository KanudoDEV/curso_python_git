# Operadores in e not in
# String são iteráveis
#  0 1 2 3 4 5
#  M o i s e s
# -6-5-4-3-2-1

nome = 'Moisés'

print(nome[2])
print(nome[-4])

print('i' in nome)
print('z' in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print (f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')