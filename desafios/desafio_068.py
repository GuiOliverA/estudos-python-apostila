#Jogo do Par ou Ímpar. O computador joga contra você. 
#O jogo só para quando o jogador PERDER. No final, mostre o total de vitórias consecutivas que você conquistou.
from random import randint
from time import sleep
resultado = 0
vitoria = 0
print('-=-'*10 , 'PAR ou ÍMPAR' , '-=-'*10)
print(' '*26 , 'Usuário X Computador')
while True: #Enquanto não tiver o break, repete o loop
    num_computador = randint(1,10) 
    num_jogador = int(input('Digite um número de 1 a 10\n> '))
    if num_jogador <= 10:
        jogador = int(input('[1] = Ímpar\n[2] = Par\nEscolha uma opção\n> '))
        if jogador == 1:
            print('Você escolheu ÍMPAR...')
            sleep(1.5)
        elif jogador == 2:
            print('Você escolheu PAR...')
            sleep(1.5)
        if jogador < 3:
            if (num_jogador + num_computador) % 2 == 0: ##Verifica se a soma do jogador e computador é par ou ímpar
                resultado = 2         
            else:
                resultado = 1
            print('-=-'*10)
            print(f'Número jogador: {num_jogador}\nNúmero computador: {num_computador}\nResultado: {num_jogador + num_computador}')
            print('-=-'*10)
            sleep(2)
            if jogador == resultado:
                print('VOCÊ VENCEU! Jogue novamente.\n')  
                vitoria += 1
            else:
                print('VOCÊ PERDEU! Fim de jogo.\n') 
                break  
        else:
            print(f'ERRO, a opção {jogador} não é válida\nTente novamente!')
            print('Voltando ao início do jogo...\n ')
            sleep(1)
        
    else:
        print(f'ERRO, o número {num_jogador} não é válido\nTente novamente!')
        print('Voltando ao início do jogo...\n ')
        sleep(1)
print('Contando total de vitórias de consecutivas do usuário...')
sleep(2)
print('-=-'*10)
if vitoria > 0:
    print(f'Vitórias consecutivas: {vitoria}\nMuito bem!')
else:
    print(f'Vitórias consecutivas: {vitoria}\nBoa sorte na próxima vez haha')
print('-=-'*10)



