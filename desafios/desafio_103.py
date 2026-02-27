    #Crie uma função ficha() que receba o nome de um jogador e o número de gols. A função deve funcionar mesmo se os dados não forem informados (parâmetros opcionais).
def ficha(jog='<desconhecido>', gol=0):
    """
    -- Exibe a ficha de um jogador baseada nos gols marcados.
    :param jog: Nome do jogador (opcional).
    :param gol: Quantidade de gols (opcional).
    """
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


# --- Programa Principal ---
n = str(input("Nome do Jogador: ")).strip()
g = str(input("Número de Gols: ")).strip()

if g.isnumeric():    #Se 'g' for numérico, o 'g' vira int
    g = int(g)
else:
    g = 0  #Se não, 'g' é igual a 0

if n == '':
    ficha(gol=g) # Passa apenas o gol, o nome assume o padrão
else:
    ficha(n, g)
    