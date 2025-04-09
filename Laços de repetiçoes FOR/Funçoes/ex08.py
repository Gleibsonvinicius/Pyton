import os


os.system("cls||clear")

soma = 0 

def calcular (soma):
    return soma/2

for i in range (2):
    nota = float(input("Digite a sua nota : "))
    soma += nota

media = calcular (soma)
print(f" a sua Media é : {media}")