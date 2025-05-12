import os
from dataclasses import dataclass

os.system ("cls||clear")

@dataclass

class Funcionario:
    def criar(self, nome, data_nascimento, cpf, funcao):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.funcao = funcao

def adicionar_funcionario(funcionarios):
    print("\nAdicionar novo funcionário:")
    nome = input("Nome: ")
    data_nascimento = input("Data de Nascimento: ")
    cpf = input("CPF: ")
    funcao = input("Função: ")

    for f in funcionarios:
        if f.cpf == cpf:
            print("Erro: CPF já cadastrado!\n")
            return

    funcionario = Funcionario()
    funcionario.criar(nome, data_nascimento, cpf, funcao)
    funcionarios.append(funcionario)
    print("Funcionário adicionado com sucesso!\n")

def listar_funcionarios(funcionarios):
    if len(funcionarios) == 0:
        print("\nNenhum funcionário cadastrado.\n")
        return
    print("\nLista de funcionários:")
    for i, f in enumerate(funcionarios, 1):
        print(f"Nome: {f.nome}, Data Nascimento: {f.data_nascimento}, CPF: {f.cpf}, Função: {f.funcao}")
    print()

def atualizar_funcionario(funcionarios):
    cpf = input("\nDigite o CPF do funcionário que deseja atualizar: ")
    funcionario_encontrado = None
    for f in funcionarios:
        if f.cpf == cpf:
            funcionario_encontrado = f
            break

    if funcionario_encontrado :
        print("Funcionário não encontrado.\n")
        return

    print("Deixe o campo vazio para não alterar.")
    nome = input(f"Novo nome [{funcionario_encontrado.nome}]: ")
    data_nascimento = input(f"Nova data de nascimento [{funcionario_encontrado.data_nascimento}]: ")
    funcao = input(f"Nova função [{funcionario_encontrado.funcao}]: ")

    if nome != "":
        funcionario_encontrado.nome = nome
    if data_nascimento != "":
        funcionario_encontrado.data_nascimento = data_nascimento
    if funcao != "":
        funcionario_encontrado.funcao = funcao

    print("Funcionário atualizado com sucesso!\n")

def deletar_funcionario(funcionarios):
    cpf = input("\nDigite o CPF do funcionário que deseja deletar: ")
    for i, f in enumerate(funcionarios):
        if f.cpf == cpf:
            del funcionarios[i]
            print("Funcionário deletado com sucesso!\n")
            return
    print("Funcionário não encontrado.\n")

def menu():
    funcionarios = []
    while True:
        print("======= Gerenciamento de Funcionários =======")
        print("1. Adicionar Funcionário")
        print("2. Listar Funcionários")
        print("3. Atualizar Funcionário")
        print("4. Deletar Funcionário")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            adicionar_funcionario(funcionarios)
        elif escolha == '2':
            listar_funcionarios(funcionarios)
        elif escolha == '3':
            atualizar_funcionario(funcionarios)
        elif escolha == '4':
            deletar_funcionario(funcionarios)
        elif escolha == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

menu()
