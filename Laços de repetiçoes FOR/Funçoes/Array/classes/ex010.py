import os
from dataclasses import dataclass

os.system ("cls||clear")

@dataclass


class Endereco:
    logradouro: str
    numero: int
    cidade: str
    estado: str

    def cadastrar_endereco(self):
        self.logradouro = input("Logradouro: ")
        self.numero = int(input("Número: "))
        self.cidade = input("Cidade: ")
        self.estado = input("Estado: ")
        return self

    def visualizar_endereco(self):
        print("\n--- Endereço ---")
        print(f"Logradouro: {self.logradouro}, {self.numero}")
        print(f"Cidade: {self.cidade} - {self.estado}")

    def atualizar_endereco(self):
        print("\n--- Atualizar Endereço ---")
        self.logradouro = input(f"Novo Logradouro ({self.logradouro}): ") or self.logradouro
        novo_numero = input(f"Novo Número ({self.numero}): ")
        self.numero = int(novo_numero) if novo_numero else self.numero
        self.cidade = input(f"Nova Cidade ({self.cidade}): ") or self.cidade
        self.estado = input(f"Novo Estado ({self.estado}): ") or self.estado
        return self

class Aluno:
    nome: str
    data_nascimento: int
    cpf: str
    ra: str
    curso: str
    endereco: Endereco

    def cadastrar(self):
        self.nome = input("Nome do aluno: ")
        data = input("Data de Nascimento : ")
        self.data_nascimento = int(data)
        self.cpf = input("CPF: ")
        self.ra = input("Registro Acadêmico (R.A.): ")
        self.curso = input("Curso: ")
        print("\n--- Endereço ---")
        self.endereco = Endereco().cadastrar_endereco()
        print("Aluno cadastrado com sucesso!")

    def visualizar(self):
        print("\n--- Dados do Aluno ---")
        print(f"Nome: {self.nome}")
        print(f"Data de Nascimento: {self.data_nascimento}")
        print(f"CPF: {self.cpf}")
        print(f"R.A.: {self.ra}")
        print(f"Curso: {self.curso}")
        self.endereco.visualizar_endereco()

    def atualizar(self):
        print("\n--- Atualizar Dados do Aluno ---")
        self.nome = input(f"Novo Nome ({self.nome}): ") or self.nome
        nova_data = input(f"Nova Data de Nascimento (ddmmaaaa) ({self.data_nascimento}): ")
        self.data_nascimento = int(nova_data) if nova_data else self.data_nascimento
        self.cpf = input(f"Novo CPF ({self.cpf}): ") or self.cpf
        self.ra = input(f"Novo R.A. ({self.ra}): ") or self.ra
        self.curso = input(f"Novo Curso ({self.curso}): ") or self.curso
        print("\n--- Atualizar Endereço ---")
        self.endereco.atualizar_endereco()
        print("Dados do aluno atualizados com sucesso!")

class SistemaAlunos:
    alunos: list = []

    def exibir_menu(self):
        print("\n--- Menu Sistema de Alunos ---")
        print("1. Cadastrar Aluno")
        print("2. Visualizar Aluno")
        print("3. Atualizar Aluno")
        print("4. Excluir Aluno")
        print("5. Listar Todos os Alunos")
        print("0. Sair")

    def cadastrar_aluno(self):
        aluno = Aluno()
        aluno.cadastrar()
        self.alunos.append(aluno)

    def visualizar_aluno(self):
        if not self.alunos:
            print("Nenhum aluno cadastrado.")
            return
        ra_busca = input("Digite o R.A. do aluno que deseja visualizar: ")
        aluno_encontrado = self.buscar_aluno(ra_busca)
        if aluno_encontrado:
            aluno_encontrado.visualizar()
        else:
            print("Aluno não encontrado.")

    def atualizar_aluno(self):
        if not self.alunos:
            print("Nenhum aluno cadastrado.")
            return
        ra_busca = input("Digite o R.A. do aluno que deseja atualizar: ")
        aluno_encontrado = self.buscar_aluno(ra_busca)
        if aluno_encontrado:
            aluno_encontrado.atualizar()
        else:
            print("Aluno não encontrado.")

    def excluir_aluno(self):
        if not self.alunos:
            print("Nenhum aluno cadastrado.")
            return
        ra_excluir = input("Digite o R.A. do aluno que deseja excluir: ")
        aluno_encontrado = self.buscar_aluno(ra_excluir)
        if aluno_encontrado:
            self.alunos.remove(aluno_encontrado)
            print("Aluno excluído com sucesso!")
        else:
            print("Aluno não encontrado.")

    def listar_todos_alunos(self):
        if not self.alunos:
            print("Nenhum aluno cadastrado.")
            return
        print("\n--- Lista de Todos os Alunos ---")
        for aluno in self.alunos:
            print(f"Nome: {aluno.nome}, R.A.: {aluno.ra}")

    def buscar_aluno(self, ra):
        for aluno in self.alunos:
            if aluno.ra == ra:
                return aluno


sistema = SistemaAlunos()


sistema.exibir_menu()
opcao = input("Escolha uma opção: ")

if opcao == '1':
    sistema.cadastrar_aluno()
elif opcao == '2':
    sistema.visualizar_aluno()
elif opcao == '3':
    sistema.atualizar_aluno()
elif opcao == '4':
    sistema.excluir_aluno()
elif opcao == '5':
    sistema.listar_todos_alunos()
elif opcao == '0':
    print("Saindo do sistema.")
else:
    print("Opção inválida.")

