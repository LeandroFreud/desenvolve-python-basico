def conta_espaços(frase):
    return frase.count(" ")

frase = input("Digite a frase: ")
espaços = conta_espaços(frase)

print("Espaços em branco:", espaços)