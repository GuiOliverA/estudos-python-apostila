#Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.


def calculo_area(larg, compr):
    print(f'A área de um terreno {larg:.1f} x {compr:.1f} é de {larg*compr}m².')


print('-'*5 ,  'Controle de terrenos' , '-'*5)
l = float(input('Largura (m):\n> '))
c = float(input('Comprimento (m):\n> ')) 
calculo_area(l, c)

