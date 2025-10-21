from password_utils import validate_inputs

# Entrada de dados do usuário
def get_inputs():

    while True:
        try:
            username = str(input("Informe o username: "))
            validate_username = validate_inputs("username", username)

            service = str(input("Informe o serviço da senha: "))
            validate_service = validate_inputs("serviço", service)

            return validate_username, validate_service
        
        except ValueError as e:
            print(f"Erro: {e}\nTente novamente!")

# Exibição formatada da tabela no terminal
def list_table(resultado):
    print(f"| {'ID':>3} | {'Service':<20} | {'User':<20} | {'Password':<20} |")
    print("-" * 76)

    for linha in resultado:
        id_, service, user, password = linha

        print(f"| {id_:>3} | {service:<20} | {user:<20} | {password:<20} |")

# Interação para receber as novas alterações
def get_update_inputs(text_id, text):

    while True:
        try:
            id_ = int(input(f"Informe o ID {text_id} que quer atualizar: "))
            validate_id = validate_inputs(text, str(id_))

            change = str(input(f"Informe {text}: "))
            validate_change = validate_inputs(text, change)

            return int(validate_id), validate_change
        
        except ValueError:
            print(f"Erro: Os campo não pode ser vazio.")

# Função para deletar dados no banco
def get_delete_inputs():
    delete_id = int(input("Informe o ID da linha que quer excluir: "))

    if delete_id == "":
        print("Erro: O ID não foi informado")
        return None

    else:
        return delete_id