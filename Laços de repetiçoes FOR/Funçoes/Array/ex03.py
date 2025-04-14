import os

os.system ("cls||clear")




listas_numero = []
QUANTIDADE_NUMEROS = 6

def pares_impares(lista):
    pares = 0
    impares = 0

    for numero in lista: 
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

    return pares, impares
 
for _ in range(QUANTIDADE_NUMEROS):
    numero = int(input("Digite um número: "))
    listas_numero.append(numero)

pares, impares = pares_impares(listas_numero)
print(f"Números pares: {pares}, Números ímpares: {impares}")