#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
from random import choice
from time import sleep
alunos = []
for alun in range (0,4):
    alunos.append(str(input(f'Nome {alun + 1}º aluno:\n> ')).strip().title())
print(f'''Nome dos alunos:
1 = [{alunos[0]}] 
2 = [{alunos[1]}]
3 = [{alunos[2]}]
4 = [{alunos[3]}]     
      ''')
print(f'Sorteando aluno para apagar o quadro...')
sleep(1.5)
print(f'aluno sorteado: {choice(alunos)}!')
    