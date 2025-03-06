import re

def validador_senha(senha):
    # Verifica se a senha tem pelo menos 8 caracteres
    if len(senha) < 8:
        return False
    
    # Verifica se a senha contém pelo menos uma letra maiúscula e uma letra minúscula
    if not re.search("[a-z]", senha) or not re.search("[A-Z]", senha):
        return False
    
    # Verifica se a senha contém pelo menos um número
    if not re.search("[0-9]", senha):
        return False
    
    # Verifica se a senha contém pelo menos um caractere especial
    if not re.search("[^A-Za-z0-9]", senha):
        return False
    
    return True


# Exemplo de uso:
senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"

print(validador_senha(senha1))  # Saída esperada: True
print(validador_senha(senha2))  # Saída esperada: False
print(validador_senha(senha3))  # Saída esperada: False