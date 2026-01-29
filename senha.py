def tem_numero(senha):
    """Retorna True se a senha conter pelo menos um número"""
    return any(caractere.isdigit() for caractere in senha)
            
def tem_letra_maiuscula(senha):
    """Retorna True se a senha conter pelo menos uma letra maiúscula"""
    return any(caractere.isupper() for caractere in senha)


def validar_senha(senha):
    """valida a senha de acordo com os requisitos mínimos, se não for validada, aparece uma mensagem de erro"""
    if len(senha) < 8:
            return 'senha curta demais (mínimo 8 caracteres)'

    if not tem_numero(senha):
            return 'a senha precisa conter pelo menos um número'
            
    if not tem_letra_maiuscula(senha):
            return 'a senha precisa conter pelo menos uma letra maiúscula'

    return None

while True:
    senha = input('digite sua senha para cadastrar: ').strip()

    erro = validar_senha(senha)
    if erro:
        print(erro)
        continue 

    print('Sua senha foi cadastrada com sucesso, bem vindo!')
    break       


