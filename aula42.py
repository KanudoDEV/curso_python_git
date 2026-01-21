frase = 'aaa a i ooooaaa'

i = 0
qtd_final = 0
letra_final = ''
while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_atual = frase.count(letra_atual)

    if qtd_final < qtd_atual:
        qtd_final = qtd_atual
        letra_final = letra_atual

    i += 1

print(f'A letra que apareceu mais vezes foi o '
      f'"{letra_final}" que apareceu '
      f'{qtd_final}x')