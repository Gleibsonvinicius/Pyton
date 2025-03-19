import os

os.system ("cls||clear")



nota = -1


while nota < 0 or nota > 10:

    nota = float(input("Por favor, informe a nota do aluno (0 a 10): "))
    

    if nota < 0 or nota > 10:
        print("Nota inválida! A nota deve estar entre 0 e 10.")

   





print(f"A nota informada foi: {nota}")




