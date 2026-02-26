from Interno import cores

def ajuda(com):  # comando
    titulo(f"Acessando o manual do comando '{com}'")
    help(com)


def titulo(mensagem):
    tam = len(mensagem) + 4
    print('=' * tam)
    print(f'  {mensagem}')
    print('=' * tam)


# Programa principal
while True:
    titulo('SISTEMA DE AJUDA PyHelp')
    comando = input('Função ou biblioteca:\n> ').strip()

    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

titulo('BONS ESTUDOS')


