#Criar uma tupla com os 20 primeiros colocados do Brasileirão. Mostrar: os 5 primeiros, os 4 últimos, a lista em ordem alfabética e a posição do oitavo colocado.
#Lista tabela 2025
timesA = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol', 'Fluminense', 'Botafogo', 'Bahia', 'São Paulo', 'Grêmio',
           'Bragantino', 'Atlético-MG', 'Santos', 'Corinthians', 'Vasco da Gama', 'EC Vitória', 'Internacional', 'Ceará SC', 'Fortaleza', 'Juventude', 'Sport Recife') 

print('Tabela Brasileirão série A 2025:')
print('---'*10)
for t in timesA:
      print(t)
print('---'*10)
#Do índice 0 até o índice 19...
print('5 primeiros:')
for i in timesA[0:5]: #Para i em Tupla. Ínicio, Fim
        print(i) #5 primeiros
print('---'*10)
for um in timesA[:1]:
    print(f'Campeão: {um}') #Primeiro
print('---'*10)
print('4 Últimos Rebaixados para série B 2026:')
for c in timesA[-4:]: #Começa no 15 e vai até o final
    print(f'{c}') #4 últimos
print('---'*10)
print(f'Oitavo colocado: {timesA[7]}') #Oitavo
print('---'*10)
print(f'Posição do TIMÃO: {timesA.index('Corinthians')+1}º colocado') #Corinthians 
print('---'*10)
print(f'Em ordem alfabética: {sorted(timesA)}') #Ordem alfabética