

def substitui_vogais(frase):
    vogais = 'aeiouAEIOU'
    return ''.join('*' if char in vogais else char for char in frase)

frase = input("Digite uma frase: ")
frase_modificada = substitui_vogais(frase)

print("Frase modificada:", frase_modificada)