print("Responda as perguntas com [S/N]")
qntd = 0
p1 = input("Você telefonou para a vítima?\nSua resposta = ").upper()
p2 = input("Você esteve no local do crime?\nSua resposta = ").upper()
p3 = input("Você mora perto da vítima?\nSua resposta = ").upper()
p4 = input("Você devia para a vítima?\nSua resposta = ").upper()
p5 = input("Você já trabalhou com a vítima?\nSua resposta = ").upper()

if p1!="S" and p1!="N" or p2!="S" and p2!="N" or p3!="S" and p3!="N" or p4!="S" and p4!="N" or p5!="S" and p5!="N":
  print("Digite respostas corretas ou suspeitaremos de você!!!")
else:
  if p1 == "S":
    qntd = qntd + 1
  if p2 == "S":
    qntd = qntd + 1
  if p3 == "S":
    qntd = qntd + 1
  if p4 == "S":
    qntd = qntd + 1
  if p5 == "S":
    qntd = qntd + 1

  if qntd == 2:
    print("Você é SUSPEITO")
  elif qntd == 3 or qntd == 4:
    print("Você é CÚMPLICE")
  elif qntd == 5:
    print("Você é o ASSASINO")
  else:
    print("Você é INOCENTE")