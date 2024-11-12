# Solicitar a distância da entrega em quilômetros
distancia = float(input("Digite a distância da entrega (em km): "))

# Solicitar o peso do pacote em quilogramas
peso = float(input("Digite o peso do pacote (em kg): "))

# Definir a tarifa por quilograma com base na distância
if distancia <= 100:
    tarifa_por_kg = 1.00
elif 101 <= distancia <= 300:
    tarifa_por_kg = 1.50
else:
    tarifa_por_kg = 2.00

# Calcular o custo base do frete
custo_frete = tarifa_por_kg * peso

# Adicionar taxa adicional para pacotes com peso superior a 10 kg
if peso > 10:
    custo_frete += 10

# Imprimir o valor total do frete
print(f"O valor do frete é: R${custo_frete:.2f}")
