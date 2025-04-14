import os

os.system ("cls||clear")



listas_numero = []
QUANTIDADE_NUMEROS = 5

print("= Solicitando Números =")
for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i + 1}º número: "))
    listas_numero.append(numero)

maior = max(listas_numero)
menor = min(listas_numero)

print("\nMostrando números:")

for i, numero in enumerate(listas_numero, start=1):
    print(f"{i}º número: {numero}")

print(f"\nMaior número: {maior}")
print(f"Menor número: {menor}")