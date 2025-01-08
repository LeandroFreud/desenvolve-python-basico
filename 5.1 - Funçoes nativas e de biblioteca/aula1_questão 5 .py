import emoji

# lista de emojis disponíveis
def exibir_emoji_sugestoes():
    emojis = {
        ":smile:": "😀",
        ":heart:": "❤️",
        ":thumbs_up:": "👍",
        ":star:": "⭐",
        ":dog:": "🐶",
        ":cat:": "🐱",
        ":sunny:": "🌞",
        ":fire:": "🔥",
        ":sunglasses:": "😎",
        ":thinking:": "🤔"
    }
    print("Emojis disponíveis:")
    for texto, emoji_char in emojis.items():
        print(f"{texto}: {emoji_char}")


def main():
    
    exibir_emoji_sugestoes()

    
    frase_codificada = input("\nDigite uma frase codificada com emojis (ex: 'Eu gosto de :dog: e :heart:'):\n")

    
    frase_decodificada = emoji.emojize(frase_codificada)


    print("\nFrase decodificada com emojis:")
    print(frase_decodificada)


if __name__ == "__main__":
    main()

