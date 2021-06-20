nomes = []
idades = []
geral = []
total = []

maior = 0
menor = 0

for i in range(2):
    nome = input("Digite o nome = ").capitalize()
    idade = int(input("Digite sua idade = " ))

    nomes.append(nome)
    idades.append(idade)

    geral.append(nomes[:])
    
    if idade>=18:
        maior+=1
        maioridade = "Maior"
    else:
        menor+=1
        maioridade = "Menor"
    
    geral.clear()

    lista = (f"Nome: {nomes[i]} || Idade: {idades[i]} || Maioridade: {maioridade}")
    total.append(lista)

for e in range(2):
    print(total[e])
print(maior,"pessoa(s) são maiores de idade e",menor, "pessoa(s) são menores de idade.")
    