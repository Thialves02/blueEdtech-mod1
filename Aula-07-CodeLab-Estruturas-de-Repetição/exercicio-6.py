soma = 0
maior = 0
menor = 100000
nome_menor = ""
mais = 0



nome = input("Digite o nome do produto = ")
prec = int(input("Digite opreço do produto = "))
pergunta = input("Deseja continuar [S/N]?").upper()
soma = soma + prec 
print("")
while pergunta == "S":
    nome = input("Digite o nome do produto = ")
    prec = int(input("Digite opreço do produto = "))
    pergunta = input("Deseja continuar [S/N]?").upper()
    print("")
    soma = soma + prec 
    if prec>1000:
        mais+=1
    if prec<menor:
        menor=prec
        print(nome)
        nome_menor = nome
print("O total gasto foi de",soma)
print(mais,"produtos custam mais que R$1000")
print("O produto",nome_menor,"foi o mais barato")
