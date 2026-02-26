print('=-='*10, 'Criar um dicionário dentro de uma lista', '=-='*10)
brasil = []
estado1 = {'UF': 'Paraná', 'sigla': 'PR'}
estado2 = {'UF': 'Santa Catarina', 'sigla': 'SC'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print('')
print(f'Lista criada com os dicionários estado1 e estado2: {brasil}')       #Aqui usamos manipulação de listas também 
print(f'Primeiro índice 0: {brasil[0]}')
print(f'Segundo índice 1: {brasil[1]}')

print('')
print(f'Pegar o segundo índice da lista brasil (1) e mostrar a chave "sigla": {brasil[1]['sigla']} ')
print('')
del estado1, estado2, brasil

print('=-='*10, 'Parte 2', '=-='*10)
estado = dict()
brasil = list()
for c in range (0,3):              
    estado['UF'] = str(input('Unidade federativa (UF):\n> '))
    estado['sigla'] = str(input('Sigla do estado:\n> '))
    #brasil.append(estado[:])  fatiamento de uma lista de depois um '.clear()' não funciona para dicts, em razão das keys e values. Mas sim o .copy()
    brasil.append(estado.copy())
print(brasil)
print('')
for e in brasil:    #cada 'e' (de estado) é um dicionário 
    for k, v in e.items():      #Mostra tudo
        print(f'A chave (key) {k} tem valor (value) {v}.')
print('')
for e in brasil:
    for v in e.values():      #Mostra valores
        print(v , end = ' ')
    print('')