from random import sample
from time import sleep


# 1. O Computador sorteia 5 números ÚNICOS e guarda em uma TUPLA
# O sample garante que não haverá números repetidos no sorteio
sorteio = tuple(sample(range(1, 21), 5))

# 2. O Usuário faz o seu jogo em uma LISTA
palpite = []
print('--- BILHETE DE LOTERIA (1 a 20) ---')
for i in range(0, 5):
    num = int(input(f'Digite o {i+1}º número do seu jogo: '))
    while num < 1 or num > 20 or num in palpite:        #condicionais que nao seja menor que 1 e nem maior que 20
        num = int(input('Número inválido ou já digitado. Tente outro (1 a 20): '))
    palpite.append(num)

# 3. Comparação e Análise
acertos = []
for n in palpite:
    if n in sorteio: # Verifica se o seu número está dentro da tupla oficial
        acertos.append(n)

print('\n' + '=-=' * 10)
print(f'SORTEIO OFICIAL: {sorted(sorteio)}')
print(f'SEU JOGO:        {sorted(palpite)}')
print('=-=' * 10)
sleep(1)

# 4. Resultado Final
if len(acertos) == 0:
    print('Poxa, você não acertou nenhum número. Mais sorte na próxima!')
else:
    print(f'Parabéns! Você teve {len(acertos)} acerto(s).')
    print(f'Números acertados: {acertos}')