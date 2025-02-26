import os

os.system("clear")


dia = input("Digite o dia da semana ")

match dia :
    case "segunda":
        print("Hoje é Segunda feira")
    case "Terça":
        print("Hoje é Terça feira")
    case "Quarta":
        print("Hoje é quarta feira")
    case "Quinta":
        print("Hoje é Quinta feira")
    case "Sexta":
        print("Hoje é Sexta feira")
    case "Sabado" | "domingo":
        print("Hoje é Fim de semana")
    case _:
        print("Dia invalido")

print(dia)

print("======FIM======")


