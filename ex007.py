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

# Exemplo de for: Fazer um programa que lê um valor inteiro N e depois N números inteiros.
'''Ao final, mostra a soma dos N números lidos.'''

'''soma = 0
valor = 0

vezes = int(input("Quantos números serão digitados? "))
for i in range(0, vezes):
    valor = int(input("Digite um número: "))
    soma += valor

print(f"SOMA = {soma}")'''

# Tabuada
'''tabuada = int(input("Deseja saber a tabuada de qual valor? "))
for i in range(1, 11):
    print(f"{tabuada} x {i} = {tabuada * i}")'''

# Problema "soma_impares" 
'''Leia 2 valores inteiros X e Y (em qualquer ordem). A seguir, calcule e mostre a soma dos números
impares entre eles. '''

'''x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))
soma_impar = 0
troca = 0

if x > y:
    troca = x
    x = y      # Garantir que x e y estejam sempre na ordem crescente.
    y = troca

if x < 0:
    x += 1
elif y < 0: # O professor escreveu em Portugol a mesma coisa que eu e deu resultado diferente
    y -= 1 # Fiz essa "gambiarra" para consertar e dar todos os resultados iguais em Python

for i in range(x, y):
    if i % 2 != 0:
        soma_impar += i
print(f"SOMA DOS ÍMPARES: {soma_impar}")'''

# Problema "validacao_de_nota"
'''Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e imprima a
média semestral. Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao
intervalo [0,10]). Cada nota deve ser validada separadamente. '''

'''nota1 = float(input("Digite a primeira nota: "))
while nota1 < 0 or nota1 > 10:
    nota1 = float(input("Valor inválido! Tente novamente: "))

nota2 = float(input("Digite a segunda nota: "))
while nota2 < 0 or nota2 > 10:
    nota2 = float(input("Valor inválido! Tente novamente: "))
media = (nota1 + nota2) / 2
print(f"MÉDIA = {media}")'''

# Problema "quadrante"
'''Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no
sistema cartesiano. Para cada ponto escrever o quadrante a que ele pertence (Q1, Q2, Q3 ou Q4). O
algoritmo será encerrado quando pelo menos uma de duas coordenadas for NULA (nesta situação sem
escrever mensagem alguma). '''

'''x = int(input("Digite o valor da coordenada X: "))
y = int(input("Digite o valor da coordenada Y: "))

while x != 0 and y != 0:
    while x > 0 and y > 0:
        print("Quadrante Q1")
        x = int(input("Digite o valor da coordenada X: "))
        y = int(input("Digite o valor da coordenada Y: "))
    while x < 0 and y > 0:
        print("Quadrante Q2")
        x = int(input("Digite o valor da coordenada X: "))
        y = int(input("Digite o valor da coordenada Y: "))
    while x < 0 and y < 0:
        print("Quadrante Q3")
        x = int(input("Digite o valor da coordenada X: "))
        y = int(input("Digite o valor da coordenada Y: "))
    while x > 0 and y < 0:
        print("Quadrante Q4")
        x = int(input("Digite o valor da coordenada X: "))
        y = int(input("Digite o valor da coordenada Y: "))'''

# Problema "combustivel"
'''Um posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes.
Escreva um algoritmo para ler o tipo de combustível abastecido (codificado da seguinte forma:
1.Álcool 2.Gasolina 3.Diesel 4.Fim). Caso o usuário informe um código inválido (fora da faixa de 1 a
4) deve ser solicitado um novo código (até que seja válido). O programa será encerrado quando o
código informado for o número 4, devendo então mostrar a mensagem "MUITO OBRIGADO", bem
como as quantidades de cada combustível. '''

'''codigo = 0

alcool = 0
gasolina = 0
diesel = 0

while codigo != 4:
    codigo = int(input("Informe um código (1, 2, 3) ou 4 para parar: "))
    if codigo == 1:
        alcool += 1
    elif codigo == 2:
        gasolina += 1
    elif codigo == 3:
        diesel += 1

print(f"Muito obrigado!\nAlcool: {alcool}\nGasolina: {gasolina}\nDiesel: {diesel}")'''

# Problema "pares_consecutivos"
'''O programa deve ler um valor inteiro X indefinidas vezes. (O programa irá parar quando o valor de X
for igual a 0). Para cada X lido, imprima a soma dos 5 pares consecutivos a partir de X, inclusive o X
, se for par. Se o valor de entrada for 4, por exemplo, a saída deve ser 40, que é o resultado da operação:
4+6+8+10+12, enquanto que se o valor de entrada for 11, por exempo, a saída deve ser 80, que é a
soma de 12+14+16+18+20. '''

# Esse deu trabalho!!

'''soma = 0
quantidade = 0
x = int(input("Digite o valor de x: "))

while x != 0:
    if x % 2 == 0: # se for par
        soma = 0
        quantidade = 0
        while quantidade < 5:
            soma += x
            x += 2
            quantidade += 1
        print(f"SOMA = {soma}")
    if x % 2 != 0: # se for ímpar
        soma = 0
        quantidade = 0
        x += 1
        while quantidade < 5:
            soma += x
            x += 2
            quantidade += 1
        print(f"SOMA = {soma}")
    x = int(input("Digite o valor de x: "))'''

# Problema "sequencia_impares"
'''Leia um valor inteiro X. Em seguida mostre os ímpares de 1 até X, um valor por linha, inclusive o X,
se for o caso. '''

'''x = int(input("Digite o valor de X: "))
for i in range(0, x):
    if i % 2 != 0:
        print(i)'''

# Problema "dentro_fora"
'''Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo,
conforme exemplo '''

'''numero = 0
fora = 0
dentro = 0

quantidade = int(input("Quantos números você vai digitar? "))
for i in range(0, quantidade):
    numero = int(input("Digite um número: "))
    if numero < 10 or numero > 20:
        fora += 1
    else:
        dentro += 1
print(f"{dentro} DENTRO\n{fora} FORA")'''

# Problema "par_impar" 
'''Leia um valor inteiro N. Este valor será a quantidade de números inteiros que serão lidos em seguida.
Para cada valor lido, mostre uma mensagem dizendo se este valor lido é PAR ou IMPAR, e também
se é POSITIVO ou NEGATIVO. No caso do valor ser igual a zero (0), seu programa deverá imprimir
apenas NULO. '''

'''numero = 0

quantidade = int(input("Quantos números você vai digitar? "))
for i in range(0, quantidade):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0 and numero > 0:
        print("PAR POSITIVO")
    elif numero % 2 == 0 and numero < 0:
        print("PAR NEGATIVO")
    elif numero % 2 != 0 and numero > 0:
        print("ÍMPAR POSITIVO")    
    elif numero % 2 != 0 and numero < 0:
        print("ÍMPAR NEGATIVO")
    elif numero == 0:
        print("NULO")'''

# Problema "media_ponderada"
'''Leia um valor inteiro N, que representa o número de casos de teste que vem a seguir. Cada caso de
teste consiste de 3 valores reais, para os quais você deverá calcular e mostrar a média ponderada, sendo
que o primeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro valor tem peso 5. Vale lembrar
que a média ponderada é a soma de todos os valores multiplicados pelo seu respectivo peso, dividida
pela soma dos pesos. '''

'''v1 = 0
v2 = 0
v3 = 0

p1 = 2
p2 = 3
p3 = 5

media = 0

quantidade = int(input("Quantos casos você vai digitar? "))
for i in range(0, quantidade):
    v1 = float(input("Digite o primeiro número: "))
    v2 = float(input("Digite o segundo número: "))
    v3 = float(input("Digite o terceiro número: "))
    media = ((v1 * p1) + (v2 * p2) + (v3 * p3)) / (p1 + p2 + p3)
    print(f"MÉDIA = {media:.2f}")'''

# Problema "divisão"
'''Escreva um algoritmo que leia dois números e imprima o resultado da divisão do primeiro pelo
segundo. Caso não for possível, mostre a mensagem “DIVISAO IMPOSSIVEL”. '''

'''numerador = 0
denominador = 0
divisao = 0

quantidade = int(input("Quantos casos você vai digitar? "))
for i in range(0, quantidade):
    numerador = int(input("Entre com o numerador: "))
    denominador = int(input("Entre com o denominador: "))
    if denominador == 0:
        print("Divisão impossível.")
    else:
        divisao = numerador / denominador
        print(f"Divisão = {divisao}")'''

# Problema "fatorial"
'''Fazer um programa para ler um número natural N (valor máximo: 15), e depois calcular e mostrar o
fatorial de N. '''

'''total = 1
numero = int(input("Digite o valor de N: "))
if numero <= 15:
    for i in range(1, numero+1):
        
        total *= i
        
    print(f"Fatorial: {total}")
else:
    print("Quantidade máxima ultrapassada.")'''

# Problema "experiencias"
'''Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para
organizar os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano,
quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada. Este
laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas
informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia
utilizada e a quantidade de cobaias utilizadas em cada experimento. Faça um programa que leia um
valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso de teste contém um
inteiro que representa a quantidade de cobaias utilizadas e uma letra ('C', 'R' ou 'S'), indicando o tipo
de cobaia (R:Rato S:Sapo C:Coelho). Apresente o total de cobaias utilizadas, o total de cada tipo de
cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o
percentual deve ser apresentado com dois dígitos após o ponto. '''

'''quantidade_cobaias = 0
tipo_de_cobaia = ""

coelho = 0
rato = 0
sapo = 0

total_cobaias = 0

vezes = int(input("Quantos casos de teste serão digitados? "))
for i in range(0, vezes):
    quantidade_cobaias = int(input("Quantidade de cobaias: "))
    total_cobaias += quantidade_cobaias
    tipo_de_cobaia = input("Tipo de cobaia: ")
    if tipo_de_cobaia == "C":
        coelho += quantidade_cobaias
    elif tipo_de_cobaia == "R":
        rato += quantidade_cobaias
    elif tipo_de_cobaia == "S":
        sapo += quantidade_cobaias

total_animais = coelho + rato + sapo

percentual_coelho = (coelho / total_animais) * 100
percentual_rato = (rato / total_animais) * 100
percentual_sapo = (sapo / total_animais) * 100

print(f"RELATÓRIO FINAL: \nTotal: {total_cobaias} cobaias\nTotal de coelhos: {coelho}\nTotal de ratos: {rato}\nTotal de sapos {sapo}")
print(f"Percentual de coelhos: {percentual_coelho:.2f}\nPercentual de ratos: {percentual_rato:.2f}\nPercentual de sapos: {percentual_sapo:.2f}")
'''