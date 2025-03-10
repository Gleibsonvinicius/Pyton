import os

os.system("clear")

# Entrada de dados
nome_aluno = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Cálculo da média
media = (nota1 + nota2) / 2

# Determinação do conceito
match media:
    case media if media >= 9:
        conceito = 'A'
    case media if media >= 7:
        conceito = 'B'
    case media if media >= 5:
        conceito = 'C'
    case media if media >= 4:
        conceito = 'D'
    case _:
        conceito = 'E'

# Exibição do resultado
print(f"Nome do Aluno: {nome_aluno}")
print(f"Média: {media:.2f}")
print(f"Conceito: {conceito}")

# Mensagem de aprovação ou reprovação
match conceito:
    case 'A' | 'B' | 'C':
        print("Status: Aprovado")
    case 'D' | 'E':
        print("Status: Reprovado")