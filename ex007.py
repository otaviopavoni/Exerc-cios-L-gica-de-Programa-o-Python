# Exercícios de Estrutura "while"

# Problema "crescente" (adaptado de URI 1113)
'''Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Escreva para cada X e Y uma
mensagem que indique se estes valores foram digitados em ordem crescente ou decrescente. O
programa deve finalizar quando forem digitados dois valores iguais. '''

'''numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

while numero1 != numero2:
    while numero1 > numero2:
        print("Decrescente!")
        numero1 = int(input("Digite outro primeiro número: "))
        numero2 = int(input("Digite outro segundo número: "))
    while numero1 < numero2:
        print("Crescente!")
        numero1 = int(input("Digite outro primeiro número: "))
        numero2 = int(input("Digite outro segundo número: "))'''

# Problema "media_idades"
'''Faça um programa para ler um número indeterminado de dados, contendo cada um, a idade de um
indivíduo. O último dado, que não entrará nos cálculos, contém um valor de idade negativa. Calcular
e imprimir a idade média deste grupo de indivíduos. Se for entrado um valor negativo na primeira vez,
mostrar a mensagem "IMPOSSIVEL CALCULAR". '''

'''idade = 0
idade_soma = 0
idade_numero = 0
idade_media = 0

while idade >= 0:
    idade = int(input("Digite as idades: "))
    idade_soma += idade

    if idade_soma < 0:
        print("Impossível calcular")
        break

    idade_numero += 1

    if idade < 0:
        idade_media = (idade_soma-idade) / (idade_numero-1)
        print(f"A média dos números válidos é {idade_media:.2f}")'''

# Problema "senha_fixa" (adaptado de URI 1114)
'''Escreva um programa que repita a leitura de uma senha até que ela seja válida. Para cada leitura de
senha incorreta informada, escrever a mensagem "Senha Invalida! Tente novamente:". Quando a senha
for informada corretamente deve ser impressa a mensagem "Acesso Permitido" e o algoritmo
encerrado. Considere que a senha correta é o valor 2002. '''

'''senha_real = 2002
tentativa_usuario = int(input("Digite a senha: "))
while tentativa_usuario != senha_real:
    tentativa_usuario = int(input("Por favor, tente novamente: "))
print("Acesso concedido!")'''

