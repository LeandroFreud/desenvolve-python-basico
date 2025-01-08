# Inicializa o produto
produto = 1
# Variável para controlar se algum número positivo foi digitado
encontrou_positivo = False

# Laço para leitura de valores
while True:
    # Lê um número do usuário
    numero = int(input())

    # Encerra o programa quando o número for 0
    if numero == 0:
        break

    # Se o número for positivo, atualiza o produto
    if numero > 0:
        produto *= numero
        encontrou_positivo = True

# Exibe o resultado
if encontrou_positivo:
    print(f'Produto: {produto}')
else:
    print('Produto: 0')
