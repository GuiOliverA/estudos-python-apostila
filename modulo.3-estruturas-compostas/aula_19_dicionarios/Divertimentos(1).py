pessoas = {'nome': 'Guilherme', 'sexo': 'M', 'idade': 22}                     #Dicionário: var = {} Tupla: var = () e Listas: var = []
print(pessoas)
print(f'O {pessoas['nome']} tem {pessoas['idade']} anos, do sexo {pessoas['sexo']}')        #Sempre tem keys com ':' e passando para outra key uma vírgula ','
print('')
print(f'Todas as chaves: {pessoas.keys()}')                             #Não existe índices numéricos nos dicts, mas sim CHAVES ou keys
print(f'Todos os valores: {pessoas.values()}')
print(f'Todos os itens: {pessoas.items()}')
print('=-='*10, 'LAÇOS', '=-='*10)

for k in pessoas.keys(): 
    print(f'Só as chaves (chaves, keys): {k}')
print('')

for k in pessoas.values():                                #variáveis contadores intuitivas:
    print(f'Só os valores (valores, values): {k}')          #k = key / v= value
print('')

for k, v in pessoas.items():
    print(f'Todos os itens (items)> Chave(key): {k} = Valor (value): {v}')
print('')

for k, v in pessoas.items():
    print(f'Todos os itens (items)> Chave(key): {k} = Valor (value): {v}')
print('')

pessoas['nome'] = 'Taine'              #Modificamos o dict e adicionamos uma chave
pessoas['idade'] = 19                  #(!) o '.append()' não funciona nos dicionários
pessoas['peso'] = 60
for k, v in pessoas.items():
    print(f'Todos os itens (items)> Chave(key): {k} = Valor (value): {v}')
print('')


del pessoas['sexo']                      #Deletando o elemento 'sexo'
for k, v in pessoas.items():
    print(f'Todos os itens (items)> Chave(key): {k} = Valor (value): {v}')
print('')



