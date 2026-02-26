#Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120.
from math import factorial 

num = int(input('Digite um número e veja seu fatorial:\n> '))
contador = num
print(f'Calculando {num}!... ', end = '')
while contador > 0:
    print(f'{contador}' , end = '')      #end = no final do print terá ''
    print(' x ' if contador > 1 else '= ', end = '') #se o contador > 1 se não coloca '=' atrás do 1
    contador -= 1 
print(factorial(num))

