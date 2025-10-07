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
    password = str(input("Informe sua senha: "))
    return password

def validate_inputs(campo, valor):

    if not valor or valor.strip() == "":
        raise ValueError(f"O campo '{campo}' não pode estar vazio.")
    
    return valor.strip()