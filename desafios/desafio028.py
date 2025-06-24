from random import randint 
from time import sleep
num_computador = randint (0, 5) #Faz o computador sortear o número
print('-=-' * 30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 30)
jogador = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(3)
if jogador == num_computador:
    print('Parabéns, você conseguiu me vencer.')
else:
    print(f'GANHEI! Eu pensei no número {num_computador} e não no {jogador}')

