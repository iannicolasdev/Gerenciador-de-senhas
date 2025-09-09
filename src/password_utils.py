import string as st

def generate_password(length):
    import random
    # Caracteres incluidos na geração de senhas
    caracteres = st.ascii_letters + st.digits + st.punctuation

    # Geração de senha aleatória
    password = (''.join(random.choices(caracteres, k=length)))
    return password

def manual_password():
    # Inserção de senha manualmente pelo usuário
    password = str(input("Digite sua senha: "))
    return password

def choose_password_method():
    while True:
        print("""
        ---------Password---------
        1 - Adicionar nova senha
        2 - Gerar senha aleatória
        --------------------------
        """)

        decisao = int(input("Digite sua escolha: "))

        if decisao == 1:
            password = manual_password()
            return password
            
        elif decisao == 2:
            length = int(input("Qual o tamanho da senhas?: "))
            password = generate_password(length)
            return password

        else:
            print("Opção invalida, Tente novamente!\n")