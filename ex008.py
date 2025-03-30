# Exercícios de vetores

# Problema Exemplo de Vetores
'''Fazer um programa para ler um número inteiro positivo N (máximo = 10), depois ler N números quaisquer e armazena-los num vetor. Em seguida, mostrar na tela todos os elementos do vetor.'''

'''vezes = int(input("Quantos números você vai digitar? "))
while vezes > 10:
    vezes = int(input("Digite um número menor que 10: "))
vetor = []
for i in range(0, vezes):
    numero = float(input("Digite um número: "))
    vetor.append(numero)

print(f"Números digitados: {vetor}")'''

# Problema "negativos"
'''Faça um programa que leia um número inteiro positivo N (máximo = 10) e depois N números inteiros
e armazene-os em um vetor. Em seguida, mostrar na tela todos os números negativos lidos. '''

'''vetor = []
vezes = int(input("Quantos números você vai digitar? "))

while vezes > 10:
    vezes = int(input("Digite um número menor que 10: "))

for i in range(0, vezes):
    numero = int(input("Digite um número inteiro: "))
    if numero < 0:
        vetor.append(numero)

print(f"Os números negativos que você digitou são: {vetor}")'''

# Problema "soma_vetor" 
'''Faça um programa que leia N números reais e armazene-os em um vetor. Em seguida:
- Imprimir todos os elementos do vetor
- Mostrar na tela a soma e a média dos elementos do vetor '''

'''vetor = []
soma = 0
media = 0
vezes = int(input("Quantos números você vai digitar? "))
for i in range(0, vezes):
    numero = float(input("Digite um número: "))
    soma += numero
    vetor.append(numero)
media = soma / vezes
print(f"VALORES: {vetor}\nSOMA: {soma}\nMÉDIA: {media}")'''

# Problema "alturas" 
'''Fazer um programa para ler nome, idade e altura de N pessoas, conforme exemplo. Depois, mostrar na
tela a altura média das pessoas, e mostrar também a porcentagem de pessoas com menos de 16 anos,
bem como os nomes dessas pessoas caso houver. '''

'''nomes = []
idades = []
idade_total = 0
alturas = []
altura_soma = 0
menor_16 = 0
menor_16_array = []

vezes = int(input("Quantas pessoas serão digitadas? "))
for i in range(0, vezes):
    print(f"Dados da {i+1}a pessoa:")
    
    nome = input("Nome: ")
    nomes.append(nome)
    
    idade = int(input("Idade: "))
    idades.append(idade)
    idade_total += 1

    if idade < 16:
        menor_16 += 1
        menor_16_array.append(nome)
    
    altura = float(input("Altura: "))
    alturas.append(altura)
    altura_soma += altura

altura_media = altura_soma / vezes
porcentagem_16 = (menor_16 / idade_total) * 100 # percentual = (parte / total) * 100
print(f"\nAltura média: {altura_media:.2f}\nPessoas com menos de 16 anos: {porcentagem_16}% = {menor_16_array}")'''

# Problema "numeros_pares" 
'''Faça um programa que leia N números inteiros e armazene-os em um vetor. Em seguida, mostre na
tela todos os números pares, e também a quantidade de números pares. '''

'''array_pares = []
quantidade_pares = 0

vezes = int(input("Digite quantos números você vai digitar: "))
for i in range(0, vezes):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        array_pares.append(numero)
        quantidade_pares += 1
print(f"Números pares: {array_pares}\nQuantidade de pares: {quantidade_pares}")'''

# Problema "maior_posicao" 
'''Faça um programa que leia N números reais e armazene-os em um vetor. Em seguida, mostrar na tela
o maior número do vetor (supor não haver empates). Mostrar também a posição do maior elemento,
considerando a primeira posição como 0 (zero). '''

# Precisei de ajuda nesse! o.O

'''numeros = []
maior_valor = 0
posicao_maior_valor = 0

vezes = int(input("Quantos números você vai digitar? "))

for i in range(0, vezes):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

for i in range(1, len(numeros)):
    if numeros[i] > numeros[i-1]:
        maior_valor = numeros[i]
        posicao_maior_valor = i

print(f"Maior valor: {maior_valor}\nPosição do maior valor: {posicao_maior_valor}")'''

# Problema "soma_vetores" 
'''Faça um programa para ler dois vetores A e B, contendo N elementos cada. Em seguida, gere um
terceiro vetor C onde cada elemento de C é a soma dos elementos correspondentes de A e B. Imprima
o vetor C gerado.'''

'''valores_a = 0
setor_a_array = []
valores_b = 0
setor_b_array = []
vetor_c_array = []

quantos = int(input("Quantos valores vai ter cada vetor? "))
for i in range(0, quantos):
    valores_a = int(input("Digite os valores do vetor A: "))
    setor_a_array.append(valores_a)
    
for i in range(0, quantos):
    valores_b = int(input("Digite os valores do vetor B: "))
    setor_b_array.append(valores_b)

for i in range(0, quantos):
    vetor_c_array.append(setor_a_array[i] + setor_b_array[i])

print(f"Vetor resultante: {vetor_c_array}")'''

# Problema "abaixo_da_media" 
'''Fazer um programa para ler um número inteiro N e depois um vetor de N números reais. Em seguida,
mostrar na tela a média aritmética de todos elementos com três casas decimais. Depois mostrar todos
os elementos do vetor que estejam abaixo da média, com uma casa decimal cada. '''

'''vezes = int(input("Quantos elementos vai ter o vetor? "))
vetor = []
soma = 0
media = 0
vetor_abaixo = []

for i in range(vezes):
    numero = float(input("Digite um número: "))
    soma += numero
    vetor.append(numero)

media = soma / vezes

for i in range(0, len(vetor)):
    if vetor[i] < media:
        vetor_abaixo.append(vetor[i])

print(f"MÉDIA DO VETOR = {media:.3f}")
print(f"ELEMENTOS ABAIXO DA MÉDIA = {vetor_abaixo}")'''

# Problema "media_pares "
'''Fazer um programa para ler um vetor de N números inteiros. Em seguida, mostrar na tela a média
aritmética somente dos números pares lidos, com uma casa decimal. Se nenhum número par for
digitado, mostrar a mensagem "NENHUM NUMERO PAR" '''

'''quantidade_pares = 0
soma_pares = 0

array = []
vezes = int(input("Quantos elementos vai ter o vetor? "))
for i in range(vezes):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        array.append(numero)
        soma_pares += numero
        quantidade_pares += 1

if quantidade_pares > 0:
    print(f"MÉDIA DOS PARES = {soma_pares / quantidade_pares}")
else:
    print("NENHUM NÚMERO PAR.")'''

# Problema "mais_velho" 
'''Fazer um programa para ler um conjunto de nomes de pessoas e suas respectivas idades. Os nomes
devem ser armazenados em um vetor, e as idades em um outro vetor. Depois, mostrar na tela o nome
da pessoa mais velha. '''

'''nomes = []
idades = []

vezes = int(input("Quantas pessoas você vai digitar? "))
for i in range(vezes):
    print(f"Dados da {i+1}a pessoa:")
    nome = input("Nome: ")
    nomes.append(nome)

    idade = int(input("Idade: "))
    idades.append(idade)

pessoa_mais_velha = nomes[0]
idade_mais_velha = idades[0]

for i in range(1, len(idades)):
    if idades[i] > idade_mais_velha:
        pessoa_mais_velha = nomes[i]
        idade_mais_velha = idades[i]

print(f"Pessoa mais velha: {pessoa_mais_velha}\nIdade: {idade_mais_velha}")'''

# Problema "aprovados" 
'''Fazer um programa para ler um conjunto de N nomes de alunos, bem como as notas que eles tiraram
no 1º e 2º semestres. Cada uma dessas informações deve ser armazenada em um vetor. Depois, imprimir
os nomes dos alunos aprovados, considerando aprovados aqueles cuja média das notas seja maior ou
igual a 6.0 (seis). '''

'''nomes = []
primeiras_notas = []
segundas_notas = []

vezes = int(input("Quantos alunos serão digitados? "))
for i in range(vezes):
    nome = input(f"Digite o nome do {i+1}o aluno: ")
    nomes.append(nome)

    primeira_nota = float(input(f"Digite a primeira nota do aluno: "))
    primeiras_notas.append(primeira_nota)

    segunda_nota = float(input(f"Digite a segunda nota do aluno: "))
    segundas_notas.append(segunda_nota)

alunos_aprovados = []

for i in range(len(primeiras_notas)):
    if ((primeiras_notas[i] + segundas_notas[i]) / 2) >= 6:
        alunos_aprovados.append(nomes[i])

print(f"Alunos aprovados: {alunos_aprovados}")'''

# Problema "dados_pessoas" 
'''Tem-se um conjunto de dados contendo a altura e o gênero (M, F) de N pessoas. Fazer um programa
que calcule e escreva a maior e a menor altura do grupo, a média de altura das mulheres, e o número
de homens.'''

'''alturas = []
generos = []

vezes = int(input("Quantas pessoas serão digitadas? "))
for i in range(vezes):
    altura = float(input(f"Altura da {i+1}a pessoa: "))
    alturas.append(altura)

    genero = input(f"Gênero da {i+1}a pessoa: ")
    generos.append(genero)

menor_altura = alturas[0]
maior_altura = alturas[0]

for i in range(len(alturas)):
    if alturas[i] < menor_altura:
        menor_altura = alturas[i]
    elif alturas[i] > maior_altura:
        maior_altura = alturas[i]

soma_mulheres = 0
quantidade_mulheres = 0

for i in range(len(generos)):
    if generos[i] == "F":
        soma_mulheres += alturas[i]
        quantidade_mulheres += 1

media_mulheres = soma_mulheres / quantidade_mulheres
numero_homens = vezes - quantidade_mulheres

print(f"Menor altura: {menor_altura}\nMaior altura: {maior_altura}")
print(f"Média das alturas das mulheres: {media_mulheres:.2f}")
print(f"Quantidade de homens: {numero_homens}")'''

# Problema "comerciante"
'''Um comerciante deseja fazer o levantamento do lucro das mercadorias que ele comercializa. Para isto,
mandou digitar um conjunto de N mercadorias, cada uma contendo nome, preço de compra e preço de
venda das mesmas. Fazer um programa que leia tais dados e determine e escreva quantas mercadorias
proporcionaram:
lucro < 10%
10% ≤ lucro ≤ 20%
lucro > 20%
Determine e escreva também o valor total de compra e de venda de todas as mercadorias, assim como
o lucro total. '''

'''nomes = []
preco_compras = []
preco_vendas = []

vezes = int(input("Serão digitados dados de quantos produtos? "))
for i in range(vezes):
    print(f"Produto {i+1}:")
    nome = input("Nome: ")
    nomes.append(nome)

    preco_compra = float(input("Preço de compra: "))
    preco_compras.append(preco_compra)

    preco_venda = float(input("Preço de venda: "))
    preco_vendas.append(preco_venda)

lucros = []

for i in range(len(preco_compras)):
    lucro = preco_vendas[i] - preco_compras[i]
    lucros.append(lucro)

porcentuais = []

for i in range(len(lucros)):
     # percentual = (parte / total) * 100
    porcentuais.append((lucros[i] / preco_compras[i]) * 100)

lucro_abaixo_10 = 0
lucro_entre_10_e_20 = 0
lucro_acima_20 = 0

for i in range(len(lucros)):
    if porcentuais[i] < 10:
        lucro_abaixo_10 += 1
    elif 10 <= porcentuais[i] <= 20:
        lucro_entre_10_e_20 += 1
    elif porcentuais[i] > 20:
        lucro_acima_20 += 1

valor_total_compra = 0
for i in range(len(preco_compras)):
    valor_total_compra += preco_compras[i]

valor_total_venda = 0
for i in range(len(preco_vendas)):
    valor_total_venda += preco_vendas[i]

lucro_total = 0
for i in range(len(lucros)):
    lucro_total += lucros[i]

print("RELATÓRIO:")
print(f"Lucro abaixo de 10%: {lucro_abaixo_10}")
print(f"Lucro entre 10% e 20%: {lucro_entre_10_e_20}")
print(f"Lucro acima de 20%: {lucro_acima_20}")

print(f"Valor total da compra: {valor_total_compra:.2f}")
print(f"Valor total da venda: {valor_total_venda:.2f}")
print(f"Lucro total: {lucro_total:.2f}")'''