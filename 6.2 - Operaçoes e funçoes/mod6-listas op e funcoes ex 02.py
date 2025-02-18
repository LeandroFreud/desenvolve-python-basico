import random

# Gerar um número aleatório entre 5 e 20 para definir a quantidade de elementos
num_elementos = random.randint(5, 20)

# Gerar uma lista com 'num_elementos' valores entre 1 e 10
elementos = [random.randint(1, 10) for _ in range(num_elementos)]

# Calcular a soma e a média dos valores da lista
soma_valores = sum(elementos)
media_valores = soma_valores / num_elementos

# Exibir os resultados
print("Lista de elementos:", elementos)
print("Soma dos valores:", soma_valores)
print("Média dos valores:", round(media_valores, 2))
