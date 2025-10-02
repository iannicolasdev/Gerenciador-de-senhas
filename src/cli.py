# Entrada de dados do usuário
def get_inputs():
    username = str(input("Informe o username: "))

    if username == "":
        print("Erro: O username não pode estar vazio")
        return None, None
    
    service = str(input("Informe o serviço da senha: "))

    if service == "":
        print("Erro: O serviço não pode estar vazio")
        return None, None

    else:
        return username, service

# Exibição formatada da tabela no terminal
def list_table(resultado):
    print(f"| {'ID':>3} | {'Service':<20} | {'User':<20} | {'Password':<20} |")
    print("-" * 76)

    for linha in resultado:
        id_, service, user, password = linha

        print(f"| {id_:>3} | {service:<20} | {user:<20} | {password:<20} |")

# Interação para receber as novas alterações
def get_update_inputs(text_id, text):
    id_ = int(input(f"Informe o ID {text_id} que quer atualizar: "))

    if id_ == "":
        print("Erro: O ID não foi informado")
        return None, None

    change = str(input(f"Informe {text}: "))

    if change == "":
        print("Erro: O a alteração não pode estar vazia")
        return None, None

    else:
        return id_, change

def get_delete_inputs():
    delete_id = int(input("Informe o ID da linha que quer excluir: "))

    if delete_id == "":
        print("Erro: O ID não foi informado")

    else:
        return delete_id