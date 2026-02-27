try:   
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))          #Cada um aqui poderia ter um bloco try... (iria ficar um programa grande)
    r = a/b

#COM MAIS EXCEÇÕES:


except (ValueError, TypeError):   
    print('Tivemos um problema com os tipos de dados que você digitou...')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:  #Não digitou informações
    print('O usuário não informou os dados!')

except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')



else: 
    print(f'O resultado é {r:.1f}')



finally:  
    print('Volte sempre! Muito obrigado e Deus abençoe')
    
'''IMPORTANTE:

sempre testar seu programa pelo certo, depois os erros e, finalmente, tratá-los

'''