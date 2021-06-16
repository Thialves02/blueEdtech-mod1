frase = input("Digite uma frase : ")

for i in frase:
    if i == "a" or i == "e"or i == "i"or i == "o"or i == "u":
        print(frase.replace("a","").replace("e","").replace("i","").replace("o","").replace("u",""))
        break