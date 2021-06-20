nomes = []
idades = []

while True:
    nome = input("Digite o nome da pessoa = ")
    idade = int(input("Digite a idade da pessoa = "))
    continua = input("Deseja continuar? = ").upper()

    nomes.append(nome)
    idades.append(idade)

    if continua == "N":
        break

print(len(nomes),"pessoas foram cadastradas")
print("A pessoa com maior idade tem",max(idades),"anos")
print("A pessoa com menor idade tem",min(idades),"anos")