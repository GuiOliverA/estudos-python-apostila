#Crie um programa que leia vários números inteiros. 
#O programa só vai parar quando o usuário digitar o valor 999 (Flag). No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

num = cont = soma = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]:\n '))
    if num == 999: break  
    soma += num
    quant += 1
print('---'*15)
print(f'Quantidade de números digitados: {quant}\nSoma dos {quant} números digitados: {soma}')
print('---'*15)
    
