#Leia vários números e mostre: 
#   A) Quantos números foram digitados; 
#   B) A lista de valores ordenada de forma decrescente; 
#   C) Se o valor 5 foi digitado e está ou não na lista.
print('=-='*10 , 'Minha solução:' , '=-='*10)

nums = []
while True:
        n = int(input('Digite um número:\n> '))
        nums.append(n)
        print(f'Número {n} adicionado na lista: {nums}\n---')

        simnao = str(input('Continuar? [S/N]\n> ')).upper().strip()
        print('-'*3)

        while simnao[0] not in 'SN':
            simnao = str(input('ERRO! Digite apenas "SIM ou "NÃO":\n> ')).upper().strip()
        if simnao[0] == 'N':
                    break
print('=-='*10)
print(f'Lista digitada: {nums}')
print('=-='*10)

nums.sort(reverse=True)

print(f'A: Quantidade de números digitados: {len(nums)}\nB: Lista ordenada de forma decrescente: {nums}')
if 5 in nums:
       print(f'C: Número 5 foi digitado na lista!')
else:
       print(f'C: Número 5 NÃO foi digitado na lista!')