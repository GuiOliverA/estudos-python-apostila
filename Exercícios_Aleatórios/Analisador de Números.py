#Peça para o usuário digitar quantos números ele quer analisar. Depois, leia todos eles e mostre qual foi o maior e qual foi o menor valor digitado.

maior = 0
menor = 0

fim_intervalo = int(input('Quantos números você quer analisar?\n> '))
for i in range (1,fim_intervalo +1): #Para, no intervalo de: Ínicio, fim
    num = int(input('Digite um número:\n→'))
    if i == 1:
           maior = num
           menor = num
    else:
          if num > maior:
                maior = num
          elif num < menor:
                menor = num
print(f'MAiOR número: {maior}\nMENOR número: {menor}')