
import os

os.system ("cls||clear")




# Exibição do cardápio
print("Bem-vindo ao Restaurante! Aqui está o nosso cardápio:")
print("1 - Picanha - R$ 25,00")
print("2 - Lasanha - R$ 20,00")
print("3 - Strogonoff - R$ 18,00")
print("4 - Bife Acebolado - R$ 15,00")
print("5 - Pao com ovo - R$ 5,00")

# Inicialização das variáveis
pratos_escolhidos = []
total = 0.00

# Loop para escolha dos pratos
while True:
    # Solicitar ao usuário para escolher o prato
    opcao = int(input("Escolha o número do prato desejado: "))
    
    if opcao == 1:
        pratos_escolhidos.append(("Picanha", 25.00))
        total += 20.00
    elif opcao == 2:
        pratos_escolhidos.append(("Prato B", 25.00))
        total += 25.00
    elif opcao == 3:
        pratos_escolhidos.append(("Prato C", 30.00))
        total += 30.00
    elif opcao == 4:
        pratos_escolhidos.append(("Prato D", 35.00))
        total += 35.00
    elif opcao == 5:
        pratos_escolhidos.append(("Prato E", 40.00))
        total += 40.00
    else:
        print("Opção inválida! Tente novamente.")
        continue

    # Perguntar se o usuário deseja escolher outro prato
    continuar = input("Deseja escolher outro prato? (s/n): ").strip().lower()
    if continuar != 's':
        break

# Exibição do resumo do pedido
print("\nResumo do seu pedido:")
for prato, valor in pratos_escolhidos:
    print(f"{prato}: R$ {valor:.2f}")

print(f"\nTotal sem gorjeta: R$ {total:.2f}")

# Perguntar sobre a gorjeta
gorjeta = 0.10 * total
pagar_gorjeta = input("\nDeseja pagar uma gorjeta de 10%? (s/n): ").strip().lower()

# Calcular e exibir o valor final a ser pago
if pagar_gorjeta == 's':
    print(f"Gorjeta (10%): R$ {gorjeta:.2f}")
    total_com_gorjeta = total + gorjeta
else:
    total_com_gorjeta = total

print(f"\nTotal a pagar: R$ {total_com_gorjeta:.2f}")
