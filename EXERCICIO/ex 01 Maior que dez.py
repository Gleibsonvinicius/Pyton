import os

os.system("clear")



#Elabore um algoritimo para solicitar ao usuario um valor e escrever a mensagem : é maior que 10! , se o valor lido for maior que 10 , caso contrario escrever: Nao é maior que 10!

# Solicita um valor ao usuário
valor = float(input("Digite um valor: "))

# Verifica se o valor é maior que 10
if valor > 10:
    print("É maior que 10!")
else:
    print("Não é maior que 10!")
