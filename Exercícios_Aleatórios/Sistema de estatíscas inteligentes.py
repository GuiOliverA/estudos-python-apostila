def analisar_lista(lista):
    quantd = len(lista)

    if quantd == 0:
        print('Lista vazia. Nada para analisar.')
        return

    maior = max(lista)
    menor = min(lista)
    media = sum(lista) / quantd

    maior_cem = media >= 100

    print(
        f'Maior número da lista: {maior}\n'
        f'Menor número: {menor}\n'
        f'Quantidade de números: {quantd}\n'
        f'Média: {media:.2f}\n'
        f'A média é maior ou igual a 100? {maior_cem}'
    )


def linha(titulo_lista):
    print('=-=' * len(titulo_lista))


nome_lista_user = input('Digite o nome da lista:\n> ').strip().upper()
lista = []

n_list = int(input('Quantos números deseja digitar?\n> '))
for n in range(n_list):
    num = int(input(f'{n+1}º Digite um número:\n> '))
    lista.append(num)

lista.sort()
print(f'Todos os números da lista {nome_lista_user}: {lista}')
linha(nome_lista_user)
analisar_lista(lista)
linha(nome_lista_user)
