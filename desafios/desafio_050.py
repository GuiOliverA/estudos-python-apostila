#Ler seis números inteiros e somar apenas os que forem pares (divisiveis por 0).
soma = 0
for i in range (1,7): #ínicio, fim
    num = int(input(f'Digite um valor {i}: '))
    if num % 2 == 0:
        soma += num #soma = soma (0) + num digitado ||| soma = soma (cálculo anterior) + num digitado
print(f'A soma de todos os números PARES é igual a {soma}')