def intercalar_listas(lista1, lista2):
    intercalada = []
    menor_tamanho = min(len(lista1), len(lista2))

    # Intercalar elementos até o fim da menor lista
    for i in range(menor_tamanho):
        intercalada.append(lista1[i])
        intercalada.append(lista2[i])

    # Adicionar os elementos restantes da maior lista
    intercalada.extend(lista1[menor_tamanho:])
    intercalada.extend(lista2[menor_tamanho:])

    return intercalada

# Entrada da primeira lista
n1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = [int(input(f"Digite o {i+1}º elemento da lista 1: ")) for i in range(n1)]

# Entrada da segunda lista
n2 = int(input("Digite a quantidade de elementos da lista 2: "))
lista2 = [int(input(f"Digite o {i+1}º elemento da lista 2: ")) for i in range(n2)]

# Criar lista intercalada
lista_intercalada = intercalar_listas(lista1, lista2)

# Exibir resultado
print("Lista intercalada:", " ".join(map(str, lista_intercalada)))
