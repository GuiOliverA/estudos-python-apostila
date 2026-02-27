nome = str(input('Nome completo:\n> ')).strip().title()
print(f'{nome} com letras maísculas: {nome.upper()}')
print(f'{nome} com letras minúsculas: {nome.lower()}')

letras = len(nome) - nome.count(' ') 
print(letras)

print(f'Quantidade de letras (sem espaços): {letras}')

separado = nome.split()
print(f'Quantidade de letras do primeiro nome de {nome}: {len(separado[0])}')

if 'Silva' not in nome:
    print(f'O nome {nome} não contém o famoso "Silva" 😅')
else:
    print(f'Contém "Silva" no nome: {nome}')



