# Leitura de dados (entrada)
fahrenheit = int(input("Digite a temperatura em F: "))


# Processamento
celsius = (fahrenheit - 32) * 5 / 9

# Impressão de dados (saída)
print(f"{fahrenheit} graus Fahrenheit sáo {int(celsius)} graus Celsius.")