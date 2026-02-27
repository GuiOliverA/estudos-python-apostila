#Faça um programa que tenha uma função chamada escreva(), 
#que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável. Ex: escreva('Olá, Mundo!') deve gerar linhas de traços no tamanho exato da frase.

def escreva(msg):
    print('='* len(msg))
    print(frase)
    print('='* len(msg))

frase = str(input('Escreva uma palavra/frase:\n> ')).strip()
print('')
escreva(frase)