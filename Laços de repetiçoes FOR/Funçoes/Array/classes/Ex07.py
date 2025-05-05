import os
from dataclasses import dataclass

os.system ("cls||clear")

@dataclass

class nome:
    nome = str
    nascimento = float
    Rg = float
    Cpf = float


usuarios = []

def pedir_dados(usuarios):
    print("Digite os dados do usuário:")
    nome = input("Nome: ")
    nascimento = input("Data de nascimento : ")
    rg = input("RG: ")
    cpf = input("CPF: ")
    usuarios.append([nome, nascimento, rg, cpf])


def mostrar_dados(usuarios):
    print("== Dados dos usuários ==")
    print("Usuário:",)
    print(" Nome:", )
    print(" Data de nascimento:", )
    print(" RG:", )
    print(" CPF:", )
    


for i in range(5):
    pedir_dados(usuarios)

mostrar_dados(usuarios)

nome_arquivo = "Funcionarios.txt"  # Definindo a variável nome_arquivo

try:
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha:
                usuarios.append(linha)
except FileNotFoundError:
    print("Erro ao ler arquivo:")
