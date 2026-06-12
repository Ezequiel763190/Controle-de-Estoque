import json

def carregar_dados():
    try:
        with open("estoque.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"produtos": {}}


def salvar_dados(dados):
    with open("estoque.json", "w") as file:
        json.dump(dados, file)


def cadastrar_produto():
    dados = carregar_dados()

    produto = input("Digite o nome do produto: ")
    marca = input("Digite a marca do produto: ")
    quantidade = int(input(f"Digite a quantidade de {produto}: "))

    novo_id = str(len(dados["produtos"]) + 1)

    dados["produtos"][novo_id] = {
        "nome": produto,
        "marca": marca,
        "quantidade": quantidade
    }

    salvar_dados(dados)
    print("Produto cadastrado com sucesso!")



def listar_produtos():
    dados = carregar_dados()

    if not dados["produtos"]:
        print("Nenhum produto cadastrado.")
        return

    for id_produto, info in dados["produtos"].items():
        print(f"\nID: {id_produto}")
        print(f"Nome: {info['nome']}")
        print(f"Marca: {info['marca']}")
        print(f"Quantidade: {info['quantidade']}")



def remover_produto():
    dados = carregar_dados()

    id_produto = input("Digite o ID do produto: ")

    if id_produto in dados["produtos"]:
        del dados["produtos"][id_produto]
        salvar_dados(dados)
        print("Produto removido com sucesso!")
    else:
        print("Produto não encontrado.")



def adicionar_estoque():
    dados = carregar_dados()

    id_produto = input("Digite o ID do produto: ")
    quantidade = int(input("Quantidade para adicionar: "))

    if id_produto in dados["produtos"]:
        dados["produtos"][id_produto]["quantidade"] += quantidade
        salvar_dados(dados)
        print("Estoque atualizado!")
    else:
        print("Produto não encontrado.")


def remover_estoque():
    dados = carregar_dados()

    id_produto = input("Digite o ID do produto: ")
    quantidade = int(input("Quantidade para remover: "))

    if id_produto in dados["produtos"]:
        atual = dados["produtos"][id_produto]["quantidade"]

        if quantidade <= atual:
            dados["produtos"][id_produto]["quantidade"] -= quantidade
            salvar_dados(dados)
            print("Estoque atualizado!")
        else:
            print("Quantidade insuficiente.")
    else:
        print("Produto não encontrado.")



def estoque_baixo():
    dados = carregar_dados()

    print("\nProdutos com estoque baixo:")

    for id_produto, info in dados["produtos"].items():
        if info["quantidade"] <= 3:
            print(f"- {info['nome']} (Qtd: {info['quantidade']})")



while True:
    print("\n==============================")
    print("   ESTOQUE DO MERCADO")
    print("==============================")

    print("[1] Cadastrar produto")
    print("[2] Listar produtos")
    print("[3] Remover produto")
    print("[4] Adicionar estoque")
    print("[5] Remover estoque")
    print("[6] Estoque baixo")
    print("[0] Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        cadastrar_produto()

    elif opcao == "2":
        listar_produtos()

    elif opcao == "3":
        remover_produto()

    elif opcao == "4":
        adicionar_estoque()

    elif opcao == "5":
        remover_estoque()

    elif opcao == "6":
        estoque_baixo()

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")