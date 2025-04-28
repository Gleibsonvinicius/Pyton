import os
from dataclasses import dataclass

os.system ("cls||clear")


@dataclass
class Pessoa:
    nome: str
    email: int
    telefone: float
    endereco: float


pessoa1 = Pessoa("Marta", "marta@example.com", "123456789", "Rua A, 123")

print("Solicitando dados")


nome = input("Digite seu Nome: ")
email = input("Digite seu email: ")
telefone = input("Digite seu telefone: ")
endereco = input("Digite seu endereço: ")


pessoa1 = Pessoa(nome=nome, email=email, telefone=telefone, endereco=endereco)


print("\nExibindo dados:")
print(f"Nome: {pessoa1.nome}, Email: {pessoa1.email}, Telefone: {pessoa1.telefone}, Endereço: {pessoa1.endereco}")
