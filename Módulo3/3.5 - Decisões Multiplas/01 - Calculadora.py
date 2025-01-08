   
n1 = float(input("Digite o primeiro operando: ")) 
operador = input("Digite o operador (+, -, /, *, **): ")  
n2 = float(input("Digite o segundo operando: "))  


if operador == "+":
    resultado = n1 + n2
    print(f"Resultado: {n1} + {n2} = {resultado}")
elif operador == "-":
    resultado = n1 - n2
    print(f"Resultado: {n1} - {n2} = {resultado}")
elif operador == "/":
    if n2 == 0:  
        print("Erro! Divisão por zero.")
    else:
        resultado = n1 / n2
        print(f"Resultado: {n1} / {n2} = {resultado}")
elif operador == "*":
    resultado = n1 * n2
    print(f"Resultado: {n1} * {n2} = {resultado}")
elif operador == "**":
    resultado = n1 ** n2
    print(f"Resultado: {n1} ** {n2} = {resultado}")
else:
    print("Erro! Operação inválida.")
        