
def formata_numero_celular(numero):
    if len(numero) == 8:
        return f"9{numero[:4]}-{numero[4:]}"
    elif len(numero) == 9 and numero[0] == "9":
        return f"{numero[:5]}-{numero[5:]}"
    else:
        return "Número inválido"

numero = input("Digite o número: ")
numero_completo = formata_numero_celular(numero)

print("Número completo:", numero_completo)