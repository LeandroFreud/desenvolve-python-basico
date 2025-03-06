import random

def encrypt(nomes):
    chave_aleatoria = random.randint(1, 10)
    nomes_cript = []
    
    for nome in nomes:
        nome_cript = ""
        for char in nome:
            ascii_char = ord(char)
            if 33 <= ascii_char <= 126:
                ascii_char_cript = (ascii_char - 33 + chave_aleatoria) % 94 + 33
                nome_cript += chr(ascii_char_cript)
            else:
                nome_cript += char
        nomes_cript.append(nome_cript)
    
    return nomes_cript, chave_aleatoria

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_cript, chave_aleatoria = encrypt(nomes)

print("Nomes criptografados:", nomes_cript)
print("Chave de criptografia:", chave_aleatoria)