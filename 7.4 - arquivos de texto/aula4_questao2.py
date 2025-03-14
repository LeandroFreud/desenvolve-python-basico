import re

# Lê a frase do arquivo "frase.txt"
with open("frase.txt", "r") as arquivo:
    frase = arquivo.read()

# Remove espaços em branco e caracteres não alfabéticos
# Usa expressão regular para encontrar palavras
palavras = re.findall(r"[a-zA-ZÀ-ÿ]+", frase)

# Salva as palavras no arquivo "palavras.txt"
with open("palavras.txt", "w") as novo_arquivo:
    for palavra in palavras:
        novo_arquivo.write(palavra + "\n")

# Lê e imprime o conteúdo do arquivo "palavras.txt"
with open("palavras.txt", "r") as novo_arquivo:
    conteudo = novo_arquivo.read()
    print(conteudo)