#Gerencie o aproveitamento de um jogador de futebol. 
#O programa vai ler o nome e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida. Tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = {}
partidas = []

jogador['nome'] = str(input('Nome jogador(a):\n> '))
total = int(input(f'Quantas partidas {jogador['nome']} jogou?\n> '))
for c in range(0, total):      #para cada contador no intervalo ínicio 0 e fim var total (que vem do int acima)
    partidas.append(int(input(f'    Quantos gols na partida {c}?\n> ')))             #Número de gols de acordo com o total e colocar na lista partidas
jogador['gols'] = partidas[:]                     #A chave/key  'gols' do do dict jogador recebe a lista inteira '[:]' de partidas
jogador['total'] = sum(partidas)                    #A chave/key 'total' nada mais é do que a soma da lista partidas inteira
print('=-='*30)
print(jogador)           #print do dicionário (dict)
print('=-='*30)

for k, v in jogador.items():       #para cada key e value no método items()
    print(f'O campo {k} tem o valor {v}')           #A chave X tem valor X
print('=-='*30)

print(f'O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas.')

for i, v in enumerate(jogador['gols']):        #Para cada var 'i' (índice) e 'v' (elemento/valor) no intervalo enumerado do dict jogador[chave 'gols']
    print(f'    => Na partida {i}, fez {v} gols.')          #A chave 'gols' tem a lista inteira de partidas, ou seja, vai printar o índice e seu valor  
print(f'Foi um total de {jogador['total']} gols.')                  #print do total que é um sum() da lista partidas