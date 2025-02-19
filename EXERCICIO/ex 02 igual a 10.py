
import os

os.system("clear")


# Solicita um valor ao usuário
valor = float(input("Digite um número: "))

# Verifica o valor digitado
if valor > 10:
    print("É maior que 10!")
elif valor < 10:
    print("Não é maior que 10!")
else:
    print("O número é igual a 10!")
