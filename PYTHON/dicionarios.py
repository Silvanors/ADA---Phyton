# > DICIONÁRIOS

# Criando dicionários

dicionario = {}
dicionario = dict()

dicionario = {"nome": "silvano", "idade": 30, "altura": 1.86}

print(dicionario)
print(dicionario["idade"])

# Adicionando elementos em um dicionário

dicionario["programador"] = True # adicionando

print(dicionario)

dicionario["altura"] = 2 # sobrescrevendo no que existe

print(dicionario)

# Iterando sobre um dicionário

for var in dicionario:
    print(var) # imprimi as chaves do dicionário

for chave in dicionario:
    print(chave, dicionario[chave]) # imprime chave 

# Testar se a chave já existe no dicionário

print("peso" in dicionario)
print("altura" in dicionario)