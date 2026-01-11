"""
Tipos int e float
int -> números inteiros
O tipo int representa qualquer numero inteiro, positivo ou negativo. int sem sinal e considerado positivo.

float -> Numero com ponto flutuante
O tipo float representa qualquer numero positivo ou negativo com ponto flutuante. float sem sinal e considerado positivo.

A função type() mostra o tipo que o Python inferiu ao valor.

"""

# Tipo int
print(11) # int
print(-11) # int
print(0) # int

# Tipo float
print(1.1, 10.11) # float
print(0.0, -1.5) # float

# Imprimindo o tipo
print(type('Otavio'))
print(type(0))
print(type(1.1), type(-1.1), type(0.0))
