frase = input("Digite sua frase\n")
vogal = "aeiou"
totalVogal = 0

for i in frase:
    if i in vogal:
        totalVogal +=1
        
print("As vogais aparecem ",totalVogal,"vezes")