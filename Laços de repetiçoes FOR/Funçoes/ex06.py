import os

os.system("cls||clear")

def calcular_preco_inflacionado(preco):
   
    if preco < 100:
        return preco * 1.10  #inflaciona  10%
    else:
        return preco * 1.20  #inflaciona 20%

def descontar (preco):
  
    if preco < 100:
        return preco * 0.1 #desconta   10%
    else:
        return preco * 0.2  #desconta 20%

preco_original = float(input("Digite o preço do produto: "))

preco_final = calcular_preco_inflacionado(preco_original)
preco_descontado = descontar(preco_original)

print(f"O preço inflacionado é: R$ {preco_final:.2f}")
print(f"O preço com desconto é: R$ {preco_descontado:.2f}")

