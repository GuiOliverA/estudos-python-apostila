#Digite 5 valores numéricos e cadastre-os já na posição correta de inserção (sem usar o sort()). Mostre a lista ordenada no final.
num = list()
for i in range (0,5):                                       #Para i no intervalo de ínicio 0 e Fim 5
    n = int(input('Digite um número:\n> '))
    num.append(n)
    print(f'Lista até aqui: {num}')
num.sort()
print(f'Lista na ordem correta: {num}')

print('-=-=-=-\nGUANABARA:\n-=-=-=-\n ')
del num

print('=-='*10 , 'Conheça a importância do .sort():', '=-='*10)
lista = []
for i in range (0,5):
    n = int(input('Digite um valor:\n> '))
    print(f'Lista: {lista}')

    if i == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')                #Adiciona o maior ao final da lista
    
    else:
        posicao = 0
        while posicao < len(lista):
                
                if n <= lista[posicao]:            #Adiciona o número na posição X da lista
                    lista.insert(posicao, n)
                    print(f'Adicionado na posição {posicao} da lista...')      
                    break
                
                posicao += 1
print('=-='*10)
print(f'Os valores digitados em ordem foram {lista}')


