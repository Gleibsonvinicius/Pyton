import os

os.system("cls||clear")

def massa_corporal(altura, peso):
    resultado = peso / (altura * altura)  
    return resultado

def classificar_imc(imc):
    if imc >= 40:
        classificacao = "Obesidade grau III"
        recomendacao = "Busque assistência médica"
    elif imc >= 35:
        classificacao = "Obesidade grau II"
        recomendacao = "Consulte um médico para avaliação e orientação"
    elif imc >= 30:
        classificacao = "Obesidade grau I"
        recomendacao = "Procure um profissional da saúde"
    elif imc >= 25:
        classificacao = "Sobrepeso"
        recomendacao = "Considere uma dieta balanceada e pratique atividade física"
    elif imc >= 18.5:
        classificacao = "Peso normal"
        recomendacao = "Mantenha hábitos saudáveis"
    else:
        classificacao = "Abaixo do peso"
        recomendacao = "Consulte um médico para avaliação de sua saúde"
    
    
    return classificacao, recomendacao

altura = float(input("Qual a sua altura: "))
peso = float(input("Qual o seu peso: "))

resultado_media = massa_corporal(altura, peso)
classificacao, recomendacao = classificar_imc(resultado_media)

print(f"O seu IMC é {resultado_media:.2f} e você está classificado como: {classificacao}")
print(f"Recomendação: {recomendacao}")
