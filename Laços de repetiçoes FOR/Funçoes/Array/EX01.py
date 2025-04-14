import os

os.system ("cls||clear")



listas_notas = []
QUANTIDADE_NOTAS = 3  

for i in range(QUANTIDADE_NOTAS):
    nota = float(input("Digite sua nota: "))  
    listas_notas.append(nota)

media = sum(listas_notas) / QUANTIDADE_NOTAS

if media >= 7:
    resultado = "Aprovado"
elif media >= 5:
    resultado = "Recuperaçao"
else:
    resultado = "Reprovado"



print("\nNotas digitadas:")
for nota in listas_notas:
    print(nota)

print(f"Média: {media:.1f}")
print(f"Resultado: {resultado:}")
