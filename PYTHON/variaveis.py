# > VARIÁVEIS

# 1. Variáveis

idade = 26 # Criando uma variável

print(idade)

nome = "Silvano Rodrigues"

print(nome)

"""
Tipos de variáveis:

1. int: números inteiros, ou seja, números sem parte decimal: 0, 5, -1, 1000
2. float: números reais, ou seja, números com parte decimal: 1.0, -2.7, 3.14
3. str: cadeias de caracteres, ou seja, dados textuais (string)
4. bool: valores lógicos (booleanos): True ou False
"""

idade = 26
altura = 1.77
nome: "Silvano"
estudando = True # Atenção ao case sensitive (maiúsculo/minisculo)

print( type(idade))
print( type(altura))
print( type(nome))
print( type(estudando))

# Obtendo dados do usuário e salvando em variáveis

linguagem = input("Qual é a linguagem de programação que você está estudando?")

print("A linguagem que você está estudando é", linguagem)