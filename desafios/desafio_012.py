# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

n = float(input("Digite o preço de um produto: \nR$"))
desconto = n * 5 / 100
print(f'O preço do produto com 5% de desconto é: R${n - desconto:.2f}.')