#Ler um número inteiro e dizer se ele é ou não um número primo.
#Um número primo é um número natural maior que 1 que POSSUI APENAS DOIS DIVISORES positivos distintos: o número 1 e ele mesmo. 

num = int(input('\033[mDigite um número:\n>'))
total_divs = 0
for i in range (1, num +1): #Ínicio (1), Fim (num) e Passo (+1)    #'i' é a váriavel contador 
    if num % i == 0:      #dívisivel por
        print('\033[33m')
        total_divs += 1
    else:
        print('\033[31m')
    print(f'{i}')
print(f'\n\033[mO número {num} foi divisível {total_divs} vezes')
if total_divs == 2:
    print(f'O número {num} É PRIMO')
else:
    print(f'O número {num} NÃO É PRIMO')