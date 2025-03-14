# Lista de livros que você leu ou gostaria de ler
livros = [
    ("O Caçador de Pipas", "Khaled Hosseini", 2003, 368),
    ("Torto Arado", "Itamar Vieira Junior", 2019, 264),
    ("1984", "George Orwell", 1949, 328),
    ("Dom Casmurro", "Machado de Assis", 1899, 288),
    ("A Menina que Roubava Livros", "Markus Zusak", 2005, 552),
    ("O Senhor dos Anéis: A Sociedade do Anel", "J.R.R. Tolkien", 1954, 423),
    ("O Alquimista", "Paulo Coelho", 1988, 208),
    ("A Revolução dos Bichos", "George Orwell", 1945, 112),
    ("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 96),
    ("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, 223)
]

# Criando e escrevendo no arquivo CSV
with open("meus_livros.csv", "w") as file:
    # Escrevendo os títulos
    file.write("Título,Autor,Ano de publicação,Número de páginas\n")
    
    # Escrevendo as informações dos livros
    for livro in livros:
        file.write(",".join(map(str, livro)) + "\n")

print("Arquivo 'meus_livros.csv' criado com sucesso!")