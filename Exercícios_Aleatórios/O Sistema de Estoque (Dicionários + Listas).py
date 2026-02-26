item = {}
estoque = []
soma_preco = []
soma_x_quantidade = []

def adicionar_item():
        item['nome'] = str(input('Nome produto:\n> ')).strip()
        item['quantidade'] = int(input('Quantidade:\n> '))
        item['preço unitário'] = float(input('Preço unitário:\n> '))
        soma_x_quantidade.append(item['quantidade'] * item['preço unitário'])
        estoque.append(item.copy())
        item.clear()
        print(estoque)

while True:

    simnao = str(input('Adicionar novo item? [S/N]\n> ')).upper().strip()[0]
    if simnao not in 'SN':
            simnao = str(input('Adicionar novo item no estoque? [S/N]?\n> ')).upper().strip()[0]
    elif simnao == 'S':
            adicionar_item()
    elif simnao == 'N':
            break
if not estoque:
      print('Nenhum item fora adicionado ao estoque.\nVolte sempre.')  
else:
      print(f'Itens no estoque: {len(estoque)}')
      print(f'Investimento total [quantidade x preço de todos os itens]: R${sum(soma_x_quantidade):.2f}')
      