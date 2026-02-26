#Ler o primeiro termo e a razão de uma PA (Progressão Aritmética) e mostrar os 10 primeiros termos.
print('-=-'*10, '10 Termos de uma PA' , '-=-'*10)
termo1 = int(input('Primeiro termo\n> '))                         #Começa de qual número?
razao = int(input('Razão\n>'))                                   #Vai pulando quantos números?
for i in range (1,11): #ínicio, fim
    print (termo1)
    termo1 += razao                                              #termo1 soma e recebe razao