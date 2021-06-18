l = []
par = []
impar = []


while True:
    num = int(input("Digite um valor\nValor digitado = "))
    resposta = input("Deseja continuar?\nSua resposta = ").upper()
    if resposta == "N":
        break
    l.append(num)
    if num%2==0:
        par.append(num)
    else:
        impar.append(num)

print("A lista geral é",l)
print("A lista de pares é",par)
print("A lista de impares é",impar)


