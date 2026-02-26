#Leia nome e peso de várias pessoas. Guarde tudo em uma lista composta. Mostre:
#A) Quantas pessoas foram cadastradas; 
#B) Uma listagem com as pessoas mais pesadas; 
#C) Uma listagem com as pessoas mais leves.

pess_peso = list()
dados = list()
maior = menor = 0
while True:
    dados.append(str(input('Nome:\n> ')))
    dados.append((float(input('Peso:\n> '))))
    if len(pess_peso) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pess_peso.append(dados[:])                    #[:] > Fatiamento total da lista dados e insere (append) na lista pess_peso
    dados.clear()                                 #Limpa a lista dados para incluir novas informações
    
    simnao = str(input('Quer continuar? [S/N]\n> ')).upper().strip()[0]
    while simnao not in 'SN':
        simnao = str(input('Apenas "Sim" ou "Não". Quer continuar? [S/N]\n> ')).upper().strip()[0]
    if simnao == 'N':
        break
print('=-='*10)
print(f'Lista digitada: {pess_peso}')
print(f'A: Pessoas cadastradas: {len(pess_peso)}...')
print(f'B: Maior peso registrado: {maior}Kg -' , end ='')
for pess in pess_peso:
    if pess[1] == maior:
        print(f' {pess[0]} ' , end='')
print('')
print(f'C: Menor peso registrado: {menor}Kg -' , end='')
for pess in pess_peso:
    if pess[1] == menor:
        print(f' {pess[0]} ' , end='')
print('')
print('=-='*10)

