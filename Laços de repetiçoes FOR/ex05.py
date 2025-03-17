import os

os.system ("cls||clear")



soma_notas = 0


for i in range(4):

    nota = float(input(f"Digite a {i + 1}ª nota: "))

    soma_notas += nota


media = soma_notas / 4


print(f"A média das notas é: {media:.2f}")