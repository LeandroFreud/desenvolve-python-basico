# Lê o número de jogos
N = int(input("Digite o número de jogos: "))

# Inicializa as variáveis para contagem de vitórias, empates e derrotas
vitorias = 0
empates = 0
derrotas = 0
pontuacao = 0

# Loop para processar os resultados dos jogos
for _ in range(N):
    # Lê os gols do Galo e do time adversário
    gols_cruzeiro = int(input("Digite o número de gols do Cruzeiro: "))
    gols_adversario = int(input("Digite o número de gols do adversário: "))
    
    # Determina o resultado do jogo
    if gols_cruzeiro > gols_adversario:
        vitorias += 1
        pontuacao += 3  # Vitória vale 3 pontos
    elif gols_cruzeiro == gols_adversario:
        empates += 1
        pontuacao += 1  # Empate vale 1 ponto
    else:
        derrotas += 1
        # Derrota vale 0 pontos 

# Exibe o resultado final
print(f"Vitórias: {vitorias}")
print(f"Empates: {empates}")
print(f"Derrotas: {derrotas}")
print(f"Pontuação: {pontuacao}")
