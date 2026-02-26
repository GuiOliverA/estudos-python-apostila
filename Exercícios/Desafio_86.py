#Crie uma Matriz 3x3 em Python e preencha com valores lidos pelo teclado. Ao final, mostre a matriz na tela com a formatação correta.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for lin in range (0,3):             #para cada linha no intervalo ínicio 0 e fim 3
    for col in range (0,3):         #para cada coluna no intervalo ínicio 0 e fim 3
        matriz[lin][col] = int(input(f'Digite um número para [{lin}, {col}]:\n> '))
print('=-='*10)
for lin in range(0,3):        #acima de alimentação (coleta de nums) e aqui de formatação
    for col in range (0,3):
        print(f'[{matriz[lin][col]:^7}]' , end='')         #um do lado do outro, sem quebra de linha
    print('')       #quebra de linha :