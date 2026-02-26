#Ler nome, idade e sexo de 4 pessoas. Mostrar: a média de idade, o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
soma_idade = 0
maior_idade_homem = 0
maior_idade_mulher = 0
nome_velho = ''
menosM20 = 0

for p in range (1,5): #Para, em, intervalo. Ínicio, Fim.    
    print(f'=-= {p}ª Pessoa =-=')
    nome = str(input('Nome:\n> ')).strip() #tirar espaços
    idade = int(input('Idade:\n>' ))
    sexo = str(input('Sexo [M/F]:\n> ')).strip().lower() #tirar espaço

    soma_idade += idade #soma_idade = soma_idade + idade
    
    if sexo == 'm': # Se for a primeira pessoa E for homem
        if p == 1 or idade > maior_idade_homem:
            maior_idade_homem = idade # Se for homem e mais velho que o recorde
            nome_velhoH = nome
    elif sexo == 'f': 
        if p == 1 or idade > maior_idade_mulher:
            maior_idade_mulher= idade
            nome_velhoM = nome
        if idade < 20:
            menosM20 =+ 1

media_idade= soma_idade/4
print(f'A média de idade das pessoas acima é de {media_idade:.1f} anos.')
print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_velhoH}.')
print(f'A mulher mais velha tem {maior_idade_mulher} anos e se chama {nome_velhoM}.')
print(f'Ao todo {menosM20} mulher(es) tem menos de 20 anos.')

    

    