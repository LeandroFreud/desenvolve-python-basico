# Leitura de dados (entrada)
avaliacao = int(input("Digite a avaliação do filme (de 1 a 5): "))

# Processamento e Impressão de dados
if avaliacao == 5:
    print("Excelente!")
elif avaliacao == 4:
    print("Muito Bom!")
elif avaliacao == 3:
    print("Bom!")
elif avaliacao == 2:
    print("Regular.")
elif avaliacao == 1:
    print("Ruim.")
else:
    print("Avaliação inválida! Por favor, insira um número de 1 a 5.")
