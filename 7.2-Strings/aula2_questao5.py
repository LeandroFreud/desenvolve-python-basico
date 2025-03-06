import random

def embaralhar_palavras(frase):
    palavras = frase.split()
    palavras_embaralhadas = []
    
    for palavra in palavras:
        if len(palavra) > 3:
            meio = list(palavra[1:-1])
            random.shuffle(meio)
            palavra_embaralhada = palavra[0] + ''.join(meio) + palavra[-1]
        else:
            palavra_embaralhada = palavra
        
        palavras_embaralhadas.append(palavra_embaralhada)
    
    return ' '.join(palavras_embaralhadas)


# Exemplo de uso:
frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)
# Possível saída: "Ptohyn é uma lignaugem de prarmoagãço"

