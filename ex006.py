# Exercícios de condicionais (if/else)
'''Fazer um programa para ler as duas notas que um aluno obteve no primeiro e segundo semestres de
uma disciplina anual. Em seguida, mostrar a nota final que o aluno obteve (com uma casa decimal) no
ano juntamente com um texto explicativo. Caso a nota final do aluno seja inferior a 60.00, mostrar a
mensagem "REPROVADO", conforme exemplos. '''

'''nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

nota_final = nota1 + nota2

print(f"Sua nota final foi {nota_final}.")
if nota_final < 60:
    print("REPROVADO!")'''

# Fazer um programa para ler os três coeficientes de uma equação do segundo grau. Usando a fórmula
'''de Baskara, calcular e mostrar os valores das raízes x1 e x2 da equação com quatro casas decimais,
conforme exemplo. Se a equação não possuir raízes reais, mostrar uma mensagem. '''

'''import math
from operator import neg

a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

delta = (b * b) - (4 * a * c)

if delta < 0 or a == 0:
    print("Esse número não possui raízes reais.")
else:
    x1 = (neg(b) + math.sqrt(delta)) / (2 * a)
    x2 = (neg(b) - math.sqrt(delta)) / (2 * a)

    print(f"x1 = {x1:.4f}")
    print(f"x2 = {x2:.4f}")'''

# Problema "menor_de_tres"
'''Fazer um programa para ler três números inteiros. Em seguida, mostrar qual o menor dentre os três
números lidos. Em caso de empate, mostrar apenas uma vez. '''

'''numero1 = int(input("Primeiro valor: "))
numero2 = int(input("Segundo valor: "))
numero3 = int(input("Terceiro valor: "))

if numero1 <= numero2 and numero1 <= numero3:
    print("Menor número: " + str(numero1))
elif numero2 <= numero1 and numero2 <= numero3:
    print("Menor número: " + str(numero2))
elif numero3 <= numero1 and numero3 <= numero2:
    print("Menor número: " + str(numero3))'''

# Problema "operadora"
'''Uma operadora de telefonia cobra R$ 50.00 por um plano básico que dá direito a 100 minutos de
telefone. Cada minuto que exceder a franquia de 100 minutos custa R$ 2.00. Fazer um programa para
ler a quantidade de minutos que uma pessoa consumiu, daí mostrar o valor a ser pago. '''

'''minutos = int(input('Digite a quantidade de minutos: '))
preco = 50
if minutos > 100:
    preco = 50 + ((minutos - 100) * 2)
else:
    print(f"O total a pagar é R${preco}")'''

# Problema "troco_verificado"
'''Fazer um programa para calcular o troco no processo de pagamento de um produto de uma mercearia.
O programa deve ler o preço unitário do produto, a quantidade de unidades compradas deste produto,
e o valor em dinheiro dado pelo cliente. Seu programa deve mostrar o valor do troco a ser devolvido
ao cliente. Se o dinheiro dado pelo cliente não for suficiente, mostrar uma mensagem informando o
valor restante conforme exemplo. '''

'''preco_produto = float(input("Preço unitário do produto: "))
quantidade_comprada = float(input("Quantidade comprada: "))
dinheiro_recebido = float(input("Dinheiro recebido: "))

if dinheiro_recebido < quantidade_comprada * preco_produto:
    print(f"Dinheiro insuficiente para compra! Faltam R${((quantidade_comprada * preco_produto) - dinheiro_recebido):.2f}")
else:
    troco = dinheiro_recebido - (quantidade_comprada * preco_produto)
    print(f"O troco é de R${troco:.2f}")'''

# Problema "glicose"
'''Fazer um programa para ler a quantidade de glicose
no sangue de uma pessoa e depois mostrar na tela a
classificação desta glicose de acordo com a tabela de
referência ao lado. '''

'''glicose = float(input("Digite a medida da glicose: "))

if glicose < 100:
    print("Classificação: normal")
elif 140 >= glicose > 100:
    print("Classificação: elevado")
elif glicose > 140:
    print("Classificação: diabetes")'''

# Problema "dardo"
'''No arremesso de dardo, o atleta tem três chances para lançar o dardo à maior distância que conseguir.
Você deve criar um programa para, dadas as medidas das três tentativas de lançamento, informar qual
foi a maior. '''

'''primeira_distancia = float(input("Digite a primeira distância: "))
segunda_distancia = float(input("Digite a segunda distância: "))
terceira_distancia = float(input("Digite a terceiria distância: "))

if primeira_distancia >= segunda_distancia and primeira_distancia >= terceira_distancia:
    print(f"Maior distância: {primeira_distancia}")
elif segunda_distancia >= primeira_distancia and segunda_distancia >= terceira_distancia:
    print(f"Maior distância: {segunda_distancia}")
elif terceira_distancia >= primeira_distancia and terceira_distancia >= segunda_distancia:
    print(f"Maior distância: {terceira_distancia}")'''

# Problema "temperatura"
'''Deseja-se converter uma medida de temperatura da escala Celsius para Fahrenheit ou vice-versa. Para
isso, você deve construir um programa que leia a letra "C" ou "F" indicando em qual escala vai ser
informada uma temperatura. Em seguida o programa deve mostrar a temperatura na outra escala com 
duas casas decimais. A seguir é dada a fórmula para converter de Fahrenheit para Celsius (você deve
deduzir a fórmula de Celsius para Fahrenheit): ( 32)'''

'''temperatura = str(input("Você vai digitar a temperatura em qual escala (C/F)? "))
if temperatura == "F":
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: ")) 
    celsius = 5/9 * (fahrenheit - 32)
    print(f"Temperatura equivalente em Celsius: {celsius:.2f}°C")
elif temperatura == "C":
    celsius = float(input("Digite a temperatura em Celsius: ")) 
    fahrenheit = 9/5 * celsius + 32
    print(f"Temperatura equivalente em Fahrenheit: {fahrenheit:.2f}°F")'''

# Problema "lanchonete" (adaptado de URI 1038)
'''Uma lanchonete possui vários produtos. Cada produto possui um código
e um preço. Você deve fazer um programa para ler o código e a
quantidade comprada de um produto (suponha um código válido), e daí
informar qual o valor a ser pago, com duas casas decimais, conforme
tabela de produtos ao lado. '''

'''codigo = int(input("Código do produto comprado: "))
quantidade = float(input("Quantidade comprada: "))

if codigo == 1:
    preco = 5
    preco_final = preco * quantidade
    print(f"O total a pagar é R${preco_final:.2f}.")
elif codigo == 2:
    preco = 3.50
    preco_final = preco * quantidade
    print(f"O total a pagar é R${preco_final:.2f}.")
elif codigo == 3:
    preco = 4.80
    preco_final = preco * quantidade
    print(f"O total a pagar é R${preco_final:.2f}.")
elif codigo == 4:
    preco = 8.90
    preco_final = preco * quantidade
    print(f"O total a pagar é R${preco_final:.2f}.")
elif codigo == 5:
    preco = 7.32
    preco_final = preco * quantidade
    print(f"O total a pagar é R${preco_final:.2f}.")'''

# Problema "multiplos" (adaptado de URI 1044)
'''Fazer um programa para ler dois números inteiros, e dizer se um número é múltiplo do outro. Os
números podem ser digitados em qualquer ordem. '''

'''numero1 = int(input("Digite um número inteiro: "))
numero2 = int(input("Digite outro número inteiro: "))

if numero1 % numero2 == 0 or numero2 % numero1 == 0:
    print("São múltiplos.")
elif numero1 % numero2 != 0:
    print("Não são múltiplos.")'''

# Problema "aumento" (adaptado de URI 1048)
'''Uma empresa vai conceder um aumento percentual de
salário aos seus funcionários dependendo de quanto
cada pessoa ganha, conforme tabela ao lado. Fazer um
programa para ler o salário de uma pessoa, daí mostrar
qual o novo salário desta pessoa depois do aumento,
quanto foi o aumento e qual foi a porcentagem de
aumento. '''

'''salario = float(input("Digite o salário da pessoa: "))
if salario < 1000:
    aumento = 1.20
    novo_salario = salario * aumento
    print(f"Novo salário: R${novo_salario:.2f}")
    print(f"Aumento: R${novo_salario - salario:.2f}")
    print("Porcentagem: 20%")
elif 3000 >= salario > 1000:
    aumento = 1.15
    novo_salario = salario * aumento
    print(f"Novo salário: R${novo_salario:.2f}")
    print(f"Aumento: R${novo_salario - salario:.2f}")
    print("Porcentagem: 15%")
elif 8000 >= salario > 3000:
    aumento = 1.10
    novo_salario = salario * aumento
    print(f"Novo salário: R${novo_salario:.2f}")
    print(f"Aumento: R${novo_salario - salario:.2f}")
    print("Porcentagem: 10%")
elif salario > 8000:
    aumento = 1.05
    novo_salario = salario * aumento
    print(f"Novo salário: R${novo_salario:.2f}")
    print(f"Aumento: R${novo_salario - salario:.2f}")
    print("Porcentagem: 5%")'''

# Problema "tempo_de_jogo" (adaptado de URI 1046)
'''Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo
pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24
horas. '''

'''hora_inicial = int(input("Hora inicial: "))
hora_final = int(input("Hora final: "))

if hora_inicial > hora_final:
    hora = (24 - hora_inicial) + hora_final
elif hora_final > hora_inicial:
    hora = hora_final - hora_inicial

print(f"O jogo durou {hora} horas.")'''

# Problema "coordenadas" (adaptado de URI 1041)
'''Leia os valores das coordenadas X e Y de um ponto no plano
cartesiano. A seguir, determine qual o quadrante ao qual pertence o
ponto (Q1, Q2, Q3 ou Q4). Se o ponto estiver na origem, escreva a
mensagem “Origem”. Se o ponto estiver sobre um dos eixos escreva
“Eixo X” ou “Eixo Y”, conforme for a situação. '''

'''x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))

if x == 0 and y == 0:
    print("Origem.")
elif x == 0:
    print("Eixo Y.")
elif y == 0:
    print("Eixo X.")

if x > 0 and y > 0:
    print("Q1")
elif x < 0 and y < 0:
    print("Q2")
elif x > 0 and y < 0:
    print("Q4")
elif x < 0 and y < 0:
    print("Q3")'''