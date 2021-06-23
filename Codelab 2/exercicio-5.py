pessoa = {}
geral = []

soma = 0
media = 0
while True:
    pessoa={}
    pessoa['nome'] = input("Digite seu nome = ").title()
    pessoa['sexo'] = input("Digite seu sexo [F/M] = ").upper()
    while pessoa['sexo']!="F" and pessoa['sexo']!="M":
        print("DIGITE UM SEXO VÁLIDO [F/M]")
        pessoa['sexo'] = input("Digite seu sexo [F/M] = ").upper()
    pessoa['idade'] = int(input("Digite sua idade = "))
    geral.append(pessoa)
    soma += pessoa['idade']
    
    pergunta = input("Deseja continuar? = ").upper()
    while pergunta != "S" and pergunta != "N":
        pergunta = input("Deseja continuar? = ").upper()
    if pergunta == "N":
        break

media = soma/len(geral)

print(f'Ao todo temos {len(geral)} pessoas cadastradas e a média de idade é de {media:.2f} anos')
print(f'O nome das mulheres cadastradas são',end=' ')
for p in geral:
    if p['sexo'] == "F":
        print(f'{p["nome"]}',end=' ')
print('')
print(f'O nome das pessoas com idade acima da média são',end=' ')
for i in geral:
    if i['idade']>media:
        print(f'{i["nome"]}',end=' ')