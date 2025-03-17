import os

os.system ("cls||clear")


contagem_pares = 0
contagem_impares = 0


for i in range(5):
    
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
 
    if numero % 2 == 0:
        contagem_pares += 1
    else:
        contagem_impares += 1


print(f"Números pares: {contagem_pares}")
print(f"Números ímpares: {contagem_impares}")