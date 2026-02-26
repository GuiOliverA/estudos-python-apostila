a = (2, 5, 4)
b = (5, 8, 1, 2)
c= a + b #Vai colar as tuplas 'a' e 'b' 
print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')

print(len(c)) #Qual o tamanho da tupla?

print('\n-\n')

print(c.count(5)) #Quantos 5s tem no c? (a+b)
print(c.count(9))
print(c.count(2))

print('\n-\n')

print(c.index(2)) #Em qual posição? Está o número 8 da 'c'... a+b PEGA A PRIMEIRA OCORRêNCIA
print(c.index(2, 4)) #Número desejado e a partir da posição X (4)
print(c.index(5))

print('\n-\n')

pessoa = ('Guilherme', 22 , 60.2, 'Masculino') #Vários tipos de dados 
#del(pessoa) #Apaga a váriavel, ou tupla
#A tupla é imutável, porém pode ser apagada 

print(pessoa) #Vai dar erro, a 'pessoa' foi apagada com 'del'