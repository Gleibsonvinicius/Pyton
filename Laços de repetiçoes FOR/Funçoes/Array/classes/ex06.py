import os
from dataclasses import dataclass

os.system ("cls||clear")

@dataclass

class Nome:
    nome: str
    autor: str
    categoria: str
    preco: float

    def exibir_dados(self):
        print(f"Nome: {self.nome}, Autor: {self.autor}, Categoria: {self.categoria}, Preço: {self.preco}")


lista_de_nomes = []
lista_de_autor = []
lista_de_categoria = []
lista_de_preco = []


quantidade = int(input("Quantos Itens deseja adicionar: "))

for i in range(quantidade):
    nome = Nome(
    nome = input(" = Digite seu Nome: = "),
    autor = input("= Digite seu autor preferido: = "),
    categoria = input(" = Digite a sua categoria favorita: = "),
    preco = float(input(" = Digite o preço: =  ")),

    )
    
    lista_de_nomes.append(nome)
    nome.exibir_dados()
