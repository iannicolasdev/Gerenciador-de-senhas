import random
import string
import json

def gerar_senha(tamanho, caracteres):
    return ''.join(random.choices(caracteres, k=tamanho))

def solicitar_tamanho():
    while True:
        try:
            tamanho = int(input("Digite o tamanho da sua senha: "))
            if tamanho > 0:
                return tamanho
            else:
                print("O tamanho deve ser maior que zero.")
        except ValueError:
            print("Por favor, digite um número válido.")

def exibir_menu():
    print('''
----MENU----
1 - Números
2 - Letras
3 - Símbolos
4 - Todas
------------
''')
    while True:
        try:
            escolha = int(input("Escolha quais tipos de caracteres você deseja incluir na senha: "))
            if escolha in [1, 2, 3, 4]:
                return escolha
            else:
                print("Escolha inválida. Digite um número entre 1 e 4.")
        except ValueError:
            print("Por favor, digite um número válido.")

def escolha_caracteres(escolha):
    if escolha == 1:
        return string.digits
    elif escolha == 2:
        return string.ascii_letters
    elif escolha == 3:
        return string.punctuation
    elif escolha == 4:
        return string.digits + string.ascii_letters + string.punctuation

def verificar_forca(senha):
    pontos = 0
    if len(senha) >= 8:
        pontos += 1
    if any(char.isdigit() for char in senha):
        pontos += 1
    if any(char.islower() for char in senha):
        pontos += 1
    if any(char.isupper() for char in senha):
        pontos += 1
    if any(char in string.punctuation for char in senha):
        pontos += 1
    
    if pontos <= 2:
        return "Fraca"
    elif pontos == 3:
        return "Média"
    else:
        return "Forte"

def salvar_senha(senha, forca):
    import os
    from datetime import datetime

    nova_senha = {
        "senha": senha,
        "forca": forca,
        "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    if os.path.exists("senhas.json"):
        try:
            with open("senhas.json", "r") as arquivo:
                dados = json.load(arquivo)
        except json.JSONDecodeError:
            dados = {"senhas": []}  
    else:
        dados = {"senhas": []}  

    dados["senhas"].append(nova_senha)

    with open("senhas.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)

def visualizar_senhas():
    try:
        with open("senhas.json", "r") as arquivo:
            dados = json.load(arquivo)
            if "senhas" in dados and isinstance(dados["senhas"], list):
                print("\nSenhas armazenadas:")
                for registro in dados["senhas"]:
                    print(f"Senha: {registro['senha']}, Força: {registro['forca']}, Data: {registro['data']}")
            else:
                print("O arquivo não contém senhas válidas.")
    except FileNotFoundError:
        print("O arquivo senhas.json não foi encontrado!")
    except json.JSONDecodeError:
        print("O arquivo senhas.json está corrompido ou vazio.")

def main():
    print("Bem-vindo ao Gerador de Senhas!")
    tamanho = solicitar_tamanho()
    escolha = exibir_menu()
    caracteres = escolha_caracteres(escolha)
    senha = gerar_senha(tamanho, caracteres)
    forca = verificar_forca(senha)
    print("\nA senha gerada foi:", senha)
    print(f"A classificação de força da senha gerada é {forca}")

    salvar_senha(senha, forca)

    visualizar = int(input("Digite 1 para visualizar as senhas ou qualquer outra tecla para sair: "))
    if visualizar == 1:
        visualizar_senhas()

    input("\nAperte Enter para sair...")

if __name__ == "__main__":
    main()