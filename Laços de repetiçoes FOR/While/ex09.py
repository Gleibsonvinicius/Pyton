import os

os.system ("cls||clear")






total_salario = 0
maior_idade = 0
menor_idade = 0
quantidade_mulheres = 0
contador = 0

while True:
   
    
    print("Menu:")
    print("1 - Adicionar pessoa")
    print("2 - Exibir resultados")
    print("3 - Sair")
    
  
    opcao = int(input("Escolha uma opção: "))
    
    match opcao:
        case 1:
         
            idade = int(input("Digite a idade: "))
            sexo = input("Digite o sexo (M/F): ")
            salario = float(input("Digite o salário: "))
            
            
            total_salario += salario
            contador += 1
            
            if idade > maior_idade:
                maior_idade = idade
            if idade < menor_idade:
                menor_idade = idade
            
            if sexo == 'F' and salario >= 5000:
                quantidade_mulheres += 1
        
        case 2:
           
            if contador == 0:
                print("Nenhuma pessoa cadastrada.")
            else:
                media_salario = total_salario / contador
                print(f"Média de salário do grupo: R$ {media_salario:.2f}")
                print(f"Maior idade do grupo: {maior_idade}")
                print(f"Menor idade do grupo: {menor_idade}")
                print(f"Quantidade de mulheres com salário a partir de R$ 5.000,00: {quantidade_mulheres}")
        
        case 3:
            print("Saindo do programa...")
            break
        
        case _:
            print("Opção inválida. Tente novamente.")
    
    input("Pressione Enter para continuar...")
