# > METODOS DE LISTAS

lista = [1, 3, 12, 8,2]

#  append -> adiciona ao final
print("Antes do append", lista)

lista.append(3)

print("Depois do append", lista)

# insert -> você pode escolher aonde colocar

lista.insert(2, 10) # adiciona o elemento "10" logo no índice 2

print("Depois do insert", lista)


# extend -> para juntar duas listas pega os elementos e joga no final

lista2 = [1,2,3]

lista.extend(lista2)

print("Depois do extend", lista)

# pop -> remover elemento o último elemento ou o que for especificado

lista.pop() # elimina o último
print("Lista após o pop", lista)

lista.pop(0) # elimina o elemento de índice "0"
print("Lista após o pop", lista)

# remove -> remove o elemento, não o índice

lista.remove(3) # o remove remove o primeiro elementro que encontra
print("Lista após o remove", lista)

# count

print("Quantidade de 2 na lista", lista.count(2))

# index -> diz o índice de determinado elemento

print("Índice do elemento 12", lista.index(12))

# sort -> para ordenar a lista

lista.sort() # ordena na ordem crescente
print("Ordem crescente", lista ) 

lista.sort(reverse=True) # ordena na ordem decrescente
print("Ordem decrescente", lista )

# len -> saber quantos elementos tem na lista

print("Tamanho da lista:", len(lista))

# sum -> soma os elementos da lista

print("Soma da lista:", sum(lista))

# max -> maior elemento da lista

print("Maior elemento da lista:", max(lista))

# min -> menor elemento da lista

print("Menor elemento da lista:", min(lista))

