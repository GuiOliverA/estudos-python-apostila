#Leia nome e preço de vários produtos. Pergunte se quer continuar. 
#No fim mostre: total gasto, quantos custam mais de R$ 1000 e o nome do produto mais barato.
total = mais1k = menor = contador = 0
nome_barato = ' '
print('=-='*10 , 'MERCADO SuperFaturado' , '=-='*10)
while True: #Enquanto não tiver break
                produto = str(input("Nome do produto:\n> "))
                print('---'*10)

                preco = float(input("Preço:\nR$"))
                if preco >= 1000: #Mais de um 1kR$
                    mais1k += 1 
                total += preco #TOTAL GASTO
                
                if contador == 1 or preco < menor: #Mais barato
                        menor = preco
                        nome_barato = produto #Nome mais barato
                    
                contador += 1

                sim_nao = ' ' #Enquanto não ter S ou N no sim_nao vai repetir a pergunta...
                while sim_nao not in 'SN':
                    sim_nao = str(input('Deseja continuar com as compras? [S/N]\n> '))[0].strip().upper()     
                if sim_nao == 'N':
                        break
                

print('-=-'*10)
print(f'Valor total gasto: R$ {total:.2f}\nProdutos que custam mais de 1mil reais: {mais1k}')
print(f'Nome do produto mais barato: {nome_barato} de R$ {menor:.2f}')
