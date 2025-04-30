import os
from dataclasses import dataclass

os.system ("cls||clear")

@dataclass

class Paciente:
    # Atributos: são variáveis que pertencem à classe.
    nome: str
    idade: int

    # Método: é uma função que pertence à classe.
    # Este método exibe os dados do Paciente.
    def exibir_dados(self):
        print(f"Nome: {self.nome} \nIdade: {self.idade} \n \n")


#criando uma lista.

lista_de_pacientes = []
Quantidade_Pacientes = 2


#atribuindo dados dos pacientes

for i in range (Quantidade_Pacientes):
    paciente1 = Paciente(
nome = input("Digite seu Nome: "),
idade = int(input("Digite sua idade: "))
)
    lista_de_pacientes.append(Paciente)



# Atribuindo dados ao paciente1.
paciente1 = Paciente(
nome = input("Digite seu Nome: "),
idade = int(input("Digite sua idade: "))
)
# Exibindo dados do Paciente.

print("\n == Exibindo dados do usuario ==")
for paciente in lista_de_pacientes:
  paciente1.exibir_dados
