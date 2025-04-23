import os

os.system ("cls||clear")

import os

os.system("cls||clear")

vetor = [0] * 5 

for i in range(5):
    vetor[i] = float(input(f"Digite o {i+1}º número: "))

quantidade_negativos = 0
soma_positivos = 0

for numero in vetor:
    if numero < 0:
        quantidade_negativos += 1
    elif numero > 0:
        soma_positivos += numero

print(f"Quantidade de números negativos: {quantidade_negativos}")
print(f"Soma dos números positivos: {soma_positivos}")
