# Solicita os números do usuário até que tenha pelo menos 4 valores
numeros = []
while len(numeros) < 4:
    entrada = input("Digite um número inteiro (ou pressione Enter para finalizar): ")
    if entrada == "":
        if len(numeros) >= 4:
            break
        else:
            print("Digite pelo menos 4 números antes de finalizar.")
            continue
    try:
        numeros.append(int(entrada))
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

# Exibir as diferentes formas de fatiamento
print("\nLista original:", numeros)
print("Os 3 primeiros elementos:", numeros[:3])
print("Os 2 últimos elementos:", numeros[-2:])
print("Lista invertida:", numeros[::-1])
print("Elementos de índice par:", numeros[::2])
print("Elementos de índice ímpar:", numeros[1::2])
