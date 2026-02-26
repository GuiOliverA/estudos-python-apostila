val = []
val.append(5)
val.append(7)
val.append(2)
print(f'Print de forma "feia": {val}')
print(f'Print de forma bonitinha: ')
for i in val:   #para cada valor (ou elemento) da lista val
    print(f'{i} → ' , end='... ')
print('')                #Saiu do "end = ''"   😅
print('=-='*10)


for c, i in enumerate(val):       #dois contadores, um para índice (posição) e outros para os valores (elementos)
    print(f'No índice {c} encontrei o valor {i}!')
print('FIM DA LISTA')
del val        #Para continuar a aula...
print('=-='*10)


val = list()              #declaração de var com lista vazia
for i in range (0,5):      #Para i no intervalo de ínicio 0 e Fim 5
    val.append(int(input('Digite um valor para lista "val":\n> ')))
for ind, valor in enumerate(val):
    print(f'No índice {ind} encontrei o valor {valor}!')
print(val)
print('FIM DA LISTA')
print('=-='*10)

a= [2, 5, 6, 8]
b = a           #Ligação da lista "a" e "b"
b[2]= 8        #Mexeu nos dois pois ligou as listas acima
print(f'Lista A: {a}')
print(f'Lista B: {b}')
del a, b
print('=-='*10)

a= [2, 5, 6, 8]
b = a[:]           #Cortou com fatiamento, do ínicio e final da lista 
b[2]= 8        
print(f'Lista A: {a}')
print(f'Lista B: {b}')
