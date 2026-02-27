from utilidades_cev import moeda

preco = float(input('Digite um valor:\n>R$'))
taxa = float(input('Valor da taxa (%):\n> '))
print(f'Valor digitado: R${preco} ...\n- ')

print(f'''Valor com mais {taxa:.0f}% de taxa: {moeda.moeda(moeda.aumentar(preco, taxa))}
Valor com menos 10%: {moeda.moeda(moeda.diminuir(preco))}
Valor dobrado de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}
Valor da metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}''')