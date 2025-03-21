def eh_palindromo(frase):
    frase = ''.join(char for char in frase if char.isalnum()).lower()
    return frase == frase[::-1]

while True:
    frase = input('Digite uma frase (digite "fim" para encerrar): ')
    if frase.lower() == 'fim':
        break
    if eh_palindromo(frase):
        print(f'"{frase}" é palíndromo')
    else:
        print(f'"{frase}" não é palíndromo')
