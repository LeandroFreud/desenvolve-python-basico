#Inicializa as variáveis
maior = None
menor = None

# Laço para leitura de valores
while True:
    # Lê um número do usuário
    numero = int(input())

    # Encerra o programa quando o número for 0
    if numero == 0:
        break

    # Atualiza o maior e menor valor
    if maior is None or numero > maior:
        maior = numero
    if menor is None or numero < menor:
        menor = numero

# Exibe o maior e menor valor
print(f'Maior: {maior}')
print(f'Menor: {menor}')
