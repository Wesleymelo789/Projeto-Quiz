usuarios = []

def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o e-mail do usuário: ")
    usuarios.append({"nome": nome, "email": email})
    print("Usuário cadastrado com sucesso!\n")

def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.\n")
        return
    for i, usuario in enumerate(usuarios, 1):
        print(f"{i}. {usuario['nome']} - {usuario['email']}")
    print()

def buscar_usuario():
    termo = input("Digite o nome ou e-mail a buscar: ").lower()
    encontrados = [u for u in usuarios if termo in u["nome"].lower() or termo in u["email"].lower()]
    if not encontrados:
        print("Nenhum usuário encontrado.\n")
    else:
        for u in encontrados:
            print(f"{u['nome']} - {u['email']}")
    print()