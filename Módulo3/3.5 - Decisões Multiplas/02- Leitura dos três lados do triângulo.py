25# Leitura dos três lados do triângulo
lado1 = float(input("Digite o comprimento do lado 1: "))
lado2 = float(input("Digite o comprimento do lado 2: "))
lado3 = float(input("Digite o comprimento do lado 3: "))

# Verificar o tipo de triângulo com base nos lados
if lado1 == lado2 == lado3:
    print("Triângulo: Equilátero")
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("Triângulo: Isósceles")
else:
    print("Triângulo: Escaleno")
