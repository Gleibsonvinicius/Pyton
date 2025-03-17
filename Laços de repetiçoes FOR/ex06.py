import os

os.system ("cls||clear")



soma_notas = 0


for i in range(3):

    nota = float(input(f"Digite a {i + 1}ª nota: "))
   
    soma_notas += nota


media = soma_notas / 3


print(f"A média das notas é: {media:.2f}")


if media >= 7:
    print("Aluno aprovado.")
elif media >= 4:
    print("Aluno em recuperação.")
else:
    print("Aluno reprovado.")