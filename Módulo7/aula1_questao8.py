def valida_cpf(cpf):
    cpf = cpf.replace('.', '').replace('-', '')
    
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    
    cpf_calculado = cpf[:9]
    
    # Calcula o primeiro dígito verificador
    soma = sum(int(cpf_calculado[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    if resto < 2:
        cpf_calculado += '0'
    else:
        cpf_calculado += str(11 - resto)
    
    # Calcula o segundo dígito verificador
    soma = sum(int(cpf_calculado[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    if resto < 2:
        cpf_calculado += '0'
    else:
        cpf_calculado += str(11 - resto)
    
    return cpf_calculado == cpf

cpf = input("Digite o CPF (XXX.XXX.XXX-XX): ")
if valida_cpf(cpf):
    print("Válido")
else:
    print("Inválido")