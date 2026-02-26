#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
#O programa tem que analisar todos os valores e dizer qual deles é o maior.
from random import randint

def maior(n):
    maior = max(n)
    print('='*25)
    print(f'Maior número da lista: {n}\n> {maior}')
    print('='*25)


nums = []
for nn in range (0, randint(1,10)): #ínicio, fim (definido de 1 até 10 valores)
        nums.append(randint(1,100))

maior(nums)

