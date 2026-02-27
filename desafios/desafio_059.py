#Crie um programa que leia dois valores e mostre um menu na tela (Somar, Multiplicar, Maior, Novos números, Sair). 
#Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

n1 = int(input('Digite um valor\n> '))
n2 = int(input('Digite um valor\n> '))
print(f'Valores digitados: [{n1}] [{n2}]')
escolha = 0

while escolha != 5: #Enquanto a variável escolha for diferente de 5
    escolha = int(input('''
[1] Somar
[2] Multiplicar
[3] Mostrar o maior valor
[4] Adicionar números diferentes
[5] Sair do programa
→ '''))
    
    if escolha == 1:
        print(f'{n1} + {n2} = {n1+n2}')    
        sleep (1)
        print('-=-'*15)

    elif escolha == 2:
        print(f'{n1} x {n2} = {n1*n2}')
        sleep (1)
        print('-=-'*15)
        
    elif escolha == 3:
        if n1 > n2:
            print(f'O maior número entre {n1} e {n2} é... {n1}')
            sleep (1)
            print('-=-'*15)
        else:
            print(f'O maior número entre {n1} e {n2} é... {n2}')
            sleep (1)
            print('-=-'*15)

    elif escolha == 4:
        print('Digite os números novamente:')
        n1 = int(input('Digite um valor\n> '))
        n2 = int(input('Digite um valor\n> '))
        sleep (0.5)
        print('-=-'*15)

    elif escolha == 5:
        print('Finalizando...')
        sleep(0.5)
        print('-=-'*15)

    else:
        print('Ops, opção inválida. Tente novamente.')
        print('-=-'*15)


print('Finalizando........')
sleep (1.5)
print('FIM DO PROGRAMA')

   