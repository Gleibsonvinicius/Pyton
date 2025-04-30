import os
from dataclasses import dataclass

os.system ("cls||clear")

@dataclass

class Pessoa:
    # Atributos: são variáveis que pertencem à classe.
    nome: str
    idade: int
    peso: float
    altura: float

    def exibir_dados(self):
        print(f"Nome: {self.nome} \nIdade: {self.idade} \nPeso: {self.peso} \nAltura: {self.altura} \n")


# criando uma lista.
lista_de_pessoas = []
Quantidade_Pessoas = 2

# atribuindo dados dos pacientes
for i in range(Quantidade_Pessoas):
    pessoa = Pessoa (
        nome = input("Digite seu Nome: "),
    idade = int(input("Digite sua idade: ")),
    peso = float(input("Digite a sua altura: ")), 
   altura =   float(input("Digite o seu Peso: ")), 
    )
    
    lista_de_pessoas.append(pessoa)  

    # Exibindo os dados da pessoa cadastrada imediatamente
    pessoa.exibir_dados()  



    #salvando em um arquivo com .TXT
    nome_arquivo = "Dados_da_Pessoa.txt"
    with open (nome_arquivo,"w") as  arquivo_pacientes:
        arquivo_pacientes.write(f"{pessoa.nome}, {pessoa.idade}\n")  
        print("=Dados Salvos com Sucesso.=")