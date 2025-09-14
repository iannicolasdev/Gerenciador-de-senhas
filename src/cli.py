def get_inputs():
    # Entrada de dados do usuário
    username = str(input("Qual o seu nome?: "))
    service = str(input("Qual o serviço da senha?: "))
    return username, service

def list_table(resultado):
    print(f"| {'ID':>3} | {'Service':<20} | {'User':<20} | {'Password':<20} |")
    print("-" * 76)

    for linha in resultado:
        id_, service, user, password = linha

        print(f"| {id_:>3} | {service:<20} | {user:<20} | {password:<20} |")