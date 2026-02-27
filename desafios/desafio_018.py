# Desafio 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians

ang = float(
    input("Digite um ângulo de uma circunferência (ou seja, entre 0º e 360º): \n")
)

seno = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))

print(f'O seno, cosseno e tangente do ângulo {ang:.2f}º são, respectivamente: {seno:.2f}, {coss:.2f} e {tang:.2f}.')
