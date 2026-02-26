#Leia nome, ano de nascimento e carteira de trabalho (CTPS) e cadastre-os (com idade) em um dicionário. 
#Se a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. 
#Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar (considere 35 anos de contribuição).
from datetime import date
from time import sleep
ano_atual = date.today().year
dados_trab = {}
dados_trab['Nome'] = str(input('Nome:\n> ')).strip()
nasc = int(input('Ano de nascimento:\n> '))
dados_trab['Idade'] = ano_atual - nasc
dados_trab['CTPS'] = str(input('Carteira de trabalho (CTPS) (11 dígitos) (0 não tem):\n> ')).strip()

if dados_trab['CTPS'] != 0:
    dados_trab['Contratacao'] = int(input('Ano de Contratação: '))
    dados_trab['Salário'] = float(input('Salário: R$ '))
    # Lógica: Aposentadoria = (Ano Contratação + 35) - Ano Nascimento
    dados_trab['Aposentadoria'] = (dados_trab['Contratacao'] + 35) - nasc

print('-=' * 15)
sleep(1)

# Exibição dinâmica: mostra apenas o que existe no dicionário
for k, v in dados_trab.items():
    print(f'  - {k} tem o valor {v}')
if dados_trab['CTPS'] != 0:
    print(f' - Trabalhador irá se aposentar em {dados_trab['Contratacao'] + 35}')

if dados_trab['CTPS'] == 0:
    print('  - Status: CTPS não informada, sem dados de aposentadoria.')
