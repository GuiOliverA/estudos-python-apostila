#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
#A primeira função vai sortear 5 números e colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.

from random import randint
from time import sleep


def sorteio(lista):
    print('Sorteando 5 valores da lista: ', end= ' ')
    for cont in range (0,5):
        n = randint(1, 100)
        lista.append(n)
        print(f'{n} ', end = ' ', flush = True)
        sleep(0.5)
    print('AGORA VAI!')
                                                          
def soma_par(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = []
sorteio(numeros)   #uma função namora com a outra, ou seja, só funciona se a def sorteio() vier primeiro, uma vez que a def soma_par() faz os cálculos de acordo com os números de sorteio()
soma_par(numeros)

