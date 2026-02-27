#Faça um programa que leia o sexo de uma pessoa...
#mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Escolha uma opção:\n[M/F]\n→ ')).upper().strip()[0] #pegar somente a primeira letra da resposta
while sexo not in 'MF': #Enquanto NÃO ESTIVER EM
    sexo = str(input('Opção inválida, digite novamente.\n→ ')).upper().strip()[0] 
print(f'Sexo {sexo} registrado com sucesso!')

