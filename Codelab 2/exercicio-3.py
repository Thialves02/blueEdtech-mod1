l = {}

while True:
    aluno = input("Digite o nome do aluno = ").title()
    media = float(input("Digite a média do aluno = "))
    l[aluno] = media

    if media>=7:
        aprovado = "APROVADO"
    elif media<=6.9 and media >=5:
        aprovado = "RECUPERAÇÃO"
    else:
        aprovado = "REPROVADO"
    print(l)

    resposta = input("Deseja adicionar outro aluno [S/N]? = ").upper()
    if resposta == "N":
        break

for k, v in l.items():
        print("O aluno(a)",k ,"foi",v)
        