#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
#No final, mostre um boletim contendo a média de cada um e permita que o usuário veja as notas de cada aluno individualmente.
from time import sleep
alunos_final = list()
infos = list()
notas = list()
nums_alun = list()
flag = n1 = n1 = 0
nome = ''
while True:
    nome = str(input('Nome aluno:\n> '))
    infos.append(nome)
    n1 = int(input('Nota um:\n> '))
    n2 = int(input('Nota dois:\n> '))
    media = (n1 + n2) /2
    infos.append(media)
    alunos_final.append(infos[:])
    infos.clear()
    infos.append(n1)
    infos.append(n2)
    notas.append(infos[:])
    infos.clear()
    simnao = str(input('Quer continuar? [S/N]\n> ')).upper().strip()[0]
    while simnao not in 'SN':
        simnao = str(input('ERRO. Apenas [S/N]:\n> ')).upper().strip()[0]
    if simnao == 'N':
        break
print('Calculando a média de todos os alunos...')
sleep(1)
print('=-='*10)
print('Nome e Média:')
print('=-='*10)
for num, alun in enumerate (alunos_final):
    print(f'[{num}] {alun[0]}' , end = '')
    print(f' {alun[1]}')
    nums_alun.append(num)
print('=-='*10)
while True:
    print('---'*5)
    flag = int(input('Mostrar as notas de qual aluno? [digite 999 para sair]\n> '))
    if flag == 999:
        break
    elif flag not in nums_alun:
        flag = int(input(f'Mostrar as notas de qual aluno? - {nums_alun} - [digite 999 para sair]\n> '))
    elif flag in nums_alun:
        print(f'Aluno: {alunos_final[flag][0]}\nNotas: {notas[flag]}')
        sleep(2)
    elif flag == 999:
        break
sleep(1)
print('Obrigado :)')