import os

os.system("clear")



# Solicitar ao usuário o número do mês
numero_mes = int(input("Digite um número de 1 a 12 para o mês: "))

# Usando match-case para identificar o mês
match numero_mes:
    case 1:
        print("Janeiro")
    case 2:
        print("Fevereiro")
    case 3:
        print("Março")
    case 4:
        print("Abril")
    case 5:
        print("Maio")
    case 6:
        print("Junho")
    case 7:
        print("Julho")
    case 8:
        print("Agosto")
    case 9:
        print("Setembro")
    case 10:
        print("Outubro")
    case 11:
        print("Novembro")
    case 12:
        print("Dezembro")
    case _:
        print("Mês Invalido selecione o mês que voce deseja!!!")
      

  
 
