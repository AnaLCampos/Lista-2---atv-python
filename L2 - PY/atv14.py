identificacao = int(input("Digite o número de identificação do aluno: "))
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))
me = float(input("Digite a média dos exercícios do aluno: "))

ma = (nota1 + nota2*2 + nota3*3 + me) / 7

if ma >= 9:
    conceito = "A"
    status = "APROVADO"
elif ma >= 7.5:
    conceito = "B"
    status = "APROVADO"
elif ma >= 6:
    conceito = "C"
    status = "APROVADO"
elif ma >= 4:
    conceito = "D"
    status = "REPROVADO"
else:
    conceito = "E"
    status = "REPROVADO"

print("O aluno de número", identificacao, "obteve média de aproveitamento", ma, "e conceito", conceito + ".")
print("O aluno está", status + ".")
