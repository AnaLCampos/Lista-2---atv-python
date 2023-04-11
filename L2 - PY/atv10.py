Ano = int(input("Digite o ano: "))

if Ano % 400 == 0:
    print("O ano é bissexto")
elif Ano % 100 == 0:
    print("O ano não é bissexto")
elif Ano % 4 == 0:
    print("O ano é bissexto")
else:
    print("O ano não é bissexto")
