#Criar um módulo chamado moeda.py com as funções aumentar(), diminuir(), dobro() e metade().
'''Desafio 107'''

def aumentar(valor=0, taxa=0, formato=False):
    """_aumentar valores de acordo com a taxa em % _

    Args:
        valor (int, optional): Valor(float) informado. Defaults to 0.
        taxa (int, optional): valor da taxa (float) informado. Defaults to 0.
        formato (bool, optional): Se é formatado em R$XX,XX ou não. Defaults to False.

    Returns:
        _type_: Retorna com formatação com True e com False retorno sem formatação
    """    
    resultado = valor + (valor * taxa / 100)
    return moeda(resultado) if formato else resultado


def diminuir(valor=0, taxa=0, formato=False):
    resultado = valor - (valor * taxa / 100)
    return moeda(resultado) if formato else resultado


def dobro(valor=0, formato=False):
    resultado = valor * 2
    return moeda(resultado) if formato else resultado


def metade(valor=0, formato=False):
    resultado = valor / 2
    return moeda(resultado) if formato else resultado



'''Desafio 108'''

def moeda(valor=0, simbolo='R$'):
    return f'{simbolo}{valor:.2f}'.replace('.', ',')



'''Desafio 109'''
#adicionar um parâmetro 'sit', para evitar situações como está:
'''Valor dobrado de {moedas.moeda(preco)} é {moedas.moeda(moedas.dobro(preco))}
'''
#parece gambiarra 

'''Desafio 110'''
#Resumir todos os desafios em uma só função (def)

def resumo(preco = 0, taxa = 10, taxar = 5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preco: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'Com {taxa}% de aumento: \t{aumentar(preco, taxa, True)}')
    print(f'{taxar}% de redução: \t\t{diminuir(preco, taxar, True)}')
    print('-' * 30)