import os


os.system("cls||clear")



def metros_para_centimetros(metros):
   
    centimetros = metros * 100
    
    return centimetros


valor_metros = int(input("Digite um valor em metros: "))


valor_centimetros = metros_para_centimetros(valor_metros)

print(f"{valor_metros} metros é igual a {valor_centimetros} centímetros.")