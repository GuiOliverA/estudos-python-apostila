num = [2,5,9,1]
print(f'Lista "num" original: {num}')
num[2] = 3
num.append(7)
print(f'Lista com o índice 2 substituído e o valor "7" adicionado: {num}')
print('---'*10)

num.sort()
print(f'Lista em ordem decrescente: {num}')
print('---'*10)

num.sort(reverse = True)
num.insert(2, 0)
print(f'Lista com ordem -reversa- e com o índice 2 substituído pelo valor 0: {num}')
print('---'*10)

print(f'Essa lista tem {len(num)} elementos (quantidade).')
print('---'*10)

num.pop()         #Remove o último valor
print(f'Lista com o .pop() sem parâmetro: {num}')
num.pop(2)                 #Remove o índice 2 (número 0)
print(f'Lista com o .pop() com parâmetro 2, removendo o índice 2: {num}')
print('---'*10)

num.insert(2,2)      #colocar no índice 2 o valor 2
print(f'Lista com o índice 2 trocado pelo valor 2: {num}')
print('---'*10)

num.append(2)       #Adiciona um novo índice e um valor 2, no final da lista
print(f'Lista com novo índice e com valor 2 no final: {num}')
num.remove(2)       #Vai remover o primeiro número dois que encontrar:
print(f'Lista com o .remove(2), removeu apenas o primeiro valor 2 encontrado: {num}')
#Para remover mais números temos os laços:
while 2 in num:
    num.remove(2)
print(f'Lista sem os valores 2: {num}')
print('---'*10)

if 4 in num:
    num.remove(4)        #sem a verificação do if vai dar erro, não tem 4 in num
else:
    print(f'Nenhum valor fora removido, não existe o valor 4 na lista: {num}')
print(num)
print('---'*10)