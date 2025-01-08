# Banco de dados com os padrões de íris dos usuários
usuarios = {
    1: (100, 200, 300),
    2: (982, 653, 324),
    3: (111, 222, 333),
    4: (444, 555, 666)
}

# Margem de erro permitida
margem_erro = 5

# Função para verificar se a leitura está dentro da margem de erro
def autenticar(padrao_usuario, leitura_usuario):
    for i in range(3):  # Verifica se todos os atributos estão dentro da margem de erro
        if abs(padrao_usuario[i] - leitura_usuario[i]) > margem_erro:
            return False  # Se algum atributo estiver fora da margem de erro, falha a autenticação
    return True  # Se todos os atributos estiverem dentro da margem de erro, autenticação é bem-sucedida

# Solicita a leitura do padrão de íris para autenticação
print("Insira o padrão de íris para autenticação.")
atributo1 = int(input("Atributo 1: "))
atributo2 = int(input("Atributo 2: "))
atributo3 = int(input("Atributo 3: "))

# Cria uma tupla com os valores inseridos
leitura_usuario = (atributo1, atributo2, atributo3)

# Verifica se a leitura corresponde a algum usuário cadastrado
autenticado = False
for usuario_id, padrao_usuario in usuarios.items():
    if autenticar(padrao_usuario, leitura_usuario):
        print(f"Autenticação bem-sucedida!")
        print(f"Usuário: {usuario_id}")
        autenticado = True
        break  # Sai do loop assim que o usuário for autenticado

# Caso nenhum usuário tenha sido autenticado
if not autenticado:
    print("Autenticação falhou!")




