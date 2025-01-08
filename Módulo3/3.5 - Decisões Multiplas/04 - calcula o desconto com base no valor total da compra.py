# Solicita o valor total da compra
valor_total = float(input("Digite o valor total da compra: R$"))

# Inicializa as variáveis de desconto e valor final
desconto = 0.0

# Verifica o valor total e aplica o desconto correspondente
if valor_total >= 100:
    desconto = 20.0
elif valor_total >= 50:
    desconto = 10.0

# Calcula o valor final com desconto
valor_final = valor_total - (valor_total * desconto / 100)

# Exibe o resultado
print(f"Desconto aplicado: {desconto:.1f}%")
print(f"Valor final com desconto: R${valor_final:.2f}")


