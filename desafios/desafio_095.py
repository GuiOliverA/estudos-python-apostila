# Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogador = {}
partidas = []
time = []

while True:
    jogador['nome'] = str(input('Nome jogador(a):\n> '))
    total = int(input(f'Quantas partidas {jogador['nome']} jogou?\n> '))
    partidas.clear()
    for c in range(0, total):      #para cada contador no intervalo ínicio 0 e fim var total (que vem do int acima)
        partidas.append(int(input(f'    Quantos gols na partida {c}?\n> ')))             #Número de gols de acordo com o total e colocar na lista partidas
    jogador['gols'] = partidas[:]                     #A chave/key  'gols' do do dict jogador recebe a lista inteira '[:]' de partidas
    jogador['total'] = sum(partidas)                    #A chave/key 'total' nada mais é do que a soma da lista partidas inteira
    time.append(jogador.copy())

    while True:
        simnao = str(input('Quer continuar? [S/N]\n> ')).upper().strip()[0]
        if simnao in 'SN':
            break
        print('ERRO, Responda apenas S ou N:\n>')
    if simnao == 'N':
            break

print('=-='*30)
print('cod ', end= '')
for i in jogador.keys():
     print(f'{i:<15}' , end= '')
print()

print('=-='*30)
for k ,v in enumerate(time):
     print(f'{k:>3} ' , end='')
     for d in v.values():
          print(f'{str(d):<15}', end= '')
     print('')
print('=-='*30)

while True:
     busca = int(input('Mostrar dados de qual jogador? [999 p/ parar]\n> '))
     if busca == 999:
          break
     if busca >= len(time):
          print(f'Erro! não existe jogador com o código (cod) {busca}!')
     else:
          print(f' --- LEVANTAMENTO JOGADOR {time[busca] ['nome']}:')
          for i, g in enumerate(time[busca]['gols']):
               print(f'         No jogo {i} fez {g} gols.')
print('Obrigado :)')