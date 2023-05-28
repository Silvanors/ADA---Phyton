# > LISTAS

# Antes
nota1 = 6
nota2 = 7
nota3 = 8

# Com Lista
notas = [6,7,8]

# Criando Listas
lista = []
lista = list()
lista = [26, "silvano", False]
lista_de_lista = [10, [1,2,3]]

# Indexação e Slices (fatiamento)
lista = [26, "silvano", False]

print(lista[0])
print(lista[1])
print(lista[2])
#print(lista[3])
print(lista[-1])

# Slices 
lista = [10,50,30,40,25,60,5]
print(lista[0:3]) # vai do índice 0 até < 3
print(lista[3:6]) # vai do índice 3 até < 6
print(lista[3:]) # vai do índice 3 até o final
print(lista[2:6:2]) # vai do índice 2 até < 6 pulando de dois em dois

# Iterações com o FOR
# 1. Utilizando os próprios elementos da lista

for elemento in lista:
    print(elemento)

# 2. Utilizando os índices

print("Comprimento da lista: ", len(lista)) # "len" de lenth

# 3. Utilizando len(lista) para o tamanho da lista

for i in range(len(lista)):
    print(i)

for i in range(len(lista)):
    print(lista [i])