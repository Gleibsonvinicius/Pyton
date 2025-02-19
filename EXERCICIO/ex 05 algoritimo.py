import os

os.system("clear")

# Elabore um algoritmo para receber dois inteiros como entrada do
#teclado e escreva na tela: 

	

#A média, a soma, o produto, o menor valor e o maior valor.



#Além disso, verifique se os números informados pelo usuário são iguais.



#Usando uma linha para cada resultado.




# Receber dois inteiros como entrada do teclado
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

# Calcular a média, soma, produto, menor e maior valor
media = (num1 + num2) / 2
soma = num1 + num2
produto = num1 * num2
menor = min(num1, num2)
maior = max(num1, num2)

# Verificar se os números são iguais
if num1 == num2:
    iguais = "Sim"
else:
    iguais = "Não"

# Exibir os resultados
print(f"Média: {media}")
print(f"Soma: {soma}")
print(f"Produto: {produto}")
print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Os números são iguais? {iguais}")
