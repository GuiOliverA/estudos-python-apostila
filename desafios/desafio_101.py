#Crie uma função chamada voto() que recebe o ano de nascimento e retorna se a pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO.
def voto(ano_nasc):
    from datetime import date     #importação local
    atual = date.today().year
    idade = atual - ano_nasc        
    if idade < 16:     #Se for menor que 16
        return f'Com {idade} anos: NÃO VOTA.'
    elif idade == 16 or idade == 17 or idade > 65: # 16, 17 e acima de 65
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'  
    

print(voto(2008))