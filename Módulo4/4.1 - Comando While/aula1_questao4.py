# Entrada
N = int(input("Digite o valor de N: "))  # lê o valor de N

# Processamento inicial
maior = 0

# Estrutura de decisão
while N > 0:  # enquanto N for maior que 0
    # Entrada
    X = int(input("Digite o valor de X: "))  # lê o valor de X
    
    # Estrutura de decisão
    if X > maior:  # se X for maior que o valor atual de maior
        maior = X  # atualiza o valor de maior
    
    # Processamento
    N = N - 1  # decrementa o valor de N

# Saída
print("O maior valor é:", maior)



