class Conta:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo
    def sacar(self,saque):
        self.saldo =self.saldo - saque
        print(f'Saldo {self.saldo}')
    def deposito(self,deposito):
        self.saldo =self.saldo+ deposito
        print(f'Saldo {self.saldo}')

Conta = Conta("Thiago",1200)

Conta.sacar(200)

Conta.deposito(500)
