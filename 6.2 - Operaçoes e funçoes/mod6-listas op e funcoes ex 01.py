import random

# Gerar lista com 20 valores inteiros aleatórios entre -100 e 100
valores = [random.randint(-100, 100) for _ in range(20)]

# Criar uma versão ordenada sem modificar a original
valores_ordenados = sorted(valores)

# Encontrar os índices do maior e menor valor
indice_maior = valores.index(max(valores))
indice_menor = valores.index(min(valores))

# Exibir os resultados
print("Lista ordenada:", valores_ordenados)
print("Lista original:", valores)
print("Índice do maior valor:", indice_maior)
print("Índice do menor valor:", indice_menor)
