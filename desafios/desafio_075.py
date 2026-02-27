#Ler 4 valores pelo teclado e guardá-los em uma tupla. Mostrar: quantas vezes apareceu o 9, em que posição apareceu o primeiro 3 e quais foram os números pares.
nums = (int(input('Digite um valor:\n> ')), int(input('Digite um valor:\n> ')), int(input('Digite um valor\n> ')), int(input('Digite um valor:\n> ')))

print('=-='*10)
print(f'Valores digitados: {nums}')
print('=-='*10)
print(f'O número nove apareceu {nums.count(9)}x')
print('=-='*10)
if 3 in nums:
    print(f'O número três apareceu primeiro no índice (posição): {nums.index(3)} / (colocação) {nums.index(3)+1})')
else:
    print(f'O número 3 não foi digitado.')
print(f'Números pares digitados: ', end = '')
for i in nums: #para i em nums - cada valor se torna "i" temporariamente
    if i % 2 == 0:
        print(i, end = ' ')