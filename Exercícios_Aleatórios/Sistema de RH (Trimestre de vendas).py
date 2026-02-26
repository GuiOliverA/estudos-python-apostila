from time import sleep

empresa = []
maior_venda = 0
vencedor = ""

# 1. Cadastro de Funcionários
for c in range(0, 3):
    funcionario = {}
    funcionario['nome'] = str(input(f'Nome do {c+1}º funcionário: ')).strip()
    funcionario['cargo'] = str(input('Cargo: ')).strip()
    
    # Criando a Tupla de Vendas (Janeiro, Fevereiro, Março)
    print(f'Digite as vendas de {funcionario["nome"]} no 1º Trimestre:')
    vendas = (
        float(input('  > Janeiro: R$')), 
        float(input('  > Fevereiro: R$')), 
        float(input('  > Março: R$'))             )
    
    funcionario['vendas'] = vendas
    funcionario['total'] = sum(vendas) # Já deixamos o total calculado
    
    # Guardando na lista principal
    empresa.append(funcionario.copy())
    print('-' * 20)

# 2. Exibição dos Resultados
print('\n' + '=-=' * 15)
print(f'{"NOME":<15} {"CARGO":<15} {"TOTAL VENDAS":>12}')
print('-' * 45)

for f in empresa:                         #para cada item na lista empresa
    print(f'{f["nome"]:<15} {f["cargo"]:<15} R${f["total"]:>10.2f}')
    
    # 3. Lógica do "Vendedor de Ouro"
    if f['total'] > maior_venda:
        maior_venda = f['total']
        vencedor = f['nome']

print('-' * 45)
sleep(1)
print(f'🏆 VENDEDOR DE OURO: {vencedor} com R${maior_venda:.2f} em vendas!')
print('=-=' * 15)
print(empresa)     #essa lista tem: 
#Dicionário com os valores 'nome' , 'cargo' e 'venda'
#A chave 'vendas' tem uma tupla com as vendas de cada mês!!!