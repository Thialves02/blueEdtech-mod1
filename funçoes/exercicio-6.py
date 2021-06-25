def func_nota(nota):
    if nota>=9:
        return f'Sua nota foi A'
    elif nota>=8:
        return f'Sua nota foi B'
    elif nota>=7:
        return f'Sua nota foi C'
    elif nota>=6:
        return f'Sua nota foi D'
    elif nota<=4:
        return f'Sua nota foi F'

nota = float(input("Digite sua nota = "))

print(func_nota(nota))