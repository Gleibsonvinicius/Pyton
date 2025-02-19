import os

os.system("clear")




# Elabore um algoritmo usando operações lógicas para informar se uma pessoa é obrigada a votar.



#Considere que a regra é que menores de 18 e maiores que 65 não são obrigados a votar.


# Solicita ao usuário a idade
idade = int(input("Digite sua idade: "))

# Verifica se a pessoa é obrigada a votar
if idade >= 18 and idade <= 65:
    print("Você é obrigado a votar.")
else:
    print("Você não é obrigado a votar.")
