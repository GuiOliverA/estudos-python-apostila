def linha():
    print('=-=' * 30)


def adicionar_gastos(lista):
    compra = {}  # Não depende da variável global

    while True:
        compra['descricao'] = input('Descrição e/ou nome da compra:\n> ').strip().title()

        compra['valor'] = float(input(f"Valor da compra {compra['descricao']}:\n> ").replace(',', '.'))
        while compra['valor'] <= 0:
            compra['valor'] = float(input(f"⚠️ Valor inválido. Valor da compra {compra['descricao']}:\n> ").replace(',', '.'))

        lista.append(compra.copy())  
        compra.clear()                

        continuar = input('Adicionar nova compra? [S/N]\n> ').strip().lower()[0]
        while continuar not in 'sn':
            continuar = input('Não entendi, deseja continuar? [S/N]\n> ').strip().lower()[0]

        if continuar == 'n':
            break


def analisar_gastos(lista):
    if not lista:
        print('Nenhuma compra registrada!')
        return

    dinheiro_gasto = sum(g['valor'] for g in lista)
    print(f'Total gasto: R$ {dinheiro_gasto:.2f}')


# Programa principal
gastos = []
adicionar_gastos(gastos)
linha()
analisar_gastos(gastos)
linha()
