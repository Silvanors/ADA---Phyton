# > ESTRUTURAS CONDICIONAIS

idade = 20

# os dois pontos abaixo é similar a palavra "então"
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

"""
Imagine que você queira imprimir "Aprovada(o), caso o estudante tenha uma média 
superior ou igual a 7, e "Reprovado", caso a média inferior a 7.
"""

"""
media = float(input("Informe a média do estudante: "))


if media >= 7:
    print("Você foi aprovado(a)!")
elif media >= 5:
    print("Recuparação")
else:
    print("Você foi reprovada(o)")
"""

media = 10
presenca = 100

if media >= 7 and presenca >= 70:
    print("Aprovado!")
    print("Parabéns")
else:
    print("Reprovado")
    print("Tente novamente!")

