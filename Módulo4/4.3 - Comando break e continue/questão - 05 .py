# Lê os valores de N (linhas) e M (colunas)
N = int(input())
M = int(input())

# Imprime o cabeçalho com os números das colunas
print(" ", end="")  # Espaço antes dos números
for col in range(1, M + 1):
    print(col, end=" ")
print()  # Quebra de linha após o cabeçalho

# Imprime as linhas do campo de batalha
for linha in range(1, N + 1):
    print(linha, end=" ")  # Cabeçalho das linhas
    for col in range(1, M + 1):
        print("/", end=" ")  # Representação das posições jogáveis
    print()  # Quebra de linha após cada linha

