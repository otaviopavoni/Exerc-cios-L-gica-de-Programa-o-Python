# Exercício para treinar For / While

# Ex.: 01: Exiba os números de 1 a 10 usando um loop while
'''numero = 1
while numero <= 10:
    print(numero)
    numero += 1'''

# Ex.: 02: Crie um simulador de tabuada, onde o jogador digita um número e a tabuada desse número será mostrada.
def calcular():
    global tabuada 
    global resposta
    tabuada = int(input("Qual tabuada você deseja calcular? "))
    print(f"A tabuada do {tabuada} é:")
    for t in range (1, 11):
        print(f"{tabuada} x {t} = {tabuada * t}")

    resposta = input("\nVocê quer calcular alguma outra tabuada? sim/não: ")
    while resposta == "sim":
        calcular()

calcular()
print("Obrigado por usar o programa! Bons cálculos.")

# Ex.: 03: Escreva um programa que conta quantas vogais existem na string que o usuário digita
'''frase = input("Digite uma frase: ")
quantidade_vogais = 0
vogais = ["a", "e", "i", "o", "u"]

for i in frase:
    if i in vogais:
        quantidade_vogais += 1

print("O seu texto tem " + str(quantidade_vogais) + " vogais.")'''

# Ex.: 04: Escreva um programa onde o sistema exibe uma tabuada de 1 a 100.
'''for i in range(1, 101):
    for e in range(1,101):
        print (f"{i} x {e} = {i * e}")'''