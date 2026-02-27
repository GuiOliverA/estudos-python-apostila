# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

n = int(input("Digite um valor em metros: \n"))
# print("{} metro(s), convertido(s) em centímetros, é {}cm; convertido(s) em milímetros é {}mm.".format(n, (n*100), (n*1000)))

print(f'{n} metro(s), convertido(s) em centímetros, é {n * 100}cm; convertido(s) em milímetros é {n * 1000}mm.')
print(f'{n} metro(s) convertido(s) em centímetros é: {n * 100}cm.')
print(f'{n} metro(s) convertido(s) em milímetros é: {n * 1000}mm.')
