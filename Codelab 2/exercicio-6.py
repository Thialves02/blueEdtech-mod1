alunos = {}
geral = []
media = 0


for i in range(2):
    alunos = {}
    alunos['nome'] = input("Digite o nome do aluno = ").title()
    alunos['nota1'] = float(input("Digite a nota 1 = "))
    alunos['nota2'] = float(input("Digite a nota 2 = "))
    alunos['nota3'] = float(input("Digite a nota 3 = "))
    alunos['nota4'] = float(input("Digite a nota 4 = "))
    alunos['nota5'] = float(input("Digite a nota 5 = "))
    alunos['media'] = (alunos['nota1']+alunos['nota2']+alunos['nota3']+alunos['nota4']+alunos['nota5'])/5

    if alunos['media']>=7:
        alunos['aprovado'] = "APROVADO"
    elif alunos['media']<=6.9 and alunos['media'] >=5:
        alunos['aprovado'] = "RECUPERAÇÃO"
    else:
        alunos['aprovado'] = "REPROVADO"
    geral.append(alunos)
    print('')
for a in geral:
    print(f'O aluno {a["nome"]} teve como notas : nota 1 = {a["nota1"]}, nota 2 = {a["nota2"]}, nota 3 = {a["nota3"]}, nota 4 = {a["nota4"]}, nota 5 = {a["nota5"]}')
    print(f'A média do aluno {a["nome"]} foi de {a["media"]}, então o status de aprovação dele é : {a["aprovado"]}')
    print('')
