# 1. Todos os números pares entre 20 e 50
pares_20_50 = [num for num in range(20, 51, 2)]

# 2. Os quadrados de todos os valores da lista [1,2,3,4,5,6,7,8,9]
quadrados = [num ** 2 for num in [1, 2, 3, 4, 5, 6, 7, 8, 9]]

# 3. Todos os números entre 1 e 100 que sejam divisíveis por 7
divisiveis_por_7 = [num for num in range(1, 101) if num % 7 == 0]

# 4. "par" ou "ímpar" para valores em range(0,30,3)
paridade = ["par" if num % 2 == 0 else "ímpar" for num in range(0, 30, 3)]

# Exibir os resultados
print("Números pares entre 20 e 50:", pares_20_50)
print("Quadrados de 1 a 9:", quadrados)
print("Números entre 1 e 100 divisíveis por 7:", divisiveis_por_7)
print("Paridade dos valores em range(0,30,3):", paridade)
