import os

os.system ("cls||clear")


soma_notas = float
contador = float


while True:
    
    nota = float(input("Digite uma nota: "))
    soma_notas = 0
    contador = 1  
    
    
    resposta = input("Deseja inserir mais uma nota? (S para sim, N para não): ")


    if contador == 0:
     soma = nota
     contador = 1
    
   
    if resposta == 'N':
        media = soma_notas / contador  
        print(f"A média aritmética das {contador} notas informadas é: {media:.2f}")
        break  
