
def fatorial (num, show = bool):
    """DEF FATORIAL, calcula o fatorial de um número

    Args:
        param num: número recebido pelo usuário
        param show: 'interruptor', se for True mostra o cálculo, se for False mostrará apenas o resultado
    """    
    from math import factorial
    resultado = factorial(num)
    
    if show: # se for True
        for cont in range (num, 0, -1): #lógica do fatorial, inicio, fim, passo
            print(cont, end= '')
            print(' x ' if cont > 1 else ' = ', end = '')
    
    return resultado
help(fatorial)

#programa principal
fat = int(input('Fatorial:\n> '))
show = str(input('Quer ver o cálculo? [S/N]\n: ')).strip().upper()[0]
if show in 'S':
    print(fatorial(fat, show = True))
elif show in 'N':
    print(fatorial(fat, show = False))
else:
    print('Resposta inválida, mostrando com cálculo...')
    print(fatorial(fat, show = True))
