# Leitura de dados (entrada)
def calcular_total():
    total = 0.0
    
    for i in range(1, 4):
        nome = input(f'Digite o nome do produto {i}: ')
        preco_unitario = float(input(f'Digite o preço unitário do produto {i}: '))
        quantidade = int(input(f'Digite a quantidade do produto {i}: '))
        
        total += preco_unitario * quantidade
    
    # Processamento
    print(f'Total: R${total:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'))

# Impressão de dados (saída)
calcular_total()


