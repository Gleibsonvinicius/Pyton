import os

os.system("cls||clear")

def verificar_par_impar(numero):
    if numero % 2 == 0:
        print(f"O número {numero} é Par.")
    else:
        print(f"O número {numero} é Impar.")


numero_usuario = int(input("Digite um número: "))
verificar_par_impar(numero_usuario)
