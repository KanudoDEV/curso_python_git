""" 
Iterando strings com while
"""

nome = 'Moisés Freitas'
tamanho_nome = len(nome)
contador = 0
novo_nome = ''

# print(nome)
# print(tamanho_nome)

while contador < tamanho_nome:
    letra = nome[contador]
    novo_nome += f'*{letra}'
    contador += 1
    
print(novo_nome)