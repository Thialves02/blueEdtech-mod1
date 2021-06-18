import random

l = []
c = []


num_jogos = 0
jogos = int(input("Quantos jogos serão gerados?\nJogos gerados = "))

while num_jogos<jogos:
    count = 0
    while True:
        rand = random.randint(1,60)
        if rand not in l:
            l.append(rand)
            count += 1
        if count == 6:
            break
    c.append(l[:])
    l.clear()
    num_jogos += 1
print(c)



        

