#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('-=-'*10, '10 TERMOS DE UMA PA' , '-=-'*10)
primeiro = int(input('Primeiro termo?\n> '))
razao = int(input('Razão (PA)?\n> '))
termo = primeiro
contador = 1
while contador <= 10:
    print(f'{termo} → ' , end = '') #end = final da linha
    termo += razao
    contador += 1
print('FIM')
