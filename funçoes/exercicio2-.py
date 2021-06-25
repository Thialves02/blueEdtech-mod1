def argumento(num):
    if num>0:
        print("P") 
    elif num<0:
        print("N")
    elif num == 0:
        print("0")

num = int(input("Digite um número = "))
argumento(num)