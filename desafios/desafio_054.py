#Ler o ano de nascimento de 7 pessoas e mostrar quantas são maiores de idade e quantas não.
from datetime import date

print('-=-'*10 , 'VOCÊ É MAIOR DE 18 ANOS?', '-=-'*10)
date.today().year
num_pess = 0
total_maior = 0
total_menor = 0

for pess in range(1, 8): #para, em intervalo. Ínicio, fim
    ano = int(input(f' {pess}ª: Digite o ano de nascimento\n→ '))
    ano18 = date.today().year - ano
    if ano18  >= 18:
        total_maior += 1
    else:
        total_menor += 1
print('---'*10)       
print(f'Maiores de 18 anos: {total_maior} pessoas.')
print('---'*10)
print(f'Menores de 18 anos: {total_menor} criança(s)/adolescente(s).')

