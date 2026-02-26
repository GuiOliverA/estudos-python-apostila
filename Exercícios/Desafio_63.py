#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

print('-=-'*10 , 'Sequência de Fibonacci' , '-=-'*10)
N = int(input('Digite um número inteiro:\n> '))
t1 = 0
t2 = 1
print(f'{t1} → {t2}' , end = '')
contador = 3
while contador <= N:
    t3 = t1 + t2
    print(f' → {t3}' , end = '')
    t1 = t2
    t2 = t3
    contador += 1
print(' → FIM')
