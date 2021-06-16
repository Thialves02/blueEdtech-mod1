pessoas = 7
menor = 0
maior = 0


for i in range(pessoas):
    ano = int(input("Digite o ano do seu nascimento = "))
    if ano <2002:
        menor+=1
    else:
        maior+=1
print(menor,"pessoas são menores de idade")
print(maior,"pessoas são maiores de idade")