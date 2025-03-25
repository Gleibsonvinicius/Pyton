import os

os.system ("cls||clear")



soma = 0
contador = 0


while True:
  
    valor = int(input("Digite um valor positivo (ou um valor negativo para encerrar): "))
    
    if valor < 0:
        break
      
    soma += valor
    contador += 1

if contador > 0:
  
    media = soma / contador
    print(f"A média aritmética dos números informados é: {media:.2f}")
else:
    print("Nenhum valor válido foi inserido.")
