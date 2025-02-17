import os

os.system("clear")

def main():
    
    num_alunos = int(input("Digite o número de alunos: "))
    
    
    notas = []

    
    for i in range(num_alunos):
        nota = float(input(f"Digite a nota do aluno {i + 1}: "))
        notas.append(nota)

   
    media = sum(notas) / num_alunos

   
    print(f"\nA média das notas dos alunos é: {media:.2f}")

if __name__ == "__main__":
    main()