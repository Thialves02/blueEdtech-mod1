class pessoa:
    def __init__(self,nome,idade,peso,altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade +=1
        if self.altura<21:
            self.altura = self.altura + 0.05
            print(f"Seu nome é {self.nome}, sua nova idade é {self.idade}, seu peso é {self.peso} e sua nova altura é {self.altura}")
        else:
            print(f"Seu nome é {self.nome}, sua nova idade é {self.idade}, seu peso é {self.peso} e sua altura é {self.altura}")
    def engordar(self):
        self.peso += 1
        print(f"Seu nome é {self.nome}, sua idade é {self.idade}, seu novo peso é {self.peso} e sua altura é {self.altura}")

    def emagrecer(self):
        self.peso +=1
        print(f"Seu nome é {self.nome}, sua idade é {self.idade}, seu novo peso é {self.peso} e sua altura é {self.altura}")

    def crescer(self):
        self.altura+=0.1
        print(f"Seu nome é {self.nome}, sua idade é {self.idade}, seu peso é {self.peso} e sua nova altura é {self.altura}")

    def sair(self):
        print("=-"*25)
        print("============ OBRIGADO POR PARTICIPAR ============")
        print("=-"*25)
        return

nome = input("Digite seu nome = ").title()
idade = int(input("Digite sua idade = "))
peso = int(input("Digite seu peso = "))
altura = float(input("Digite sua altura = "))

while True:
    escolha = int(input("O que deseja fazer?\n[1] ENVELHECER \n[2] ENGORDAR\n[3] EMAGRECER\n[4] SAIR\nSUA ESCOLHA = "))
    usuario = pessoa(nome,idade,peso,altura)
    if escolha == 1:
        usuario.envelhecer()
    elif escolha == 2:
        usuario.engordar()
    elif escolha == 3:
        usuario.emagrecer()
    elif escolha == 4:
        usuario.sair()

    print("")
    continuar = input("Deseja continuar[S/N]? = ").upper()
    if continuar == 'N':
        print("")
        print("=-"*25)
        print("============ OBRIGADO POR PARTICIPAR ============")
        print("=-"*25)
        break
        