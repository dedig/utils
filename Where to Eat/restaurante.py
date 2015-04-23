import random

lista = open("locais.txt")
tmp = lista.read()
restaurantes = tmp.split("\n")
random.shuffle(restaurantes)
print(restaurantes[0])
