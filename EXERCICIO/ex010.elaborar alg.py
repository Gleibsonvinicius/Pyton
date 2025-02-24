import os

os.system("clear")



# Elabore um algoritimo usando operaçoes logicas para solicitar ao usuario 2 numeros e escrever:

# os 2 numeros informados 
# o maior numero 
# o menor numero
 

# Solicita ao usuário os dois números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Exibe os dois números informados
print(f"Os números informados foram: {numero1} e {numero2}")

# Verifica qual é o maior número
if numero1 > numero2:
    maior = numero1
    menor = numero2
elif numero1 < numero2:
    maior = numero2
    menor = numero1
else:
    maior = menor = numero1  # Caso ambos sejam iguais

# Exibe o maior e o menor número


print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
