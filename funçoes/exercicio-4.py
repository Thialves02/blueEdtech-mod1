def xyz(horas,salario_horas):

    salario = horas * salario_horas
    
    if horas>40:
        salario_extra = ((horas-40) * salario_horas)*1.5
        salario_final = salario + salario_extra
        return(f'Você trabalhou mais que 40 horas semanais então seu salario foi R${salario_final}')

    return(f'Você trabalhou menos que 40 horas semanais então seu salario foi R${salario}')
    
horas = int(input("Digite quantas horas trabalhou = "))
salario_hora = int(input("Digite quanto ganha por hora = "))

print(xyz(horas,salario_hora))