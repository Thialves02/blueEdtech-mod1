print("BEM VINDO A VOTAÇÂO")
print("CANDITATOS DISPONIVEIS\n[1] José\n[2] João\n[3] Maria\n[4] Pedro\n[5] Nulo\n[6] Branco")
print("")

v1 = 0
v2 = 0
v3 = 0
v4 = 0
v5 = 0
v6 = 0

candidato = int(input("Digite o númerom do seu candidato = "))
voto = input("Deseja votar novamente [S/N]? = ").upper()
if candidato == 1:
    v1+=1
if candidato == 2:
    v2+=1
if candidato == 3:
    v3+=1
if candidato == 4:
    v2+=1
while voto == "S":
    print("")
    print("BEM VINDO A VOTAÇÂO")
    print("CANDITATOS DISPONIVEIS\n[1] José\n[2] João\n[3] Maria\n[4] Pedro\n[5] Nulo\n[6] Branco")
    print("")
    candidato = int(input("Digite o númerom do seu candidato = "))
    voto = input("Deseja votar novamente [S/N]? = ").upper()
    if candidato == 1:
        v1+=1
    if candidato == 2:
        v2+=1
    if candidato == 3:
        v3+=1
    if candidato == 4:
        v4+=1
    if candidato == 5:
        v5+=1
    if candidato == 6:
        v6+=1
    total = v1 + v2 +v3 + v4 + v5 + v6
    porc5 = v5 * 100/total
    porc6 = v6 * 100/total
print("O candidato [1] José recebeu",v1,"votos")
print("O candidato [2] João recebeu",v2,"votos")
print("A candidata [3] Maria recebeu",v3,"votos")
print("O candidato [4] Pedro recebeu",v4,"votos")
print("[5] Nulo recebeu",v5,"votos")
print("[6] Branco recebeu",v6,"votos")
print(f'{porc5:.2f}% dos votos foram nulos')
print(f'{porc6:.2f}% dos votos foram em branco')
