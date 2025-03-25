import os

os.system ("cls||clear")



quantidade_pares = 0
quantidade_impares = 0
soma_pares = 0
soma_geral = 0
quantidade_total = 0

while True:

    numero = int(input("Digite um número inteiro positivo (0 para encerrar): "))
    

    if numero == 0:
        break
    

    quantidade_total += 1
    soma_geral += numero
    

    if numero % 2 == 0:
        quantidade_pares += 1
        soma_pares += numero
    else:
        quantidade_impares += 1


if quantidade_pares > 0:
    media_pares = soma_pares / quantidade_pares
else:
    media_pares = 0

if quantidade_total > 0:
    media_geral = soma_geral / quantidade_total
else:
    media_geral = 0


print(f"Quantidade de números pares: {quantidade_pares}")
print(f"Quantidade de números ímpares: {quantidade_impares}")
print(f"Média dos valores pares: {media_pares:.2f}")
print(f"Média geral dos números lidos: {media_geral:.2f}")
