from experta import KnowledgeEngine, Fact, Rule, MATCH, TEST

# Sistema Especialista de busca

class Brinquedo(Fact):
    pass

class FiltroBusca(Fact):
    pass

class ResultadoBusca(Fact):
    pass

class FiltroDeBrinquedos(KnowledgeEngine):

    @Rule(
        Brinquedo(nome=MATCH.nome, categoria=MATCH.cat,
                  preco=MATCH.preco, estoque=MATCH.estoque),
        FiltroBusca(categoria=MATCH.cat,
                    preco_max=MATCH.preco_max,
                    apenas_em_estoque=MATCH.so_estoque),
        TEST(lambda preco, preco_max: preco <= preco_max),
        TEST(lambda estoque, so_estoque: (not so_estoque) or estoque > 0),
    )
    def brinquedo_corresponde_ao_filtro(self, nome, preco, estoque):
        self.declare(ResultadoBusca(nome=nome, preco=preco, estoque=estoque))

    @Rule(
        ResultadoBusca(nome=MATCH.nome, 
                       preco=MATCH.preco, 
                       estoque=MATCH.estoque)
    )
    def mostrar_resultado(self, nome, preco, estoque):
        print(f"- {nome:<22} R$ {preco:>8.2f}   (estoque: {estoque})")

catalogo = [
    # --- Automoveis ---
    {"nome": "carrinho de corrida em miniatura", "categoria": "automoveis", "preco": 29.90, "estoque": 3},
    {"nome": "caminhao de brinquedo",            "categoria": "automoveis", "preco": 45.50, "estoque": 8},
    {"nome": "pista de autorama",                "categoria": "automoveis", "preco": 189.90, "estoque": 2},
    {"nome": "carrinho de fricção",              "categoria": "automoveis", "preco": 19.90, "estoque": 15},
    {"nome": "kit de carrinhos sortidos",        "categoria": "automoveis", "preco": 69.90, "estoque": 6},
    {"nome": "trator de brinquedo",              "categoria": "automoveis", "preco": 39.90, "estoque": 4},

    # --- Bonecos ---
    {"nome": "boneco de acao articulado",  "categoria": "bonecos", "preco": 59.90, "estoque": 6},
    {"nome": "boneca com acessorios",      "categoria": "bonecos", "preco": 79.90, "estoque": 10},
    {"nome": "boneco super-heroi",         "categoria": "bonecos", "preco": 49.90, "estoque": 7},
    {"nome": "kit familia de bonecos",     "categoria": "bonecos", "preco": 99.90, "estoque": 3},
    {"nome": "boneco de vinil",            "categoria": "bonecos", "preco": 34.90, "estoque": 12},
    {"nome": "boneca bebe reborn",         "categoria": "bonecos", "preco": 249.90, "estoque": 1},

    # --- Quebra-Cabeca ---
    {"nome": "quebra-cabeca 100 pecas",          "categoria": "quebra_cabeca", "preco": 24.90, "estoque": 12},
    {"nome": "quebra-cabeca 500 pecas",          "categoria": "quebra_cabeca", "preco": 39.90, "estoque": 9},
    {"nome": "quebra-cabeca 1000 pecas",         "categoria": "quebra_cabeca", "preco": 54.90, "estoque": 5},
    {"nome": "quebra-cabeca 3D",                 "categoria": "quebra_cabeca", "preco": 69.90, "estoque": 4},
    {"nome": "quebra-cabeca infantil (pecas grandes)", "categoria": "quebra_cabeca", "preco": 29.90, "estoque": 14},
    {"nome": "quebra-cabeca magnetico",          "categoria": "quebra_cabeca", "preco": 44.90, "estoque": 6},

    # --- Esportes ---
    {"nome": "bola de futebol",           "categoria": "esportes", "preco": 49.90, "estoque": 9},
    {"nome": "kit de basquete infantil",  "categoria": "esportes", "preco": 89.90, "estoque": 4},
    {"nome": "raquetes de frescobol",     "categoria": "esportes", "preco": 34.90, "estoque": 11},
    {"nome": "patins infantil",           "categoria": "esportes", "preco": 129.90, "estoque": 3},
    {"nome": "kit de golfe infantil",     "categoria": "esportes", "preco": 74.90, "estoque": 2},
    {"nome": "bola de volei",             "categoria": "esportes", "preco": 44.90, "estoque": 7},

    # --- Criatividade ---
    {"nome": "massinha de modelar (Kit)",     "categoria": "criatividade", "preco": 19.90, "estoque": 0},
    {"nome": "kit de pintura infantil",       "categoria": "criatividade", "preco": 39.90, "estoque": 6},
    {"nome": "conjunto de giz de cera",       "categoria": "criatividade", "preco": 14.90, "estoque": 20},
    {"nome": "kit de colagem e recorte",      "categoria": "criatividade", "preco": 24.90, "estoque": 8},
    {"nome": "estojo de aquarela",            "categoria": "criatividade", "preco": 29.90, "estoque": 5},
    {"nome": "kit de argila para modelagem",  "categoria": "criatividade", "preco": 34.90, "estoque": 3},

    # --- Controle Remoto ---
    {"nome": "carrinho de controle remoto",        "categoria": "controle_remoto", "preco": 149.90, "estoque": 5},
    {"nome": "drone infantil",                     "categoria": "controle_remoto", "preco": 199.90, "estoque": 3},
    {"nome": "helicoptero de controle remoto",     "categoria": "controle_remoto", "preco": 179.90, "estoque": 2},
    {"nome": "barco de controle remoto",           "categoria": "controle_remoto", "preco": 159.90, "estoque": 4},
    {"nome": "robo de controle remoto",            "categoria": "controle_remoto", "preco": 229.90, "estoque": 1},
    {"nome": "monster truck de controle remoto",   "categoria": "controle_remoto", "preco": 189.90, "estoque": 6},

    # --- Blocos de Montar ---
    {"nome": "blocos de montar classico",       "categoria": "blocos_de_montar", "preco": 89.90, "estoque": 0},
    {"nome": "kit de blocos tematico espaco",   "categoria": "blocos_de_montar", "preco": 139.90, "estoque": 4},
    {"nome": "blocos de montar cidade",         "categoria": "blocos_de_montar", "preco": 119.90, "estoque": 2},
    {"nome": "blocos de encaixe para bebe",     "categoria": "blocos_de_montar", "preco": 49.90, "estoque": 10},
    {"nome": "kit de blocos castelo",           "categoria": "blocos_de_montar", "preco": 159.90, "estoque": 1},
    {"nome": "blocos de montar veiculos",       "categoria": "blocos_de_montar", "preco": 99.90, "estoque": 5},

    # --- Musica ---
    {"nome": "teclado infantil",                  "categoria": "musica", "preco": 119.90, "estoque": 10},
    {"nome": "violao infantil",                   "categoria": "musica", "preco": 89.90, "estoque": 5},
    {"nome": "bateria infantil",                  "categoria": "musica", "preco": 149.90, "estoque": 3},
    {"nome": "microfone com alto-falante",        "categoria": "musica", "preco": 69.90, "estoque": 8},
    {"nome": "xilofone de madeira",               "categoria": "musica", "preco": 34.90, "estoque": 12},
    {"nome": "kit de instrumentos de percussao",  "categoria": "musica", "preco": 79.90, "estoque": 4},

    # --- Jogos de Tabuleiro ---
    {"nome": "jogo de damas",                       "categoria": "jogos_de_tabuleiro", "preco": 24.90, "estoque": 2},
    {"nome": "jogo de xadrez",                      "categoria": "jogos_de_tabuleiro", "preco": 39.90, "estoque": 6},
    {"nome": "jogo da vida",                        "categoria": "jogos_de_tabuleiro", "preco": 89.90, "estoque": 3},
    {"nome": "jogo de detetive",                    "categoria": "jogos_de_tabuleiro", "preco": 79.90, "estoque": 4},
    {"nome": "jogo de cartas colorido",              "categoria": "jogos_de_tabuleiro", "preco": 29.90, "estoque": 9},
    {"nome": "jogo de estrategia territorial",       "categoria": "jogos_de_tabuleiro", "preco": 99.90, "estoque": 2},

    # --- Educativo ---
    {"nome": "kit de alfabetizacao",              "categoria": "educativo", "preco": 44.90, "estoque": 9},
    {"nome": "blocos de matematica",              "categoria": "educativo", "preco": 54.90, "estoque": 7},
    {"nome": "microscopio infantil",              "categoria": "educativo", "preco": 129.90, "estoque": 3},
    {"nome": "globo terrestre interativo",        "categoria": "educativo", "preco": 149.90, "estoque": 2},
    {"nome": "kit de experiencias cientificas",   "categoria": "educativo", "preco": 89.90, "estoque": 5},
    {"nome": "tablet educativo infantil",         "categoria": "educativo", "preco": 199.90, "estoque": 4},
]

# Opções do menu

def buscar(catalogo, categoria, preco_max, apenas_em_estoque):
    motor = FiltroDeBrinquedos()
    motor.reset()

    for brinquedo in catalogo:
        motor.declare(Brinquedo(**brinquedo))

    motor.declare(FiltroBusca(
        categoria=categoria,
        preco_max=preco_max,
        apenas_em_estoque=apenas_em_estoque
    ))
    motor.run()

def listar_categorias():
    return sorted(set(item["categoria"] for item in catalogo))

def menu_buscar():

    print("\nCategorias disponiveis:")
    for cat in listar_categorias():
        print(f" - {cat}")

    categoria = input("\nDigite a categoria: ").strip()

    while True:
        try:
            preco_max = float(input("Preço maximo: R$ "))
            break
        except ValueError:
            print("Digite um numero valido.")

    resposta = input("Somente em estoque? (s/n): ").strip().lower()
    apenas_em_estoque = resposta == "s"

    buscar(catalogo, categoria, preco_max, apenas_em_estoque)

def menu_adicionar():

    print("\n=== Adicionar novo brinquedo ===")
    nome = input("Nome: ").strip()
    categoria = input("Categoria: ").strip()

    while True:
        try:
            preco = float(input("Preco (R$): "))
            break
        except ValueError:
            print("Digite um numero valido (ex.: 35.42).")

    while True:
        try:
            estoque = int(input("Estoque: "))
            break
        except ValueError:
            print("Digite um numero inteiro valido (ex.: 11).")

    catalogo.append({"nome": nome, "categoria": categoria, "preco": preco, "estoque": estoque})
    print(f"\n'{nome}' adicionado ao catalogo com sucesso!")

def menu_remover():

    if not catalogo:
        print("\nO catalogo está vazio.")
        return

    print("\n=== Itens no catalogo ===")

    for i, item, in enumerate(catalogo, start=1):
        print(f"{i}. {item['nome']} ({item['categoria']}) - R$ {item['preco']:.2f}")

    while True:

        escolha = input("\nDigite o numero do item a remover (0 para cancelar): ").strip()
        if not escolha.isdigit():
            print("Digite um numero valido.")
            continue
        escolha = int(escolha)

        if escolha == 0:
            print("Escolha cancelada.")
            return
        if 1 <= escolha <= len(catalogo):
            removido = catalogo.pop(escolha - 1)
            print(f"\n'{removido['nome']}' removido do catalogo.")
            return
        print("Numero fora do intervalo.")

# Menu principal

def main():

    while True:
        print("Loja de brinquedos - MENU PRINCIPAL")
        print("1. Buscar brinquedos")
        print("2. Adicionar item ao catalogo")
        print("3. Retirar item do catalogo")
        print("4. Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        match opcao:
            case "1":
                menu_buscar()
            case "2":
                menu_adicionar()
            case "3":
                menu_remover()
            case "4":
                print("Encerrando o programa!")
                break
            case _:
                print("O valor inserido não é reconhecido. Tente novamente.")

if __name__ == "__main__":
    main()