import os

os.system("cls||clear")

def massa_corporal(altura, peso):
   
    resultado = peso / (altura ** 2)  
    return resultado


altura = float(input("Qual a sua Altura ? "))

peso = float(input("Qual seu Peso ?"))

resultado_media = massa_corporal(altura, peso)

print(f"O seu IMC é {resultado_media:.2f}")
