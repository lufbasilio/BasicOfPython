from conta import *

a = Conta("lucas",  899,    100,    200)
#           user    nCONTA  saldo   credito

b = Conta("fulano",  501,    200,    200)
#           user    nCONTA  saldo   credito


print "\nSISTEMA nuBANK\n"
print "Bem vindo " + a.user +" | Conta: "+str(a.numero)
print "Saldo: " + str(a.imprime_saldo())
print "Credito: " + str(a.credito)

op = str(raw_input("\nDeseja fazer um saque ?\ns-sim \nn-nao\n"))


if op == "s":
    saque = int(raw_input("\ninsira o valor: "))
    print a.sacar(saque)
elif op == "n":
    print "Encerrando sessao"
else:
    print "insira uma opcao valida\nencerrando sessao"