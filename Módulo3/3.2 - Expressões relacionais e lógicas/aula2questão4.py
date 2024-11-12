# Leitura de dados (entrada)
# Solicitar a classe de personagem
classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ").strip().lower()

# Solicitar os pontos de força e magia
forca = int(input("Digite os pontos de força (de 1 a 20): "))
magia = int(input("Digite os pontos de magia (de 1 a 20): "))

# Processamento
# Inicializar a variável de consistência
pontos_consistentes = False

# Validar os pontos de atributo com base na classe escolhida
if classe == "guerreiro":
    pontos_consistentes = forca >= 15 and magia <= 10
elif classe == "mago":
    pontos_consistentes = forca <= 10 and magia >= 15
elif classe == "arqueiro":
    pontos_consistentes = forca > 5 and magia > 5 and forca <= 15 and magia <= 15

# Impressão de dados
print(f"Pontos de atributo consistentes com a classe escolhida: {pontos_consistentes}")
