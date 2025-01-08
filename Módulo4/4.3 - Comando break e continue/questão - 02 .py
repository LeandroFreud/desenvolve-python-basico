## Escreva e execute seu código aqui
# solicita o número ao usuário
numero = int(input("Digite um número: "))

#Inicializa a variavel soma
soma = 0

# Usa o comando fo para somar os números de 1 até o número informado
for i in range(1, número + 1):
    soma += i

# Exibe o resultado
print(f'A soma dos números de 1 a {numero} é {soma}')
