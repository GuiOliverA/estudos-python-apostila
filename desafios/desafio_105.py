#Crie uma função notas() que receba várias notas de alunos e retorne um dicionário com o total de notas, a maior, a menor, a média e a situação (opcional).
def notas_analisadas(*n, sit = False):
    """
    -- Analisa as notas e situações de vários alunos.
    :param lista: Uma lista de notas dos alunos.
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    dados = {}
    dados['total'] = len(n)
    dados['maior'] = max(n)
    dados['menor'] = min(n)
    dados['média'] = sum(n) / len(n)
    
    if sit:
        if dados['média'] >= 7:
            dados['situação'] = 'BOA'
        elif 5 <= dados['média'] < 7:
            dados['situação'] = 'RAZOÁVEL'
        else:
            dados['situação'] = 'RUIM'
    
    return dados


#Programa principal
valores_notas = []
quatd = int(input('Quantas notas deseja analisar?\n> '))
for i in range(quatd):
     n = float(input(f'Digite a {i+1}ª nota:\n> '))
     valores_notas.append(n)
     
situacao = str(input('Deseja analisar a situação da turma? [S/N]\n> ')).strip().upper()[0]
if situacao == 'S':
     sit = True
elif situacao == 'N':
     sit = False
else:
     print('Opção inválida, a situação da turma será analisada.')
     sit = True
resp = notas_analisadas(*valores_notas, sit=sit)
print(resp)