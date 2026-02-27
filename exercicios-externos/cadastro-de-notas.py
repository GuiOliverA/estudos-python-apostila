from time import sleep
turma = []
for alun in range (0,5):
    notas = (float(input(f'(aluno {alun+1}) Nota 1:\n> ')), float(input(f'(aluno {alun+1}) Nota 2:\n> ')))
    turma.append(notas)
print('calculando a média de cada aluno...')
sleep(1)

# Exibição Automática
for indice, notas_do_aluno in enumerate(turma):    #para cada var (variável contador de índices "indice") e var (variável de cada valor na lista turma). Enumerando a lista turma
    # notas_do_aluno é a tupla (nota1, nota2)
    media = sum(notas_do_aluno) / 2  #soma de cada valor (ou tupla) da lista divido por 2
    print(f'Média aluno {indice + 1} = {media:.1f}')