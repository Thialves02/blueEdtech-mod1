def somaimposto(custo,imposto):
    imposto_porcentagem = imposto/custo*100
    return f'O preço do produto é {custo} e o valor em % do imposto é de {imposto_porcentagem}%'


custo = float(input("Qual o custo do produto? = "))
imposto = float(input("Qual o imposto do produto = "))

print(somaimposto(custo,imposto))