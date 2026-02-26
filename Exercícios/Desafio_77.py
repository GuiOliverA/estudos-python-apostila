# Uma tupla com várias palavras (sem acentos). O programa deve mostrar, para cada palavra, quais são as suas vogais.    
palavras = ('Eu', 'Vou', 'Casar', 'Bem', 'Melhorar', 'Estudar', 'Trabalhar', 'Vencer')
for i in palavras:
    print(f'\nNa palavra "{i.upper()}" temos as vogais:', end = ' ')
    for vogal in i:
        if vogal.upper() in 'AÁÃÉEIÍÓOU':
            print(vogal.lower(), end = ' ')