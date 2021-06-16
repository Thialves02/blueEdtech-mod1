num = int(input("Digite quantos valores vão ser somados"))
soma = 0
armazena = 0
for i in range(num):
    soma = float(input("Quais serão os valores? "))
    armazena = armazena + soma
print(armazena)