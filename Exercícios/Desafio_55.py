#Ler o peso de 5 pessoas e mostrar qual foi o maior e o menor peso.
maior = 0
menor = 0
for p in range (1,6): #Para, em, intervalo. Ínicio, fim
    peso = float(input(f'[{p}ª] Qual o seu peso em Kg?\n> '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior: #define o maior 
            maior = peso
        if peso < menor: #define o menor
            menor = peso

print(f'O maior peso é {maior:.1f}\nO menor peso é {menor:.1f}')