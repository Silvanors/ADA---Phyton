# > FUNÇÕES

# 1. O que são funções e por que utilizá-las?

# Funções que já utilizamos anteriormente...

"""
print()  # Imprimi uma mensagem (int, float, str) no console (terminal, cmd)
input()  # Retorna um dado informado pelo usuário (entrada padrão) e pode receber uma string
len()    # Recebe uma lista e retorna o tamanho da lista
max()    # Retorna o maior valor da lista
"""

# 2. Criação de funções

# Função inicial
def saudacao():
    print("Seja bem-vindo")
    print("Olá! É um prazer ter você fazendo parte desse curso")

saudacao()
saudacao()
saudacao()

# Função com parâmetros

def saudacao(nome, curso):
    print(f"Seja bem-vindo, {nome}!" )
    print(f"Olá! É um prazer ter você fazendo parte desse curso de {curso}!")

saudacao("Silvano", "Python")
saudacao("Ana", "JS")

# Função com parâmetros defaut

def saudacao(nome, curso = "Python"):
    print(f"Seja bem-vindo, {nome}!" )
    print(f"Olá! É um prazer ter você fazendo parte desse curso de {curso}!")

saudacao("Silvano")

# Função com retorno

def soma(num1, num2):
    return num1 + num2

resultado = soma(5,7)

print("O resultado da soma é", resultado)

def calculadora(num1, num2, operacao = "+"):
    if operacao == "+":
        return num1 + num2
    if operacao == "*":
        return num1 * num2
    if operacao == "/":
        return num1 / num2
    elif operacao == "-":
        return num1 - num2
    
resultado = calculadora(10,20, "-")
print(resultado)

resultado = calculadora(10,20, "+")
print(resultado)

resultado = calculadora(10,20, "*")
print(resultado)

resultado = calculadora(10,20, "/")
print(resultado)
    



