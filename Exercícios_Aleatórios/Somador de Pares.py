#Faça um programa que leia 6 números inteiros. Se o número for par, some-o ao total. Se for ímpar, ignore-o. Ao final, mostre o somatório.
quant_par = 0
soma = 0

for i in range (1,7): #Para, em, intervalo. #Ínicio, fim
    num = int(input(f'[{i}] Digite um número:\n> '))
    if num % 2 == 0:
        soma += num
        quant_par += 1

print(f'Soma dos números pares: {soma}')
print(f'Quantidade de números pares lidos {quant_par}')