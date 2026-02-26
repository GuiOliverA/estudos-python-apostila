'''
Faça um programa que leia o ano de nascimento de um jovem e informe
de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento

Seu programa também deverá mostrar o tempo que faltou ou que passou do prazo
'''
from datetime import datetime

nasc = int(input("Em qual ano você nasceu? \n"))
ano_atual = datetime.now().year
# print("Ano atual: {}".format(ano_atual))
idade = (ano_atual - nasc)
if idade < 18:
    print(f'Você tem {idade} anos. Ainda faltam {18 - idade} anos para o alistamento.')
    print(f'Seu alistamento será em {nasc + 18}.')
elif idade > 18:
    print(f'Você tem {idade} anos. Já passou do tempo de alistamento.')
    print(f'Seu alistamento foi em {nasc + 18}.')
else:
    print(f'Você tem {idade} anos. Está na hora de se alistar!')