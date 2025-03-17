import os

os.system ("cls||clear")


import time  


numero = int(input("Informe um número para a contagem regressiva: "))


for i in range(numero, 0, -1):  
    print(i)  
    time.sleep(1)  

print("Contagem regressiva finalizada!")