
num = int(input("Digite um número\nSeu número = "))
l = []
c = []
l.append(num)

resposta = input("Deseja continuar?\nResposta = ").upper()

while resposta == "S":
    if num not in l:
        l.append(num)
    else:
        print("Número já adicionado")
    num = int(input("Digite um número\nSeu número = "))
    resposta = input("Deseja continuar?\nResposta = ").upper()
l.sort()
print("Sua lista é",l)