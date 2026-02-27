#Gerar 5 números aleatórios, colocar em uma tupla e mostrar o menor e o maior valor gerado.
from random import randrange
print('Valores sorteados:')
sortead = (randrange(100) , randrange(100) , randrange(100) , 
           randrange(100) , randrange(100))
for i in sortead:
    print(f'({i})', end = ' ' )        
print(f'\nMaior número: {max(sortead)}')
print(f'Menor número: {min(sortead)}')