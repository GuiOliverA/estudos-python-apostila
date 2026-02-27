#Gerar palpites da Mega Sena. Ele pergunta quantos jogos serão gerados e sorteia 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
print('=-='*10, 'MEGA PYTHON DA VIRADA', '=-='*10)
lista = list()
jogos = list()
quant = int(input('Gerar quantos jogos?\n> '))
total = 1
while total <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('=-='*5 , f'Sorteando {quant} JOGOS', '=-='*5)
for i, l in enumerate (jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('=-='*5, 'BOA SORTE!', '=-='*5)