import os

os.system ("cls||clear")




soma = 0


for i in range(5):
    
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
   
    soma += numero

# Exibe a soma total
print(f"A soma dos números lidos é: {soma}")