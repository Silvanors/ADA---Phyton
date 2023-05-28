
# o range (10) vai do 0 até o 9
"""for variavel in range(10):
    print(variavel)
"""

"""
# o range (1, 10) vai do 1 até o 9
for variavel in range(1, 10):
    print(variavel)

# Como faz para ir até o 11?
for variavel in range (1, 11):
    print(variavel)

# Como faz para pular de 3 em 3 ao invés de 1 em 1?
for variavel in range (1, 12, 3):
    print(variavel)
"""

""" 
nota1 = float(input("Informar sua nota 1: "))
nota2 = float(input("Informar sua nota 2: "))
nota3 = float(input("Informar sua nota 3: "))              
"""

soma = 0

for i in range(1, 4):
    nota = float(input(f"Informe a usa nota {i}: "))

    soma = soma + nota

print(soma / 3)