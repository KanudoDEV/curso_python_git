""" 
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou impar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um número inteiro: ')


try:
    numero_inteiro = int(numero)
    if numero_inteiro % 2 == 0: 
        print('Este número é par')
    else:
        print('Este número é impar')
except:
    print('Você não digitou um número inteiro!')

""" 
Faça um programa que pergunte hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada.
Ex.: Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""

hora = input('Que horas são? ')

try:
    hora_int = int(hora)
    if hora_int <= 11:
        print('Bom dia')
    elif hora_int >= 12 and hora_int <= 17:
        print('Boa tarde')
    elif hora_int >=18:
        print('Boa noite')
except:
    print('Não é uma hora válida!')


""" 
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos, escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

nome = input('Digite seu nome: ')

if nome:
    tamanho_nome = len(nome)

    if tamanho_nome <=4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <=6:
        print('Seu nome é normal')
    elif tamanho_nome > 6:
        print('Seu nome é muito grande')
else:
    print('Digite alguma coisa')


