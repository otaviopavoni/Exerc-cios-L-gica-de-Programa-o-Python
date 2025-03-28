# Verificador de número par ou ímpar:
# Peça um número ao usuário e informe se ele é par ou ímpar usando uma condição if.

numero = int(input("Por favor, digite um número: "))
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")