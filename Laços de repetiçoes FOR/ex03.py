import os

os.system ("cls||clear")




soma = 0

# Loop para solicitar 5 números inteiros
for i in range(5):
  
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
   
    soma += numero


print(f"A soma dos números lidos é: {soma}")