from utilidades_cev import moeda

preco = float(input('Digite um valor:\n>R$'))
taxa = float(input('Valor da taxa (%):\n> '))
print(f'Valor digitado: R${moeda.moeda(preco)} ...\n- ')

print(f'''Valor com mais {taxa:.0f}% de taxa: {moeda.aumentar(preco, taxa, True)}
Valor com menos 10%: {moeda.diminuir(preco, taxa, True)}
Valor dobrado de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}
Valor da metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}''')