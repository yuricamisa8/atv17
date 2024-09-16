# Crie um programa que receba um ano e verifique se ele é bissexto. Um ano é bissexto se for divisível por 4, exceto se for divisível por 100 e não por 400.

ano = int(input("digt ano"))
if ano %400==0:
    print("BISSEXTO")
elif ano %100==0:
    print("não e bissexto")
elif ano %4==0:
    print("bissexto")
else:
    print("não e bissexto")