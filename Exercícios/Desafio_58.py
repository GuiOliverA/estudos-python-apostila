#Melhore o jogo do DESAFIO 028 onde o computador vai “pensar” em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

computador = randint(0, 10)
print('--=--' * 15)
print('Vou pensar em um número entre 0 e 10 e você deverá tentar adivinhá-lo.')
print('--=--' * 15)
num_jogador = int(input('Em qual número você acha que eu pensei?\n> '))
print('Pensando...')

sleep(1)

palpites = 1
while num_jogador != computador: #Se for True executa abaixo, se for False vai pular para baixo
   print(f'Resposta ERRADA. Você escolheu {num_jogador}\nTente novamente')
   if num_jogador < computador:
            print(f'DICA: Tente um número maior que {num_jogador}...')
   else:
            print(f'DICA: Tente um número menor que {num_jogador}...')
   num_jogador = int(input('Em qual número você acha que eu pensei?\n> '))
   palpites += 1

print('-=-' * 15)
print(f'Meus parabéns, você ACERTOU. Você {num_jogador} e eu escolhi {computador} também!\nTotal de tentativas: {palpites}')
print('-=-' * 15)