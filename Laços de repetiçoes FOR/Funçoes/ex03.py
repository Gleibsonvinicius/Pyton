import os


os.system("cls||clear")

def positivo_negativo(numero):
    if numero == 0:
        print(f"O número {numero} é neutro.")
    elif numero > 0:
        print(f"O número {numero} é positivo.")
    else:  
        print(f"O número {numero} é negativo.")

numero = int(input("Digite um número: "))
positivo_negativo(numero)