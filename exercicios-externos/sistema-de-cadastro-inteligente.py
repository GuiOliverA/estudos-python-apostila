def linha():
    print('=' * 30)


def cadastrar(dados, pessoas):
    """cadastrar pessoas pelo nome e idade

    Args:
        dados dict = dicionário vazio de 'nome' e 'idade'
        pessoas list = lista vazia de usuários com dicionário de 'nome' e 'idade'

    Returns:
        retorna apenas a lista com os dicionários
    """    
    x = int(input('Quantas pessoas deseja cadastrar?\n> '))

    for p in range(x):
        dados['nome'] = input(f'({p+1}) Digite o nome:\n> ').strip().title()

        dados['idade'] = int(input(f"({p+1}) Digite a idade de {dados['nome']}:\n> "))
        while dados['idade'] <= 0:
            print('⚠️ Idade inválida (use maior que 0).')
            dados['idade'] = int(input(f"({p+1}) Digite a idade de {dados['nome']}:\n> "))

        pessoas.append(dados.copy())
        dados.clear()

    return pessoas


def analisar(lista):
    if not lista:                                               #Se a lista estiver vazia
        print('Nenhum usuário cadastrado.')
        return

    total = 0
    for p in lista:
        total += p['idade']
    media = total / len(lista)
    print(f'Média de idade dos usuários cadastrados: {media:.2f}')

    mais_velho = max(lista, key=lambda p: p['idade'])
    mais_novo = min(lista, key=lambda p: p['idade'])

    print(f"Usuário mais velho: {mais_velho['nome']} ({mais_velho['idade']} anos)")
    print(f"Usuário mais novo: {mais_novo['nome']} ({mais_novo['idade']} anos)")


# Programa principal
cadastro = {}
usuarios = []
cadastrar(cadastro, usuarios)
linha()
analisar(usuarios)
linha()