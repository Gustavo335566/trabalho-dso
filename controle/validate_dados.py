

def valida_cpf(cpf):
    if len(cpf) == 11:
        return cpf
    return None


def valida_telefone(telefone):
    if len(telefone) >= 11 or len(telefone) <= 12:
        return telefone
    return None


def valida_sexo(sexo):
    if sexo.upper() in "MF":
        return sexo.upper()
    return None
