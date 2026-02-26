#Crie um programa que leia vários números inteiros. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


sim_nao = 's'
contador = soma = maior = menor = 0
while sim_nao in 's':
    num = int(input('Digite um número:\n> '))
    contador += 1
    soma += num
    sim_nao = str(input('Deseja continuar a digitar valores? [SIM para continuar]\n> ')).lower().strip()[0]
    if contador == 1: #Vai analisar o primeiro 1 número digitado
        maior = num
        menor = num
    else:
        if num > maior: #Verifica o maior número digitado 
                maior = num
        if num <= menor: #Verifica o menor número digitado
                menor = num
    if sim_nao in 'n':
        break                
print(f'Quantidade de número digitados: {contador}\nMédia: {soma / contador:.1f}')
print(f'Maior valor: {maior}\nMenor valor: {menor}')




