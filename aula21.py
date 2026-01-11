# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras.
# Se qualquer valor for considerado falso, a expressão inteira
# será avaliada naquele valor
# São considerados Falsy
# 0 0.0 '' False
# Tambpem existe o tipo None que é 
# usado para representar um não valor

entrada = input('[E]ntrar [S]air ')
if entrada == 'E' or entrada == 'e':
    senha_digitada = input('Senha: ')
    senha_permitida = '123456'
    if senha_digitada == senha_permitida:
        print('Entrou!')
    else:
        print('Senha incorreta!')
elif entrada == 'S' or entrada == 's':
    print('Saiu!')
else:
    print('Comando desconhecido!')