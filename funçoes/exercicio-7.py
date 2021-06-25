def dois(x,y):
    if x>y:
        return f'O número {y} é o menor'
    elif x<y:
        return f'O número {x} é o menor'
    elif x == y:
        return f'Os números são iguais'

primeiro = int(input("Digite o primeiro número = "))
segundo = int(input("Digite o segundo número = "))

print(dois(primeiro,segundo))