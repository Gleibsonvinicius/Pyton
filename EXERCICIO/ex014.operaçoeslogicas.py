import os

os.system("clear")


# Entrada de dados
codigo = input("Digite a matrícula do empregado: ")
ano_nascimento = int(input("Digite o ano de nascimento do empregado: "))
tempo_trabalho = int(input("Digite o tempo de trabalho em anos: "))

# Cálculo da idade
ano_atual = 2025  
idade = ano_atual - ano_nascimento

# Verificação das condições para aposentadoria
qualificado = (idade >= 65) or (tempo_trabalho >= 30)

# Exibição do resultado
print(f"Código do Empregado: {codigo}")
print(f"Idade: {idade} anos")
print(f"Tempo de Trabalho: {tempo_trabalho} anos")

if qualificado:
    print("Mensagem: Requerer aposentadoria")
else:
    print("Mensagem: Não Requerer a aposentadoria")