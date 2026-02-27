#Leia vários números e crie três listas:
#1: Completa
#3: Só com pares.
#2: Só com ímpares. Mostre as três listas no final.
from time import sleep
nums = []
nums_par = []
nums_impar = []
quant = int(input('Quantos números quer digitar na lista?\n> '))
print(f'Vamos digitar {quant} números na nossa lista...\n ')
sleep(1)
for i in range (0, quant):       #Para i no intervalo 0 Ínicio e quant Fim
    n = int(input('Digite um número:\n> '))
    nums.append(n)
    if n % 2 == 0:            #Identifica números pares e adiciona na lista par
        nums_par.append(n)
    elif n % 2 != 0:        #Identifica números ímpares e adiciona na lista ímpar
        nums_impar.append(n)
print(f'{quant} números digitados, organizando lista...\n ')
sleep(1)
print('=-='*10)
print(f'Lista completa: {nums}\nLista com números pares: {nums_par}\nLista com números ímpares: {nums_impar}')