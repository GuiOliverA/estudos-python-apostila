#O usuário digita vários valores. Se o número já existir na lista, ele não será adicionado. Ao final, mostre os valores únicos em ordem crescente.
nums = list()
n = 0
simnao = ''
while True:
        n = int(input('Digite um valor:\n> '))
        while n in nums:
            print(f'Número {n} já fora adicionado, digite outro número!\n---')
            n = int(input('Digite um valor:\n> '))
        else:
              nums.append(n)
              print(f'Número {n} adicionado com sucesso!\n-')
              simnao = str(input('Deseja continuar? [S/N]\n> ')).strip().upper()
        while simnao[0] not in 'SN': 
                simnao = str(input('Deseja continuar? [S/N]\n> ')).strip().upper()
        if simnao[0] in 'N':
                    break
print('=-='*10)
print(f'Lista digitada: {nums}')
nums.sort()
print(f'Lista em ordem crescente: {nums}')


