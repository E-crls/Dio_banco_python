class ContaBancaria:
    def __init__(self, numero_da_conta):
        self.numero_da_conta = numero_da_conta
        self.saldo = 0

    def deposito(self, valor):
        self.saldo += valor
        return self.saldo

    def saque(self, valor):
        if self.saldo < valor:
            print("Saldo insuficiente.")
            return
        self.saldo -= valor
        return self.saldo

    def extrato(self):
        return self.saldo

class Banco:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, numero_da_conta):
        self.contas[numero_da_conta] = ContaBancaria(numero_da_conta)

    def deposito(self, numero_da_conta, valor):
        if numero_da_conta not in self.contas:
            print("Conta não encontrada.")
            return
        self.contas[numero_da_conta].deposito(valor)

    def saque(self, numero_da_conta, valor):
        if numero_da_conta not in self.contas:
            print("Conta não encontrada.")
            return
        self.contas[numero_da_conta].saque(valor)

    def extrato(self, numero_da_conta):
        if numero_da_conta not in self.contas:
            print("Conta não encontrada.")
            return
        return self.contas[numero_da_conta].extrato()
