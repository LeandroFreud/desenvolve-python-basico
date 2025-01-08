# Inicializa a variável para a soma dos números
soma = 0

# Solicita ao usuário que digite 10 números
print("Digite 10 números positivos:")
for i in range(10):
    valor = int(input())  # Lê o número digitado pelo usuário
    # Verifica se o número é positivo, se não for, repete a solicitação
    while valor <= 0:
        print("Por favor, digite um número positivo.")
        valor = int(input())
    soma += valor  # Adiciona o valor à soma

# Calcula a média
media = soma / 10

# Exibe a média com duas casas decimais
print(f'A média dos valores digitados é {media:.2f}')