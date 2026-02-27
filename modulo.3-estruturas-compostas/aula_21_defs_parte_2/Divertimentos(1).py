print('--- Retornando valores ---')

print('CÓDIGO COM LIMITAÇÃO: ')
def somar (a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')

somar(3, 2, 10)
somar(2, 2)
somar(4)


print('')
print('--- COM RETURN: ---')

def somar_ret (a=0, b=0, c=0):
    s = a + b + c
    return s      #permite que o resultado seja atribuído a variáveis
                #neste caso, temos 4x respostas
r1 = somar_ret(3, 2, 10)
r2 = somar_ret(2, 2)
r3 = somar_ret(4)
r4 = somar_ret(30, 5, 2026)
print(f'Os resultados foram {r1}, {r2}, {r3} e {r4}')

