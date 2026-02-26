#Criar um módulo chamado moeda.py com as funções aumentar(), diminuir(), dobro() e metade().

from utilidades_cev import moeda

valor = float(input('Digite um valor:\n> '))
taxa = float(input('Valor da taxa (%):\n> '))
print(f'Valor digitado: R${valor} ...\n- ')

print(f'''Valor com mais {taxa}% de taxa: R${moeda.aumentar(valor, taxa)}
Valor com menos 10%: R${moeda.diminuir(valor)}
Valor dobrado: R${moeda.dobro(valor)}
Valor pela metade: R${moeda.metade(valor)}''')
