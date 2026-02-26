'''for c in range (1,5): #Para, em, intervalo. Ínicio, Fim
    n = int(input('Digite um valor:\n> '))
print('FIM')'''

n= 1
while n != 0:
    n = int(input('Digite um número:\n> '))
print('FIM')
#-----------------------------------------------------------------
r = 'sim'
while r == 'sim': #até que seja respondido "sim"
    n = int(input('Digite um número:\n> '))
    r= str(input('Quer continuar?\n> [Sim/Não] ')).lower()
print('FIM')

#-----------------------------------------------------------------

n = 1 
par = impar = 0 
while n != 0:
    n = int(input('Digite um número:\n> '))
    if n != 0: #O 0 não vai ser considerado, ele é uma saída do loop While
        if n % 2 == 0:  
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares!')