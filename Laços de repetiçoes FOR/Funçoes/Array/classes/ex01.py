import os
from dataclasses import dataclass

os.system ("cls||clear")

@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float


pessoa1 = Pessoa("Marta", 33, 55.33, 1.69)

print("Solicitando dados")

nome = input("Digite seu Nome: ")
idade = int(input("Digite sua idade: "))  
peso = float(input("Digite seu peso: "))  
altura = float(input("Digite sua altura: "))  


pessoa1 = Pessoa(nome=nome, idade=idade, peso=peso, altura=altura)


pessoa2 = Pessoa(nome=nome, idade=idade, peso=peso, altura=altura)

print("\nExibindo dados:")

print(f"Nome: {pessoa1.nome}, Idade: {pessoa1.idade}, Peso: {pessoa1.peso}, Altura: {pessoa1.altura}")


print(f"Nome: {pessoa2.nome}, Idade: {pessoa2.idade}, Peso: {pessoa2.peso}, Altura: {pessoa2.altura}")