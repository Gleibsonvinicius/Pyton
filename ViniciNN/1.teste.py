import os

os.system("clear")



def main():
    
    nome = input("Digite o nome do jogador: ")
    jogos = int(input("Digite o número de jogos que o jogador fez: "))
    gols = int(input("Digite o número de gols que o jogador marcou: "))
    assistencias = int(input("Digite o número de assistências que o jogador deu: "))

    
    participacoes_gols = gols + assistencias

    
    print("\n--- Informações do Jogador ---")
    print(f"Nome: {nome}")
    print(f"Número de Jogos: {jogos}")
    print(f"Número de Gols: {gols}")
    print(f"Número de Assistências: {assistencias}")
    print(f"Participações em Gols: {participacoes_gols}")

if __name__ == "__main__":
    main()