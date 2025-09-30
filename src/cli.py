# Entrada de dados do usuário
def get_inputs():
    username = str(input("Qual o seu nome?: "))
    service = str(input("Qual o serviço da senha?: "))
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

    change = str(input(f"Digite {text}: "))

    return id_, change

def get_delete_inputs():
    delete_id = int(input("Informe o ID da linha que quer excluir: "))

    return delete_id