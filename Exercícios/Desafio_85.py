#O usuário digita sete valores numéricos e os cadastra em uma lista única que mantenha separados os valores pares e ímpares (uma lista com duas listas internas). 
#Ao final, mostre os valores pares e ímpares em ordem crescente. (reverse = True)
nums = list()
num_par = list()
num_impar = list()

for i in range (0,7):
    n = int(input('Digite um número:\n> '))
    if n % 2 == 0:
        num_par.append(n)
    else:
        num_impar.append(n)
nums.append(num_impar[:])
nums.append(num_par[:])
print(f'Números digitados: {nums}')
nums[0].sort()
nums[1].sort()
print(f'Lista números ímpares: {nums[0]}\nLista números pares: {nums[1]}')

print(' \n', 'Do professor G. Guanabara:', '\n ')

num = [[], []]        #declaração de uma lista com duas listas internas - 0 par, 1 ímpar
valor = 0
for i in range (1, 8):         #Para o var i no intervalo de ínicio 1 até  fim 7 (último valor ignorado)
    valor = int(input('Digite um valor:\n> '))
    if valor % 2 == 0:
        num[0].append(valor)      #Adiciona em num na lista interna de índice 0
    else:
        num[1].append(valor)     ##Adiciona em num na lista interna de índice 1
print('=-='*30)
print(f'Todos os valores digitados: {num}')
num[0].sort()
num[1].sort()
print(f'Valores pares: {num[0]}\nValores ímpares {num[1]}')
