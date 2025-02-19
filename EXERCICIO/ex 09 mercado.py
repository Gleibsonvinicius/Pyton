import os

os.system("clear")


#Elabore um algoritmo para resolver a seguinte questão: 



#As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. 



#Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.



# Ler a quantidade de maçãs compradas
quantidade_macas = int(input("Digite o número de maçãs compradas: "))

# Verificar o preço unitário com base na quantidade comprada
if quantidade_macas < 12:
    preco_unitario = 1.30
else:
    preco_unitario = 1.00

# Calcular o custo total
custo_total = quantidade_macas * preco_unitario

# Exibir o custo total da compra
print(f"O custo total da compra é R$ {custo_total:.2f}")
