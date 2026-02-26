#Leia idade e sexo de várias pessoas. A cada pessoa, pergunte se quer continuar. 
#No fim mostre: quantas pessoas têm mais de 18 anos, quantos homens e quantas mulheres têm menos de 20 anos.
totalp18 = 0
totalM = 0 #Masculino
totalF20 = 0 #Feminino
while True:
    print('---'*10)
    idade = int(input('Digite a idade\n> ')) 
    print('---'*10)
    sexo = str(input('Digite o sexo [M/F]\n> '))[0].strip().upper()
    print('---'*10)

    if sexo in 'MF': #Verificação do desafio proposto
        if idade >= 18 and sexo in 'MF':
            totalp18 += 1
        if sexo in 'M': 
            totalM += 1 
        if idade < 20 and sexo in 'F': 
            totalF20 += 1
    else:
        print('ERRO, digite o sexo correto e tente novamente...\n ')
    sim_nao = str(input('Deseja continuar? [Sim/Não]\n> '))[0].strip().upper()
    if sim_nao in 'S':
        print('Continuando...\n ')

    else:
        print(' ')  
        break

print('---'*10)
print(f'Total de pessoas com +18: {totalp18}\nTotal de homens registrados: {totalM}\nTotal de mulheres com menos de 20 anos: {totalF20}')
print('---'*10)