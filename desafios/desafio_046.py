#Contagem regressiva para estouro de fogos de artifício (10 a 0 com pausa de 1 segundo).
from time import sleep
R = str(input('Pronto para começar?\n[SIM] ou [NÃO]?\n>')).strip().lower()
if R == 'sim':
        cont = 0
        for cont in range (10,-1,-1): #Ínicio, fim, passo
                sleep(1)
                print(f'{cont}!')       
        print('BOOOOOMMM 💥💥💥')
elif R == 'não' or R == 'nao':
        print('Ok não vamos explodir nada : )')
else:
        print('ERROR!\nEscolha [SIM] ou [NÃO]')


print('---'*25 , 'Outra forma:' , '---'*25)



for cont in range (10,-1,-1): #Ínicio, fim, passo
                sleep(0.5)
                print(cont)       
print('BOOOOOMMM 💥💥💥')