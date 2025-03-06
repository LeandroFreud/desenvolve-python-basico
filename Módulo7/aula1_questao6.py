def encontra_anagramas(frase, palavra_objetivo):
    frase = frase.lower()
    palavra_objetivo = palavra_objetivo.lower()
    anagramas = []
    
    for palavra in frase.split():
        if sorted(palavra) == sorted(palavra_objetivo):
            anagramas.append(palavra)
    
    return anagramas

frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")

anagramas = encontra_anagramas(frase, palavra_objetivo)

print("Anagramas:", anagramas)