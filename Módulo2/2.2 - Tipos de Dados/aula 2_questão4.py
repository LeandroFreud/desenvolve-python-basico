juros = 1.01
saldo = 500.0

# Cálculo dos rendimentos em três meses
for _ in range(3):
    saldo *= juros

print("Após 3 meses meu novo saldo é")
print(saldo)
