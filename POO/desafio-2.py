dic = []

class Jogador():
    def __init__(self,nome,partidas):
        self.nome = nome
        self.partidas = partidas

    def calculo(self,dic):
        gols =[]
        for i in range(self.partidas):
            gol = int(input("Quantos jogos fez nessa partida? = "))
            gols.append(gol)
            dic[self.nome] = [(sum(gols)//games) , sum(gols)]
        return print(f'O jogador {self.nome}, fez uma media de {dic[self.nome][0]}, gols por partida, com um total de {dic[self.nome][1]} gols')

jogos = {}
condition = ''
while condition != 'NAO':
    name = str(input("Qual o nome do jogador? = "))
    games = int(input("Quantas partidas jogou? = "))
    jogador = Jogador(name,games)
    jogador.calculo(jogos)
    condition = str(input('Deseja adicionar outro jogador = ')).upper().replace('Ã','A').strip()