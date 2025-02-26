import os

os.system("clear")

# Desenvolva um programa que receba como entrada um numero inteiro que represente um dos 7 dias da semana e imprima na tela se esse dia é util , final de semana ou invalido 

#considere que domingo é o dia 1 e sabado o dia 7.



# Solicitar o número do dia da semana
dia = int(input("Digite o número de um dia da semana (1 a 7): "))

# saida
match dia:
    case 1 | 7:
        print("Final de semana")
    case 2 | 3 | 4 | 5 | 6:
        print("Dia útil")
    case _:
        print("Dia inválido")
