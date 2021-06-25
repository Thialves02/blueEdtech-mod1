def IMC(peso,altura):
    imc = peso/altura**2.
    return f'Seu IMC é {imc:.2f}'

peso = int(input("Digite seu peso = "))
altura = float(input("Digite sua altura = ")).replace(',','.')

print(IMC(peso,altura))