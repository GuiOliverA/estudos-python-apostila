def analisar_biblioteca(lista):
    #Média de páginas
    total_pg = 0  
    for livros in lista:
        total_pg += livros['paginas']
    
    media = total_pg / len(lista) 
    
    print(f'\nMédia de páginas: {media:.1f}')
    print(f'Total de páginas no acervo: {total_pg}')

    #Livro mais antigo
    ano_mais_antigo = lista[0]['ano']
    titulo_mais_antigo = lista[0]['titulo']
    for livro in lista:
        if livro['ano'] < ano_mais_antigo:
            ano_mais_antigo = livro['ano']
            titulo_mais_antigo = livro['titulo']
    print(f'Livro mais antigo: {titulo_mais_antigo} ({ano_mais_antigo})')

    #Livros modernos (pós 2020)
    livros_modernos = []
    for livro in lista:
        if livro['ano'] > 2020:
            livros_modernos.append(livro['titulo'])
        if len(livros_modernos) == 0:
            livros_modernos = 'Nenhum livro pós 2020 encontrado'
    print(f'Livros modernos (pós-2020): {livros_modernos}')

#Programa Principal
biblioteca = []
acervo = {}

while True:
    acervo['titulo'] = str(input('Título: ')).strip().title()
    acervo['autor'] = str(input(f"Autor de {acervo['titulo']}: ")).strip().title()
    acervo['ano'] = int(input('Ano: '))
    acervo['paginas'] = int(input('Páginas: '))

    biblioteca.append(acervo.copy())
    
    resp = str(input('Continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break

analisar_biblioteca(biblioteca)