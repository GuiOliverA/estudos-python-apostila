i= int(input('Ínicio: '))
f= int(input('Fim: '))
passo = int(input('Passo: '))
for c in range (i, f+1, passo): 
    print(c, i, passo)
print('FIM')

#--
soma = 0
for c in range (0,3):
    num = int(input('Digite um número: '))
    soma += num

print(f'A soma de todos os valores foi {soma}.')