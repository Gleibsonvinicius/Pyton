import os


os.system("cls||clear")

def notas():
    
    nota1 = float(input("Digite a sua Primeira Nota: "))
    nota2 = float(input("Digite a sua Segunda Nota: "))
    return nota1, nota2

def media():
   
    nota1, nota2 = notas()  
    soma = nota1 + nota2    
    media = soma / 2        
    return media


resultado_media = media()
print(f"A Sua media é : {resultado_media:.1f}")