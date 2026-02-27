# Faça um programa que leia a largura e a algura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

largura = float(input("Digite a largura: \n"))
altura = float(input("Digite a altura: \n"))
area = largura * altura

print(f'A área da parede é: {area:.2f}m².')

# Cada litro (L) de tinta pinta uma área de 2m².
tinta_necessaria = area / 2
print(f'A quantidade de tinta necessária para pintar a parede é: {tinta_necessaria:.2f}L.')
# Conferir a resposta porque não sei se entendi o problema. O velho Guilherme continua o mesmo, só que agora com ímpeto suficiente para continuar
