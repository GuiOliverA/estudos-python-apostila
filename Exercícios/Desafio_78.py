#Leia 5 valores numéricos, guarde-os em uma lista e mostre qual foi o maior e o menor valor digitado, com suas respectivas posições.
menor = 0
maior = 0
val = list()
for cont in range(0,5):
    val.append(int(input(f'Digite um valor para índice {cont}:\n> ')))
print('=-='*10)
for ind, num in enumerate(val):
    print(f'índice: {ind}\nNúmero: {num}\n ')
    if ind == 4:
        print('=-='*10)
    if ind == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num <= menor:
            menor = num
print(f'Lista "val": {val}')
print('=-='*10)
print(f'MAIOR número digitado: {maior}\nNos índices: ' , end = '')
for i , valor in enumerate(val):
    if valor == maior:
        print(f'{i}... ', end = '') 
del i, valor
print('')
print(f'MENOR número digitado: {menor}\nNos índices: ', end = '')
for i, valor in enumerate(val):
    if valor == menor:
        print(f'{i}... ', end = '')
print('')
print('=-='*10)


