#Pergunte o valor a ser sacado (inteiro) e o programa informa quantas cédulas de cada valor serão entregues.
#Considere notas de R$ 50, R$ 20, R$ 10 e R$ 1.
print('=-='*10, 'BANCO', '=-='*10)
valor = int(input('Qual o valor de saque:\n> '))
montante = valor
cedula_atual = 50
total_cedulas = 0

while True:
    if montante >= cedula_atual:
        # Se o dinheiro que falta sacar ainda cabe a nota atual...
        montante -= cedula_atual
        total_cedulas += 1
    else:
        # Se não cabe mais a nota atual, eu mostro o que contei até agora
        if total_cedulas > 0:
            print(f'Total de {total_cedulas} cédulas de R${cedula_atual}')
        
        # Agora eu troco a nota atual para a próxima menor
        if cedula_atual == 50:
            cedula_atual = 20
        elif cedula_atual == 20:
            cedula_atual = 10
        elif cedula_atual == 10:
            cedula_atual = 1
        
        # IMPORTANTE: Reseto o contador para a nova nota
        total_cedulas = 0
        
        # Se o montante zerou, eu paro o programa
        if montante == 0:
            break
         

        