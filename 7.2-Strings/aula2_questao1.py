def formata_data(data):
    dias, meses, anos = data.split('/')
    meses_extenso = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 
                       'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    return f"{dias} de {meses_extenso[int(meses) - 1]} de {anos}"

data = input("Digite uma data de nascimento (dd/mm/aaaa): ")
print(f"Você nasceu em {formata_data(data)}.")