import os

os.system("clear")




n1 = float(input("== Digite a sua primeira nota!: == "))
os.system("clear")

n2 = float(input("== Digite a sua segunda nota!: == "))
os.system("clear")

media = (n1 + n2) / 2

if media > 6:
    print("Você está de aprovado, boas Ferias")
elif media < 6:
    print("Você está de Recuperaçao , estude mais ")
elif media == 6:
    print("Você está exatamente com a média, continue se esforçando!")

print(f"A sua média foi: {media:.1f}")
