#Soma de todos os números ímpares múltiplos de três entre 1 e 500.
soma = 0
cont = 0 
for i in range(1,501,+2): #ínicio, fim, passo
 if i % 3==0: #resto da divisão (Multiplos de 3)
   print(i)
   soma += i
   cont += 1
print(f'A soma de todos os {cont} números solicitados é:\n>{soma}')