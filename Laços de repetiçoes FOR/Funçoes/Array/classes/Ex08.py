import os
from dataclasses import dataclass

os.system("cls||clear")

@dataclass
class Funcionario:
    def cadastrar(self):
        self.nome = input("Nome: ")
        self.data_admissao = input("Data de Admissão : ")
        self.matricula = input("Matrícula: ")
        self.endereco = input("Endereço: ")

class Cliente:
    def cadastrar(self):
        self.nome = input("Nome: ")
        self.data_nascimento = input("Data de Nascimento : ")
        self.endereco = input("Endereço: ")

def coletar_dados_funcionarios():
    funcionarios = []
    cadastrar = []
    for i in range(3):
        print(f"Digite os dados do Funcionário {i + 1}:")
        funcionario = Funcionario()
        cadastrar()
        funcionarios.append(funcionario)
    return funcionarios

def coletar_dados_clientes():
    clientes = []
    cadastrar = []
    for i in range(3):
        print(f"Digite os dados do Cliente {i + 1}:")
        cliente = Cliente()
        cadastrar()
        clientes.append(cliente)
    return clientes

funcionarios = coletar_dados_funcionarios()
clientes = coletar_dados_clientes()

print("Dados dos Funcionários:")
for f in funcionarios:
    print(f"Nome: {f.nome}, Data de Admissão: {f.data_admissao}, Matrícula: {f.matricula}, Endereço: {f.endereco}")

print("\nDados dos Clientes:")
for c in clientes:
    print(f"Nome: {c.nome}, Data de Nascimento: {c.data_nascimento}, Endereço: {c.endereco}")


