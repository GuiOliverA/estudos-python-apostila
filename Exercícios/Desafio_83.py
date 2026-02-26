#O usuário digita uma expressão matemática com parênteses. O programa deve analisar se a expressão é válida (parênteses abertos e fechados na ordem correta).
expres = str(input('Digite a expressão:\n> ')).strip()
pilha = []    #lista das strings digitadas em expres
for simb in expres:                                   #Para cada simb (contador/elemento) no var expres
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é válida.')
else:
    print('Sua expressão é inválida.')