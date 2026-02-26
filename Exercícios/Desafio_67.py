#Faça um programa que mostre a tabuada de vários números, um de cada vez. O programa será interrompido quando o número solicitado for negativo.
from time import sleep
while True: #Enquanto não tiver o break, repete o loop
    n = int(input('Digite um número para ver sua tabuada:\n> '))
    if n < 0:
        break
    print('-=-'*10, f'Tabuada do número {n}', '-=-'*10)
    for i in range (1,11): #Para i no intervalo de Ínicio Fim
        print(f'{n} x {i} = {n * i}')
    print(' ')
    sleep (2)
print(f'ERRO\nO número digitado ({n}) é NEGATIVO! Tente novamente!')