#Leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. Mostre: 
#A) Quantas pessoas cadastradas; 
#B) A média de idade; 
#C) Uma lista com as mulheres; 
#D) Uma lista com as pessoas com idade acima da média.

pessoas = []
dados = {}
media = soma_idade = 0
while True:
    dados['nome'] = str(input('Nome:\n> ')).strip()
    while True:
        dados['sexo'] = str(input('Sexo:\n> ')).upper().strip()[0]
        if dados['sexo'] in 'MF':
                break
    dados['idade'] = int(input('Idade:\n> '))
    soma_idade += dados['idade']
    pessoas.append(dados.copy())
    simnao = str(input('Deseja continuar? [S/N]\n>  ')).strip().upper()[0]
    if simnao not in 'SYN':
            simnao = str(input('Deseja continuar? [S/N]\n>  ')).strip().upper()[0]
    if simnao in 'N':
          break
print(f'A> Pessoas cadastradas: {len(pessoas)}')
media = soma_idade / len(pessoas)
print(f'B> Média de idade: {media:.2f}')
print(f'C> Mulheres cadastradas: ' , end = '')
for pessoa in pessoas:   #para cada pessoa (contador) na lista pessoas...
      if pessoa['sexo'] == 'F':
            print(f'{pessoa['nome']} ', end = '')
print('')
print('D> Lista de pessoas acima de média: ')
for pessoas in pessoas:
      if pessoas['idade'] >= media:
            print('   ', end = '')
            for k, v in pessoas.items():
                  print(f'{k} = {v} ', end = '')
            print()
print('---FIM---')             