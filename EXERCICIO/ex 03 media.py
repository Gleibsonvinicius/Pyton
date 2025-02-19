import os

os.system("clear")




#Elabore um algoritmo para solicitar ao usuário três notas. Calcule a média do aluno. Caso a média do aluno seja menor que 7, o aluno está reprovado. Mostrar: média e se está aprovado ou reprovado.




# Solicitar as três notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcular a média
media = (nota1 + nota2 + nota3) / 3

# Verificar se o aluno está aprovado ou reprovado
if media >= 7:
    status = " Parabens Voce foi Aprovado que alegria"
else:
    status = " Que Tristeza infelizmente  Voce Reprovado"

# Exibir a média e o status
print(f"A média do aluno é: {media:.2f}")
print(f"Status: {status}")
