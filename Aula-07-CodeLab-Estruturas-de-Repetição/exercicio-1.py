maior = 0
menor = 0
peso = 0
for i in range(5):
    peso = int(input("Digite seu peso = "))
    if peso>maior:
        maior=peso
    
    if i == 0:
        menor=peso
    elif peso<menor:
        menor=peso
        
print("O maior peso é",maior)
print("O menor peso é",menor)