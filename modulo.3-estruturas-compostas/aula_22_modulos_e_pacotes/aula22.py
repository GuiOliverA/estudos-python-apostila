from uteis import numeros

num = int(input('Digite um valor:\n> '))
fat = numeros.fatorial(num)       #não precisa usar "uteis." pois já fora importado isoladamente 
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')  #não precisa usar "uteis." pois já fora importado isoladamente 
print(f'O triplo de {num} é {numeros.triplo(num)}')   #"precisa" usar "uteis." pois não foi importado de forma isolada
