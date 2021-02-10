def add(nome):
    lista.append(nome)

def imprime():
    for i in lista:
        print i
##########################################
lista = []

print ""

for i in range(0, 5):
    n = raw_input("Insira um nome: ")
    add(n)

print ""

print("Lista de nomes:")
imprime()

