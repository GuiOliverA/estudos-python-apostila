lanche = ('Hambúrguer' , 'Suco', 'Pizza' , 'Pudim')
print(lanche[:2])
#Tuplas são imutáveis (em execução)

print('\n-\n')#-------------------------------

lanche = ('Hambúrguer' , 'Suco' , 'Pizza' , 'Pudim', 'Batata frita')
for contador in range (0, len(lanche)): #Para cont no intervalo de 0, 4 (len ignona último valor)
    print(f'Eu vou comer {lanche[contador]} na posição {contador}')

print('\n-\n')#------------------------------------

for comida in lanche:  #Para contador na lista X (Sem ínicio, fim, passo)
    print(f'Eu vou comer {comida}')

print('\n-\n')#-------------------------------------

for pos, comida in enumerate (lanche): #Para pos na posição enumerada lanche
    print(f'Eu vou comer {comida} na posição {pos}')

print('\n-\n')

lanche = ('Hambúrguer' , 'Suco' , 'Pizza' , 'Pudim' , 'Batata Frita')
print(lanche) #mostra os itens da tupla (listas) lanche, em ordem
print(sorted(lanche)) #Ordem decrescente e alfabética

print('comi pra caramba')
