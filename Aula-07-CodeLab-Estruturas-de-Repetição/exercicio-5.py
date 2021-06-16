val1 = int(input("Valor 1 = "))
val2 = int(input("Valor 2 = "))
print("")

num = 0

while num==0:

    escolha = int(input("[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5]Sair do programa\nSua escolha = "))
    print("")
    if escolha==1:
        soma = val1 + val2
        print("O valor da soma é",soma)
        print("")
    if escolha == 2:
        mult = val1 * val2
        print("O valor da multiplação é",mult)
        print("")
    if escolha == 3:
        if val1>val2:
            maior = val1
        else:
            maior = val2
        print("O maior é",maior)
        print("")
    if escolha == 4:
        print("Escolha os novos valores")
        val1 = int(input("Valor 1 = "))
        val2 = int(input("Valor 2 = "))
        print("")
    if escolha == 5:
        exit()