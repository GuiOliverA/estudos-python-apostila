#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. O programa tem que realizar três contagens: 
#a) De 1 até 10, de 1 em 1. 
#b) De 10 até 0, de 2 em 2. 
#c) Uma contagem personalizada.

from time import sleep
def contador_A(inicio, fim, passo):
    print('contagem de 0 até 10, passo de 1')
    for n in range (inicio, fim, passo): #para cada num no intervalo de Inicio, Fim e Passo x:
        print(n, end = ' ', flush = True)
        sleep(0.2)
    print('FIM!')
    
         
def contador_B(inicio, fim, passo):
    print('contagem de 10 até 0, passo 1')
    for i in range (inicio, fim, passo):
        print(i, end= ' ', flush = True)
        sleep(0.2)
    print('FIM!')


def contador_C(inicio, fim, passo):
    print(f'contagem de {ini} até {fi}, passo {pas}')
    for n in range (inicio, fim+1, passo):
        print(n, end = ' ', flush = True)
        sleep(0.2)   
    print('FIM!')


contador_A(1, 11, 1)  #A
print(' ')
contador_B(10, -1, -2)    #B
print(' ')
ini = int(input('Ínicio:\n> '))
fi = int(input('Fim:\n> '))
pas = int(input('Passo:\n> '))
print('Contagem personalizada:\n ')
contador_C(ini, fi, pas) #C

print('')
print('===== Professor: ======')
print('')

def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end=' ', flush = True)
            sleep(0.2)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end= ' ', flush = True)
            sleep(0.2)
            cont -= p
        print('FIM!')

#progama principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora você vai personalizar o contador!')
ini = int(input('Início:\n> '))
fim = int(input('Fim:\n> '))
pas = int(input('Passo:\n> '))
contador (ini, fim, pas)