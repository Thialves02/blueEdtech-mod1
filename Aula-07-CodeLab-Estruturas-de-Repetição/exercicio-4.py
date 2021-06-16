soma = 0

for i in range(6):
    valor = int(input("Digite um valor = "))
    if valor%2 == 0:
        soma = soma + valor
        
print("A soma dos valores é",soma)