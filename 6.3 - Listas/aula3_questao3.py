import random

# Gerar lista com 20 elementos entre -10 e 10
numeros = [random.randint(-10, 10) for _ in range(20)]

# Exibir lista original
print("Original:", numeros)

# Encontrar o intervalo com mais números negativos
maior_qtd_negativos = 0
indice_inicio = 0

for i in range(len(numeros) - 2):  # Percorre até o penúltimo conjunto de 3 elementos
    sublista = numeros[i:i+3]  # Pega um intervalo de 3 elementos
    qtd_negativos = sum(1 for num in sublista if num < 0)

    if qtd_negativos > maior_qtd_negativos:
        maior_qtd_negativos = qtd_negativos
        indice_inicio = i

# Deletar o intervalo encontrado
del numeros[indice_inicio:indice_inicio+3]

# Exibir lista editada
print("Editada:", numeros)
