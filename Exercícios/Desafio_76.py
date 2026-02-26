#Uma tupla única com nomes de produtos e preços sequenciais. Mostrar uma listagem de preços organizada de forma tabular.
produtos = ('Notebook Samsung', 4500,
            'Mousepad' , 50,
            'Mouse', 50,
            'Monitor 640Hz', 900,
            'Teclado', 200,
            'Lâmpada', 75,
            'Cadeira ergonômica', 450,
            'Fones de ouvido', 100,
            'Kit limpeza notebook', 90)
print('---'*15)
print('Lista de preços')
print('---'*15)
for posicao in range (0, len(produtos)): #Para posicao no intervalo. Ínicio 0, Fim ler tamanho de cada produto da tupla
    if posicao % 2 == 0: #Os produtos estão sempre em índice par e preço no ímpar
        print(f'{produtos[posicao]:.<30}' , end = '') #:. < trinta pontinhos "." a 30 posições da esquerda até o item
    else: #Se for ímpar o índice
        print(f'R${produtos[posicao]:.2f}')
print('---'*15)