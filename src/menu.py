from db import update_service, update_user, update_password

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
        choose = int(input("Digite sua escolha: "))

        func = options.get(choose)
        if func:
            func(conn)

        elif choose == 0:
            break

        else:
            print("Opção inválida!")