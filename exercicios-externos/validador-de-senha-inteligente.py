def analisar_senha(password):
    """Analisa se a senha atende aos critérios de segurança."""

    criterios = {
        'tamanho_ok': len(password) >= 8,
        'tem_numero': False,
        'tem_maiuscula': False,
        'tem_minuscula': False
    }

    for caractere in password:
        if caractere.isdigit():
            criterios['tem_numero'] = True
        if caractere.isupper():
            criterios['tem_maiuscula'] = True
        if caractere.islower():
            criterios['tem_minuscula'] = True

    atendidos = sum(criterios.values())

    forte = atendidos == 4
    
    print(criterios)

    return forte, atendidos


# Programa principal
senha = str(input('''Crie uma senha que atenda as seguintes exigências:
- Pelo menos 8 caracteres
- Pelo menos 1 número
- Pelo menos 1 letra maiúscula
- Pelo menos 1 letra minúscula
> ''')).strip()

acesso, nota = analisar_senha(senha)

print(f'\nExigências atendidas: {nota}/4')

if acesso:
    print('Senha forte! Acesso liberado.')
else:
    print('Senha fraca. Tente novamente.')
