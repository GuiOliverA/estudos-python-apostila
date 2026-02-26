# Leia nome e média de um aluno, guardando também a situação (Aprovado/Reprovado) em um dicionário. Mostre o conteúdo no final. (Média 7)
boletim = {}
boletim['Nome'] = str(input('Nome aluno(a):\n> ')).strip()
boletim['Média'] = float(input(f'Média aluno(a) {boletim['Nome']}:\n> '))
if boletim['Média'] >= 7:
        print(f'Aprovado(a), parabéns')
elif boletim['Média'] == 6:
        print(f'Aprovado(a)')
elif boletim['Média'] < 6:
        print(f'Reprovado(a)')
print(f'''Nome: {boletim['Nome']}
Média: {boletim['Média']}''')
print('')

print('=-='*5 , 'Guanabara:', '=-='*5)

aluno = {}
aluno['Nome'] = str(input('Nome:\n> '))
aluno['Média'] = float(input(f'Média de {aluno['Nome']}:\n> '))
if aluno['Média'] >= 7:
        aluno['Situação'] = 'Aprovado(a)'
elif 5 <= aluno['Média'] < 7:
        aluno['Situação'] = 'Recuperação'
else:
        aluno['Situação'] = 'Reprovado(a)'
for k, v in aluno.items():      #Para cada k (key), value(v) no dict aluno (todos os itens)
        print(f'{k}: {v}')