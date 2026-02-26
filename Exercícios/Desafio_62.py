#Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
contador= 1
total = 0
mais = 10 # Começamos com 10 termos

while mais != 0:
    total += mais # Acumula quantos termos o programa já mostrou ou vai mostrar
    while contador <= total:
        print(f'{termo} → ', end='')
        termo += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))

print(f'Progressão finalizada com {total} termos mostrados.')
               
                             
