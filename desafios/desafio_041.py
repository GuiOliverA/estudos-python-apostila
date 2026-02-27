from datetime import date

#A Confederação Nacional de Natação precisa de um programa que leia
#o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

#até 9 anos: mirim
#até 14 anos: infantil
#até 19 anos: júnior
#até 20 anos: sênior
#acima de 20: master

atual = date.today().year
nasc = int(input('Ano de nascimento do(a) nadador(a): \n'))
idade = atual - nasc
print(f'O atleta tem {idade} anos em {atual}.')


if idade <= 9:
    print(f'Classificação Mirim: {idade}.')
elif idade <= 14:
    print(f'Classificação Infantil: {idade}.')
elif idade <= 19:
    print(f'Classificação Júnior: {idade}.')
elif idade <= 25:
    print(f'Classificação Sênior: {idade}.')
else:
    print(f'Classificação Master: {idade}.')
