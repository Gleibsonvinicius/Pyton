import os

os.system ("cls||clear")


def exibir_tabuada(numero):
 
    print(f"\nTabuada do {numero}:")
   
    for i in range(1, 11):
     
        print(f"{numero} x {i} = {numero * i}")


numero_usuario = int(input("Informe um número para ver sua tabuada: "))
exibir_tabuada(numero_usuario)