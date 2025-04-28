import os
from dataclasses import dataclass

os.system ("cls||clear")


class Endereco:
    def formatar_endereco(logradouro, numero, cidade):
        return f"{logradouro}, {numero} - {cidade}"


class Usuario:
    def formatar_usuario(nome, email, endereco):
        return {
            "nome": nome,
            "email": email,
            "endereco": endereco
        }



def coletar_dados_usuario():
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    
    logradouro = str("Digite o logradouro: ")
    numero = str("Digite o número: ")
    cidade = str("Digite a cidade: ")
    
    endereco = Endereco.formatar_endereco(logradouro, numero, cidade)
    usuario = Usuario.formatar_usuario(nome, email, endereco)
    
    return usuario



usuario = coletar_dados_usuario()
print("\nDados do Usuário:")
print(f"Nome: {usuario['nome']}")
print(f"Email: {usuario['email']}")
print(f"Endereço: {usuario['endereco']}")