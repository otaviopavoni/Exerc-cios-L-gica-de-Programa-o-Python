# Contagem regressiva:
# Crie um programa que faça uma contagem regressiva de x até 0 usando um loop while.

import time

numero = int(input("Digite o número que você queira fazer a contagem regressiva: "))
numero += 1
for i in range(1, numero):
    print(f"Estamos no número {i}, faltam {numero - i - 1} números!")
    time.sleep(1)