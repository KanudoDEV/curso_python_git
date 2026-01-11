"""
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é:
        Seu nome invertido é:
        Se nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada foi digitado em nome ou idade:
    Exiba:
        "Desculpe, você deixou campos vazios."
"""

# Pede nome e idade do usuário
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

# Testa se o usuário não deixou campos vazios
if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    # Testa se no nome digitado tem ou não espaços
    if ' ' in nome:
        print('Seu nome tem espaços!')
    else:
        print('Seu nome não tem espaços!')
        
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios.')