# Fazer um programa para ler uma duração de tempo em segundos, daí imprimir na tela esta duração no formato horas:minutos:segundos. 
# Esse exercício encontrei em um curso de Lógica de Programação que estou fazendo e, diferente dos outros do mesmo módulo, é peculiarmente mais desafiador. Por isso estou trazendo pra cá.

segundos = int(input("Por favor, digite os segundos: "))
resto = segundos % 3600

horas = segundos // 3600
minutos = resto // 60
segundos = segundos % 60

print(f"{horas}:{minutos}:{segundos}")