pessoas = {}
geral = []

qntd = 0
idade_geral = 0

while True:
    pessoas = {}
    qntd += 1
    nome = input("Digite seu nome = ").title()
    sexo = input("Digite seu sexo [F/M] = ").upper()
    while sexo!= "F" and sexo!= "M":
        sexo = input("Digite seu sexo [F/M] = ").upper()
    idade = int(input("Digite sua idade = "))
    idade_geral = idade_geral + idade
    media = idade_geral/2

    pessoas[nome] = sexo,idade
    geral.append(pessoas)

    pergunta = input("Deseja continuar [S/N]?").upper()
    while pergunta != "S" and pergunta != "N":
        pergunta = input("Deseja continuar [S/N]?").upper()
    if pergunta == "N":
        break
print(qntd,"pessoas estão contratadas e a média de idade é de",media,"anos")



