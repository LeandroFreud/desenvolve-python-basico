# Solicitar informações ao usuário
genero = input("Digite seu gênero (M ou F): ").strip().upper()
idade = int(input("Digite sua idade: "))
tempo_servico = int(input("Digite seu tempo de serviço (em anos): "))

# Inicializar a variável de aposentadoria
pode_se_aposentar = False

# Verificar as condições de aposentadoria
if genero == "F":
    pode_se_aposentar = (idade > 60) or (tempo_servico >= 30) or (idade == 60 and tempo_servico >= 25)
elif genero == "M":
    pode_se_aposentar = (idade > 65) or (tempo_servico >= 30) or (idade == 60 and tempo_servico >= 25)

# Imprimir o resultado
print(pode_se_aposentar)
