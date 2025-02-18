# Solicita uma frase do usuário
frase = input("Digite uma frase: ")

# Lista de vogais
vogais = sorted([char for char in frase if char.lower() in "aeiou"])

# Lista de consoantes (removendo espaços)
consoantes = [char for char in frase if char.isalpha() and char.lower() not in "aeiou"]

# Exibir os resultados
print("Vogais:", vogais)
print("Consoantes:", consoantes)
