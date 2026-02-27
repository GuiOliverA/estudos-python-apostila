# Crie um programa que leia o nome completo de uma pessoa:
nome = str(input("Digite seu nome: \n")).strip()

print(f'O nome em maiúsculas é: {nome.upper()}.')
print(f'O nome em minúsculas é: {nome.lower()}.')
print(f'O nome tem ao todo {len(nome) - nome.count(" ")} letras.')

nome = nome.split()
print(f'O primeiro nome é {nome[0]} e ele tem {len(nome[0])} letras.')