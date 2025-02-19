import os

os.system("clear")






#Elabore um algoritmo usando operações lógicas para ler 2 números e escrever:

 

#Os 2 números informados.
#O maior número;
#O menor número; 





# Ler os dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Exibir os dois números informados
print(f"Os números informados são: {num1} e {num2}")

# Verificar qual é o maior número e qual é o menor
if num1 > num2:
    print(f"O maior número é: {num1}")
    print(f"O menor número é: {num2}")
elif num1 < num2:
    print(f"O maior número é: {num2}")
    print(f"O menor número é: {num1}")
else:
    print("Os dois números são iguais.")
