
def boas_vindas(primeiro_nome, sobrenome):
    nome_completo = primeiro_nome + " " + sobrenome
    print("Bem-vinda, " + nome_completo + "!")

primeiro_nome = input("Digite seu primeiro nome: ")
sobrenome = input("Digite seu sobrenome: ")

boas_vindas(primeiro_nome, sobrenome)