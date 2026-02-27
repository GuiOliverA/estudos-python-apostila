teste = list()
teste.append('Guilherme')
teste.append(22)

galera = list()
galera.append(teste[:])      #vai colocar na lista galera a teste toda [:] - do ínicio ao fim

teste[0] = 'Taine'           #vai trocar os índices da teste
teste[1] = 19
galera.append(teste[:])       #na galera vai colocar a teste toda [:] - ínicio ao fim
print(galera)
del galera

print(' \n', '=-='*10, '\n ')

galera = [['João' , 19] , ['Ana' , 33] , ['Joaquim', 13], ['Taine' , 19]]
print(galera[2][1])  #Do índice 2 quero o item 1 

for p in galera: #para cada pessoa (p) em galera: 
    print(f'{p[0]} tem {p[1]} anos de idade.')                  #quero só os itens 0 e 1
del galera

print(' \n', '=-='*10, '\n ')

galera = list()
dado = list()
totmai = totmen = 0
for i in range (0,3):
    dado.append(str(input('Nome:\n> ')))
    dado.append(int(input('Idade:\n> ')))
    galera.append(dado[:])                     #Do ínicio : até o final da lista até então
    dado.clear()          #"Limpa" a variável composta (lista) dado. Para entrar na repetição zerada de informações
for pess in galera:     #Para cada pessoa (item/contador) na lista galera
    if pess[1] >= 21:   
        print(f'{pess[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{pess[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade')