l = {}
while True:
    
    nome = input("Digite seu nome = ")
    ano = int(input("Digite o ano do seu nascimento = "))
    carteira = int(input("Número da carteira de trabalho = "))

    idade = 2021-ano

    if carteira != 0:
        contratacao = int(input("Ano de contratação? = "))
        salario = float(input("Qual seu salário? = "))
        idade_aposentar = ((contratacao - ano)+35)
    l[nome] = idade,carteira,contratacao,salario,idade_aposentar

    resposta = input("Deseja adicionar outra pessoa [S/N]? = ").upper()
    if resposta == "N":
        break

for k, v in l.items():
        print('O',k ,'tem',v[0],'anos',", o número da carteira é",v[1],",ele(a) foi contratado em",v[2],", tem salário de R$",v[3],'e vai se aposentar com ',v[4],"anos")

        

