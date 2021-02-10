class Conta(object):

    #banco = "Nubank"

    def __init__(self, user, numero, saldo, credito): #construtor = recebe valores
        self.user = user
        self.numero = numero
        self.saldo = saldo
        self.credito = credito
        self.banco = "Nubank"


    def imprime_saldo(self):
        return self.saldo


    def sacar(self, valor):
        if valor > self.saldo + self.credito:
            return "Saldo insuficiente"
        else:
            return "Saque realizado"
