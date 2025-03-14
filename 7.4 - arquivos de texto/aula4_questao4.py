import random

def carrega_palavras():
    with open("gabarito_forca.txt", "r", encoding="utf-8") as file:
        palavras = file.read().splitlines()
    return random.choice(palavras)

def carrega_enforcado():
    with open("gabarito_enforcado.txt", "r", encoding="utf-8") as file:
        enforcados = file.read().splitlines()
    return enforcados

def imprime_enforcado(tentativas):
    estagios = carrega_enforcado()
    print(estagios[tentativas])

def jogar():
    palavra = carrega_palavras()
    letras_adivinhadas = []
    tentativas = 0
    max_tentativas = len(carrega_enforcado()) - 1
    
    print("Bem-vindo ao Jogo da Forca!")
    
    while tentativas < max_tentativas:
        print("\nPalavra:", ' '.join([letra if letra in letras_adivinhadas else '_' for letra in palavra]))
        letra = input("Adivinhe uma letra: ").lower()
        
        if letra in letras_adivinhadas:
            print("Você já tentou essa letra. Tente outra.")
            continue
        
        letras_adivinhadas.append(letra)
        
        if letra in palavra:
            print("Bom trabalho! Você acertou uma letra.")
        else:
            tentativas += 1
            print("Letra errada.")
            imprime_enforcado(tentativas)
        
        # Verifica se o jogador ganhou
        if all(letra in letras_adivinhadas for letra in palavra):
            print(f"Parabéns! Você adivinhou a palavra: {palavra}")
            break
            
    if tentativas == max_tentativas:
        print(f"Você perdeu! A palavra era: {palavra}")

if __name__ == "__main__":
    jogar()