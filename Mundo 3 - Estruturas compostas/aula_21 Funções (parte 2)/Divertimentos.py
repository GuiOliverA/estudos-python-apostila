print('--- Docstrings e "help(comando ou def)"')
def contagem (inicio, fim, passo):
    """_summary_

    Args:
        inicio (int): inicio da contagem
        fim (int): fim da contagem
        passo (int): passo da contagem
    """


    cont = inicio
    while cont <= fim:
        print(f'{cont}', end=' → ')
        cont += passo
    print('FIM!')
    
contagem(0,22,2)

print('')
print('--- Parâmetros opcionais: ---')

def somar (a= 0, b= 0, c= 0):
    """_summary_

    Args:
        a (int): Soma 
        b (int): Soma
        c (int): Soma
    """    
    s = a + b + c 
    print(f'A soma vale {s}')
somar(3,10)
somar(c=4, b = 2)



print('')
print('--- Escopo de variáveis ---')

def teste():
    x = 8                               #escopo local da função teste()
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


#Programa principal
n = 2                       #var escopo global, funciona em todo o código
print(f'No progama principal, n vale {n}')
teste()
#print(f'No programa principal, x vale {x}') - retorno ERRO, var x é escopo local
print('')

def testeA(b):
    global a    #var 'a' deixou de valer 5
    a = 8
    b += 4   #vai dar 9
    c = 2       #local   
    print(f'A (def) dentro vale {a}')
    print(f'B (def) dentro vale {b}')
    print(f'C (def) dentro vale {c}')

#programa principal
a = 5       #global
testeA(a)
print(f'A fora (programa principal) vale {a}')

print('')
for i in range (0, 3):
    print(i)


#quero um programa que fale que o Guilherme é lindo, mas só 500 vezes
def elogio(nome, vezes):
    for i in range(vezes):
        print(f'{nome} é lindo!', end=' ')
elogio('Guilherme', 500)