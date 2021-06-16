import random

rand = (random.randint(0, 10))
tentativa = int(input("Digite um número = "))
print(rand)
qntd = 0

while tentativa != rand:
    if tentativa>rand:
        tentativa = int(input("Digite um número menor"))
    else:
        tentativa = int(input("Digite um número maior"))
    qntd+=1

print("Você acertou!!!!")
print(qntd,"tentativas foram necessárias")