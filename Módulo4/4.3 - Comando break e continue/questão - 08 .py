# Inicializa o resultado com o primeiro número
resultado = int(input())

# Laço para leitura de operadores e números subsequentes
while True:
    # Lê o operador (+ ou -)
    operador = input().strip()
    
    # Se o operador for "Fim", encerra o programa
    if operador == "Fim":
        break
    
    # Lê o próximo número
    numero = int(input())
    
    # Realiza a operação dependendo do operador
    if operador == "+":
        resultado += numero
    elif operador == "-":
        resultado -= numero

# Exibe o resultado final
print(resultado)