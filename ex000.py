#esse é o primeiro programa que faço após anos que não vejo nada relacionado com programação. foi um pouco difícil mas estou orgulhoso do resultado.

# a função "jogar" ira gerar sempre um novo número aleatório caso o usuário deseje jogar novamente
# 1 > criar variável random_number e armazenar o número aleatório / 2 > criar variável user_number com o pedido do usuário para digitar um número aleatório / 3 > enquanto o user_number for diferente de random_number, executar um "enquanto user_number > ou < random_number, alertar e pedir novamente" / 4 > quando o usuario acertar, perguntar se ele quer jogar novamente, se quiser, repetir jogar(). se não, encerrar o programa.

from random import randint

def jogar():
	global answer
	random_number = randint(0,100)
	#print("O número aleatório é " + str(random_number))
	user_number = input("Digite um número: ")

	
	while int(user_number) != random_number:
		while int(user_number) > random_number:
			user_number = input("Digite um número menor que " + str(user_number) + ": ")
		while int(user_number) < random_number:
			user_number = input("Digite um número maior que " + str(user_number) + ": ")			
	
	print("Parabéns! Você acertou o número.")		
	
	answer = input("\nDeseja jogar novamente? sim ou não: ")
	while str(answer) == "sim":
		jogar()
	
print("Seja bem-vindo ao jogo: acerte o número! \n\nNesse jogo a máquina irá pensar em um número aleatório de 0 a 100 e você deverá acertar via tentariva e erro. \nA cada tentativa o programa irá informar se o número digitado é maior ou menor do que o número escolhido. \n\nVocê pode jogar quantas vezes quiser. Aproveite!\n")

jogar()
print("Obrigado por jogar!")