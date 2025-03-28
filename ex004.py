# Número Primo: Crie um programa que verifique se um número informado pelo usuário é primo.
# Receber número do usuário
# Verificar se ele é somente divisível por 1 e ele mesmo

# Esse precisei de ajuda!

numero = int(input("Digite um número: "))
primo = True

for i in range(2, numero):
    if numero % i == 0: # Verifica se, em um range de 2 ao numero - 1, tem alguma divisão que o resto dá 0. Se der, primo = False.
        primo = False
        break

if primo == False:
    print(f"O número {numero} é composto.")
else:
    print(f"O número {numero} é primo.")