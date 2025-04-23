import os

os.system ("cls||clear")




vetor = []


for i in range(5):
    valor = float(input(f"Digite o {i+1}º número: "))
    
    
    if valor < 0:
        valor = 0
    
   
    vetor.append(valor)

print("\nValores no vetor:")
for valor in vetor:
    print(valor)
