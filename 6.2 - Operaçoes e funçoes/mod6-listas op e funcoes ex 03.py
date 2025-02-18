import random
from collections import Counter

# Gerar duas listas com 20 valores inteiros aleatórios entre 0 e 50
lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

# Criar a lista de interseção sem duplicatas
intersecao = sorted(set(lista1) & set(lista2))

# Contar a frequência dos elementos em cada lista
contagem_lista1 = Counter(lista1)
contagem_lista2 = Counter(lista2)

# Exibir os resultados
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista Interseção (ordenada):", intersecao)
print("\nFrequência dos elementos em Lista 1:")
for num, freq in contagem_lista1.items():
    print(f"{num}: {freq} vez(es)")

print("\nFrequência dos elementos em Lista 2:")
for num, freq in contagem_lista2.items():
    print(f"{num}: {freq} vez(es)")
