#Ler uma frase e dizer se ela é um palíndromo (lê igual de trás para frente).
frase_original = str(input('Digite um frase.\n→ ')).strip().upper()
palavras = frase_original.split() #Dividiu as palavras da frase_original e colocou em "palavras"
junto = ''.join(palavras) #juntar as palavras com espaço " " e colocou em "junto"
print(f'Você digitou a frase {junto}.')
inverso = ''
for letra in range (len(junto) -1 , -1, -1): #ínicio (len(junto)), fim -1 e passos -1 e -1
     inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
     print(f'A frase: {frase_original} é um Palíndromo!')
else:
     print(f'A frase: {frase_original} NÃO é um Palíndromo! ')