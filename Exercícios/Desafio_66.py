#Crie um programa que leia vários números. O programa só para quando digitar 999. No final, mostre a soma e quantos números foram digitados (sem contar o 999).
soma = cont = 0
while True:
    n = int(input('Digite um número [Digite 999 para interromper o programa]:\n> ')) #999 é a condição de parada 
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Números digitados: {cont}\nSoma total: {soma}')