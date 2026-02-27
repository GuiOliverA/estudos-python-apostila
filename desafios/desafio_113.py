from Interno import cores

def leia_int(txt):
    
    while True:
        try:
            num = int(input(txt))
        
        except (ValueError, TypeError):
            print(cores.vermelho('ERRO: por favor, digite um número inteiro válido.'))
            continue # Volta para o início do while
        
        except KeyboardInterrupt:
            print(cores.negrito_vermelho_cinza('Usuário preferiu não digitar um número...'))
            return 0
        else:
            # Se não deu erro nenhum, retorna o número e sai do loop
            return num

def leia_float(txt):
    while True:
        try:
            num = float(input(txt).replace(',', '.')) # Aceita vírgula e converte para o float
        
        except (ValueError, TypeError):
            print(cores.vermelho('ERRO: por favor, digite um número real válido.'))
            continue
        
        except KeyboardInterrupt:
            print(cores.negrito_vermelho_cinza('Usuário preferiu não digitar um número...'))
            return 0
        
        else:
            #Se não der erro nenhum, retorna o número e sai do loop infinito
            return num


# Programa Principal
inteiro = leia_int('Digite um número inteiro (int):\n> ')
real = leia_float('Digite um número real (float):\n> ')        
print(f'Número inteiro digitado: {inteiro}\nNúmero real digitado: {real}')