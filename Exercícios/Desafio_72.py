# Criar uma tupla com números por extenso (0 a 20). O programa deve ler um número pelo teclado e mostrá-lo por extenso usando a tupla.
contagem = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True: # enquanto o input for True e não False...
    # 1. Validação da entrada (Trava o usuário até ele digitar certo)
    while True:
        escolha = int(input('Digite um número entre 1 e 20: '))
        if 1 <= escolha <= 20:
            break
        print('Tente novamente. ', end='')

    # 2. Exibição do dado da tupla
    print(f'Você digitou o número {contagem[escolha -1].upper()}')

    # 3. Condição de parada
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    
    if resp == 'N':
        break

print('{:=^30}'.format(' PROGRAMA ENCERRADO '))
        



