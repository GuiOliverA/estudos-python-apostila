try:   #Tente executar o código abaixo:
    #Até aqui está tudo certo, até tentarmos dividir por zero: ZeroDivisionError
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except Exception as erro:   #Se der problema: // Exception com váriavel, para mostrar o tipo de erro
    print(f'Infelizmente tivemos um problema... 😥\nERRO: {erro.__class__}')

else:  #Se o try (tentativa) deu certo...
    print(f'O resultado é {r:.1f}')

#Não temos mais mensagem de erro. TRATAMENTO DE ERROS

finally:  #Acontece se deu certo ou erro (certo/falha)
    print('Volte sempre! Muito obrigado e Deus abençoe')
    


    
    '''RESUMO:
try > Tente excecutar esse código abaixo:
except > Se der erro, excecute outro código (opcional--)

except Exception as var > Vai dar um nome para o erro e mostrar a classe ou afins (opcional--)

else > Se o try (tentativa) der certo, exceute este código x (opcional--)

finally > Execute este código, dando certo ou errado    
    
    
    e mais... Podemos ter vários except: TypeError / OSError / ValueError .....    

   
    '''