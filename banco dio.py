class ContaBancaria:
    def __init__(self, numero_da_conta):
        self.numero_da_conta = numero_da_conta
        self.saldo = 0

    def depositar(self, valor):
        if valor < 0:
            return "O valor do depósito deve ser positivo."
        self.saldo += valor
        return f"Depósito realizado com sucesso. Saldo atual: {self.saldo}"

    def sacar(self, valor):
        if valor < 0:
            return "O valor do saque deve ser positivo."
        if self.saldo < valor:
            return "Saldo insuficiente para o saque."
        self.saldo -= valor
        return f"Saque realizado com sucesso. Saldo atual: {self.saldo}"

    def obter_extrato(self):
        return f"Saldo atual: {self.saldo}"

class Banco:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, numero_da_conta):
        if numero_da_conta in self.contas:
            return "Número de conta já existe."
        self.contas[numero_da_conta] = ContaBancaria(numero_da_conta)
        return f"Conta {numero_da_conta} criada com sucesso."

    def realizar_deposito(self, numero_da_conta, valor):
        if numero_da_conta not in self.contas:
            return "Conta não encontrada."
        return self.contas[numero_da_conta].depositar(valor)

    def realizar_saque(self, numero_da_conta, valor):
        if numero_da_conta not in self.contas:
            return "Conta não encontrada."
        return self.contas[numero_da_conta].sacar(valor)

    def obter_extrato(self, numero_da_conta):
        if numero_da_conta not in self.contas:
            return "Conta não encontrada."
        return self.contas[numero_da_conta].obter_extrato()
