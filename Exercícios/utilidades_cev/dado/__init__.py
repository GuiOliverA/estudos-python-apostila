def leia_dinheiro(txt):
    """Lê uma string (txt) e faz a mesma função do input, porém:

    Args:
        valido - verifica se o str dígito e se não tem espaços vazios
        além de evitar erros, caso o usuário digite ','. O programa troca o '.' por vírgula

    Returns:
        _type_: Retorna um erro se 'valido' for False e se for True o programa segue normalmente
    """    
    valido = False
    while not valido: #enquanto não for True (False)
        entrada = str(input(txt)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \'{entrada}\' é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)
    