from db import update_service, update_user, update_password
from password_utils import generate_password, manual_password

# Função para escolher o método de adicionar a senha
def choose_password_method():
    while True:
        print("""
        ---------Password---------
        1 - Adicionar nova senha
        2 - Gerar senha aleatória
        --------------------------
        """)

        choice = int(input("Informe sua escolha: "))

        if choice == 1:
            password = manual_password()
            return password
            
        elif choice == 2:
            length = int(input("Informe o tamanho da senhas: "))
            password = generate_password(length)
            return password

        else:
            print("Opção invalida, Tente novamente!\n")

# Função para escolher qual atualização o user deseja realizar
def choose_password_update(conn):
    print("""
    ---------Update---------
    1 - Atualizar serviço
    2 - Atualizar usuário
    3 - Atualizar senha
    0 - Sair
    ------------------------
    """)

    options = {
        1: update_service, 
        2: update_user,
        3: update_password
    }

    while True:
        try:
            choose = int(input("Informe sua escolha: "))

            func = options.get(choose)
            if func:
                func(conn)

            elif choose == 0:
                break
        
        except ValueError:
            print("Erro: Digite um valor válido")