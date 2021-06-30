import random

moeda = ["Cara","Coroa"]
Dado = ['1','2','3','4','5','6']

class lancador:
    def __init__(self,escolha):
        self.escolha = escolha

    def dados(self):
        print(f'O lado do dado que caiu foi == {random.choice(Dado)}')

    def moeda(self):
        print(f'O lado da moeda que caiu foi == {random.choice(moeda)}')
        

escolha = input("Escolha entre dado ou moeda = ")
escolhido = lancador(escolha)

if escolha == "dado":
    escolhido.dados()
elif escolha == "moeda":
    escolhido.moeda()
