# Contagem regressiva:
# Crie um programa que faça uma contagem regressiva de x até 0 usando um loop while.

import time

numero = int(input("Digite o número que você queira fazer a contagem regressiva: "))
for i in range(numero, 0, -1):
    print(f"Estamos no número {i}, faltam {i - 1} números!")
    time.sleep(1)