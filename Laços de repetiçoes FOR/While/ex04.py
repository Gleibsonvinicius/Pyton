
import os

os.system ("cls||clear")



nota1 = float(input("Digite a primeira nota (0 a 10): "))
while nota1 < 0 or nota1 > 10:
    print("Nota inválida! A nota deve estar entre 0 e 10.")
    nota1 = float(input("Digite a primeira nota (0 a 10): "))

nota2 = float(input("Digite a segunda nota (0 a 10): "))
while nota2 < 0 or nota2 > 10:
    print("Nota inválida! A nota deve estar entre 0 e 10.")
    nota2 = float(input("Digite a segunda nota (0 a 10): "))

nota3 = float(input("Digite a terceira nota (0 a 10): "))
while nota3 < 0 or nota3 > 10:
    print("Nota inválida! A nota deve estar entre 0 e 10.")
    nota3 = float(input("Digite a terceira nota (0 a 10): "))


media = (nota1 + nota2 + nota3) / 3


if media >= 7:
    status = "Aprovado"
elif 5 <= media < 7:
    status = "Recuperação"
else:
    status = "Reprovado"


print(f"A média do aluno é: {media:.2f}")
print(f"O aluno está: {status}")
