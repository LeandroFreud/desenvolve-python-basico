# Entrada de dados
n = int(input()) # quantidade de experimentos

# Inicializar as variaveis resultado e controle
cont = 0
soma_sapo, soma_rato, soma_coelho = 0, 0, 0

# Iterações
while cont < n:
    quantia = int(input())
    tipo = input()

    if tipo == 'S': 
        soma_sapo += quantia
    elif tipo == 'R':
        soma_rato += quantia
    elif tipo == 'C':
        soma_coelho += quantia

    cont += 1


print("Totalde cobaias: ", soma_sapo+soma_rato+soma_coelho)
print("Totalde sapos: ",   soma_sapo)
print("Totalde ratos: ",   soma_rato)
print("Totalde coelhos: ", soma_coelho)