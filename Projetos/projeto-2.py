import random

rand = ["PEDRA","PAPEL","TESOURA"]

eu = 0
pc = 0
rodadas = 0

while rodadas%2 == 0:
    print("Insira um valor ímpar para as rodadas")#Para mim não fez sentido o usuario poder escolher um número par, afinal nunca vi uma "melhor de 4/6/8..."
    rodadas = int(input("Digite quantas rodadas ira fazer\nVocê escolheu = "))
    print("")

while True:
    while eu<=(rodadas/2) or pc<=(rodadas/2):     
        escolhido = random.choice(rand)
        print(escolhido)
        escolha = input("Digite sua escolha = ").upper()
        if escolha == escolhido:
            eu+=0
            pc+=0
            print("\nEMPATE\n")
        elif escolha == "PEDRA" and escolhido == "TESOURA":
            eu+=1
        elif escolha == "TESOURA" and escolhido == "PEDRA":
            pc+=1

        elif escolha == "PAPEL" and escolhido == "PEDRA":
            eu+=1
        elif escolha == "PEDRA" and escolhido == "PAPEL":
            pc+=1
        
        elif escolha == "TESOURA" and escolhido == "PAPEL":
            eu+=1
        elif escolha == "PAPEL" and escolhido == "TESOURA":
            pc+=1

 
        if eu>=(rodadas/2) or pc>=(rodadas/2):
            break
        
        print("=====PLACAR ATUAL=====\nEU = ",eu,"\nPC = ",pc,"\n")

    if eu>pc:
        print("\nPARABENS VOCE FOI O CAMPEAO\n")
    else:
        print("\nA MAQUINA VENCEU\n")

    print("=====PLACAR FINAL=====\nEU = ",eu,"\nPC = ",pc,"\n")
    continuar = input("Deseja continuar? = ").upper()
    if continuar == "N":
        print("\nOBRIGADO POR JOGAR\n")
        break
    else:
        eu = 0
        pc = 0



