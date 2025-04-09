import os
from datetime import date

os.system("cls||clear")

def calcular (idade):
    resultado = 2025 - idade 
    return resultado


ano_nascimento = int(input("Digite o ano de seu  Nascimento :"))

idade = calcular(ano_nascimento)

print(f" a Sua Idade é  : {idade} anos ")

     
