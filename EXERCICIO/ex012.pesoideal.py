import os

os.system("clear")

# Entrada de dados
altura = float(input("Digite sua altura em metros: "))
sexo = input("Digite seu sexo (M para Masculino, F para Feminino): ")

# Cálculo do peso ideal
match sexo:
    case 'M':
        peso_ideal = (72.7 * altura) - 58
    case 'F':
        peso_ideal = (62.1 * altura) - 44.7
    case _:
        peso_ideal = None  # Caso o sexo não seja reconhecido

# Exibição do resultado
if peso_ideal is not None:
    print(f"O peso ideal para uma altura de {altura}m e sexo '{sexo}' é: {peso_ideal:.2f} kg")
else:
    print("Sexo inválido. Por favor, insira 'M' ou 'F'.")



    