# Leitura de dados (entrada)
# Solicitar a idade do usuário
idade = int(input("Digite sua idade: "))

# Solicitar se já jogou pelo menos 3 jogos
jogou_tres_jogos = input("Já jogou pelo menos 3 jogos de tabuleiro? (True/False) ").strip().capitalize() == "True"

# Solicitar quantas vezes venceu um jogo
vitorias = int(input("Quantos jogos já venceu? "))

# Processamento
# Verificar se o participante é apto para ingressar no clube
apto_para_ingressar = (16 <= idade <= 18) and jogou_tres_jogos and (vitorias >= 1)

# Impressão de dados (saída)
print(f"Apto para ingressar no clube de jogos de tabuleiro: {apto_para_ingressar}")
