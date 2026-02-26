#Crie a função leiaInt(), que funciona como o input(), mas só aceita números inteiros, validando a entrada do usuário.
def leiaint(number):
    while True:
        n = str(input(number)).strip()
        if n.isnumeric():
            return int(n)
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')

#programa principal
n = leiaint('Digite um número:\n> ')
print(f'Você acabou de digitar o número {n}')