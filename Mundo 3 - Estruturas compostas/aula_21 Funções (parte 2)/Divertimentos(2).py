def fatorial(num= 1):
    f = 1
    for c in range (num, 0, -1):
        f *= c
    return 

f1 = fatorial(5)
f2 = fatorial(3)
f3 = fatorial(8)
print(f'Os resultados são {f1}, {f2} e {f3}')

print()
print()

def par_ou_impar (n=0):
    if n % 2 == 0:
        return True
    else:
        return False
    
num = int(input('Digite um número:\n> '))
if par_ou_impar(num): #se for True
    print(f'Número {num} é par!')
else:    #se for False
    print(f'Número {num} é ímpar!')