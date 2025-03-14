import re

# Abre o arquivo para leitura
try:
    with open("estomago.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    # Verifica se o arquivo está vazio
    if not linhas:
        print("O arquivo está vazio.")
    else:
        # Imprime as primeiras 25 linhas
        print("Primeiras 25 linhas:")
        for linha in linhas[:25]:  # Usa fatiamento para simplificar
            print(linha.strip())

        # Número total de linhas no arquivo
        numero_de_linhas = len(linhas)
        print(f"\nNúmero total de linhas: {numero_de_linhas}")

        # A linha com maior número de caracteres
        linha_maior = max(linhas, key=len).strip()
        print(f"\nLinha com maior número de caracteres:\n{linha_maior}")

        # Número de menções aos nomes "Nonato" e "Íria"
        texto_completo = " ".join(linhas)  # Usa espaço entre as linhas para evitar junção incorreta de palavras
        menções_nonato = len(re.findall(r'\bNonato\b', texto_completo, re.IGNORECASE))
        menções_iria = len(re.findall(r'\bÍria\b', texto_completo, re.IGNORECASE))

        # Total de menções
        total_menções = menções_nonato + menções_iria
        print(f"\nNúmero total de menções a 'Nonato' e 'Íria': {total_menções}")
except FileNotFoundError:
    print("Erro: O arquivo 'estomago.txt' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

