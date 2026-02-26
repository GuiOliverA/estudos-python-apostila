#Exercício da tabuada, onde o usuário digita um número e você mostra os resultados de 1 a 10 usando um laço de repetição.
print('-=-'*10 , 'TABUADA' , '-=-'*10)

num = int(input('Digite um número\n> '))
print(f'Tabuada do número: [{num}]')
for i in range (1,11):    #Para, no intervalo de: Ínicio, fim
    print(f'{i} x {num} = {i*num}')  