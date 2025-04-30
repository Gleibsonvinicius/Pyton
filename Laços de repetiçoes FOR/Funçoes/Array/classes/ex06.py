import os
from dataclasses import dataclass

os.system ("cls||clear")

@dataclass

class nome:
    nome: str
    autor: str
    Categoria: str
    preco:float



def exibir_dados(self):
    print(f"nome:{self.nome} , autor: {self.autor},categoria:{self.categoria},preco:{self.preco}" )



lista_de_nomes = []
Quantidade_de_autor = 2
lista_de_categoria = []
preco = 0


for i in range(lista_de_nomes):
    nome = nome (
        nome = input("Digite seu Nome: "),
    autor = int(input("Digite seu autor preferido: ")),
    Categoria = int (input("Digite a sua categoria Favorita: ")), 
   preco =   float(input("Digite o preco: ")), 
    )


    lista_de_nomes.append(nome)  

   
    nome.exibir_dados()  