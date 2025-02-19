import os

os.system("clear")





#Elabore um algoritmo para solicitar dois números e ao final mostre na tela:A média, a soma, o produto, o menor valor e o maior valor.Usando uma linha para cada resultado.



# Solicita os dois números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Calcula os resultados
media = (num1 + num2) / 2
soma = num1 + num2
produto = num1 * num2
menor = min(num1, num2)
maior = max(num1, num2)

# Exibe os resultados
print(f"Média: {media}")
print(f"Soma: {soma}")
print(f"Produto: {produto}")
print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
