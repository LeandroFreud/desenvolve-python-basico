# Solicita a pontuação do jogador
pontuacao = float(input("Digite a pontuação do jogador: "))

# Atribui a classificação com base nas condições
if pontuacao >= 90:
    classificacao = "Excelente"
elif pontuacao >= 80:
    classificacao = "Bom"
elif pontuacao >= 70:
    classificacao = "Regular"
else:
    classificacao = "Insatisfatório"

# Exibe a classificação
print(f"Classificação: {classificacao}")

