#lê os números inteiros A e B 
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))

#verifica se A é divisível por B
if a % b == 0:
    print("A é divisível por B")
else:
    print("A não é divisível por B")
