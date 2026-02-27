#Refazer a Tabuada (Desafio 009) utilizando o laço for.

print('-=-'*10, 'tabuada 1 a 10' , '-=-'*10)

num = int(input("Digite um número para ver sua tabuada:\n>"))
for i in range (1,11):
  print(f'{num} x {i} = {num*i}')
  
#poderíamos adicionar também: soma = num * multi e colocar soma na última chave{soma}