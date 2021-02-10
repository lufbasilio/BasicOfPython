import math

def raiz(numero):
    return math.sqrt(numero)



n = int(raw_input("Insira um numero "))

result = raiz(n)

print "Raiz quadrada de " + str(n) + " = " + str(result)