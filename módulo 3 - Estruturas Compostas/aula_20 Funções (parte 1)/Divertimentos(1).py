def soma(a, b):         #Não exite o comando "soma()" no python, dito isso nós definimos (def) um comando "novo", chamado soma.
    print(f'A = {a} e B = {b}')
    s = a+b 
    print(f'A soma de A + B  = {s}')
    print('')
#'a' e 'b' são parâmetros


#Progama principal
soma(8, 9)
soma(a= 1, b =1)
soma(b= 30, a= 5)


print(' \n \n ')

def contar(*nums): # '*' = mostra ao python que irá receber vários parâmetros, seja 1, 2, 3 até 100...
    print('Dessa forma, criamos uma tupla:')
    print(nums)
    for valor in nums:
            print(f'{valor} ', end = '')
    print('FIM')
    print('')


contar(22, 19, 25)
contar(23, 22, 0)
contar(30, 5, 2026, 8, 9, 2025, 1, 1, 2026)   
print('=-='*30)

def contador(*num):
    tamanh = len(num)
    print(f'Recebi os valores {num} e são ao todo {tamanh} números')


contador(22, 19, 25)
contador(23, 22, 0)
contador(30, 5, 2026, 8, 9, 2025, 1, 1, 2026)

print('')
print('')


print('TRABALHAMOS COM TUPLAS ACIMA///\n///ABAIXO COM AS LISTAS:\n \n \n')


#criamos um comando que dobra os valores de uma lista
def dobra (lista):
     pos = 0
     while pos <len(lista):      #chamando o "dobra()", toda variável, ou parâmetro "lista"
        lista[pos] *= 2             #vai ser substituído por "valores"
        pos += 1

valores = [8, 9, 2025, 1, 1, 2026, 30, 5, 2026]
print(f'Sem a def "dobra()"com a lista valores: {valores}')
dobra(valores)
print(f'Após a def "dobra()" com a lista valores: {valores}')

print('')
print('')

print('Desempacotamento /Desempacotando:\n \n ')

def soma(*valores):
     s= 0
     for num in valores:
          s+= num
     print(f'Somando os valores {valores} temos {s}')

soma(8, 9)
soma(30, 5, 2026)
