class pessoa:
    def __init__(self,nome,sobrenome,idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
    def dados(self):
        print(f'Nome completo : {self.nome} {self.sobrenome}\nIdade : {self.idade}')

thiago = pessoa("Thiago","Roberto",18)
thiago.dados()
