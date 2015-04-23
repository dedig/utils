import random,urllib2

lista = urllib2.urlopen("https://raw.githubusercontent.com/dedig/utils/master/Where%20to%20Eat/locais.txt")
tmp = lista.read()
restaurantes = tmp.split("\n")
random.shuffle(restaurantes)
print(restaurantes[0])
