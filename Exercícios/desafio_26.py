# Faça um programa que leia uma frase qualquer e mostre:
# Quantas vezes aparece a letra "a"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

# Faça um programa que leia uma frase qualquer:
frase = str(input("Digite uma frase: \n")).lower().strip()

# Tamanho total da string (só porque eu quero mesmo):
print(f'A frase digitada tem {len(frase)} caracteres (incluindo os espaços).')

# Quantas vezes aparece a letra "a":
print(f'A letra "a" aparece {frase.count("a")} vezes na frase digitada.')

# Em que posição ela aparece a primeira vez:
print(f'A letra "a" apareceu pela primeira vez na posição {frase.find("a")}.')  # ou frase.index("a")

# Em que posição ela aparece a última vez:
print(f'A letra "a" apareceu pela última vez na posição {frase.rfind("a")}.')  # ou frase.rindex("a")