base_conhecimento_jogadores = [
    ("portugal", "al_nassr", "atacante", 38, "cristiano_ronaldo"),
    ("argentina", "inter_miami", "atacante", 36, "lionel_messi"),
    ("brasil", "al_hilal", "atacante", 31, "neymar_jr"),
    ("franca", "psg", "atacante", 24, "kylian_mbappe"),
    ("portugal", "barcelona", "atacante", 23, "joao_felix"),
    ("belgica", "manchester_city", "atacante", 32, "kevin_de_bruyne"),
    ("italia", "psg", "goleiro", 24, "donnarumma"),
    ("brasil", "liverpool", "goleiro", 29, "alisson_becker"),
    ("alemanha", "barcelona", "goleiro", 30, "ter_stegen"),
    ("brasil", "manchester_city", "goleiro", 28, "ederson_moraes"),
    ("espanha", "real_madrid", "goleiro", 27, "kepa"),
    ("argentina", "aston_villa", "goleiro", 29, "emiliano_martinez"),
    ("holanda", "liverpool", "defensor", 30, "virgil_van_dijk"),
    ("portugal", "manchester_city", "defensor", 25, "ruben_dias"),
    ("franca", "manchester_united", "defensor", 29, "raphael_varane"),
    ("escocia", "liverpool", "defensor", 28, "andrew_robertson"),
    ("alemanha", "bayern_de_munique", "defensor", 27, "joshua_kimmich"),
    ("franca", "psg", "defensor", 26, "presnel_kimpembe"),
    ("brasil", "arsenal", "defensor", 25, "gabriel_magalhaes"),
    ("brasil", "chelsea", "defensor", 39, "thiago_silva")
]

base_conhecimento_formacao = [
    ("4-4-2", "Uma formação clássica com quatro defensores, quatro meio-campistas e dois avançados. Oferece um equilíbrio entre defesa e ataque."),
    ("4-3-3", "Uma formação com quatro defensores, três meio-campistas e três avançados. É uma formação ofensiva que foca em pressionar o adversário e marcar gols."),
    ("4-2-3-1", "Uma formação com quatro defensores, dois meio-campistas defensivos, três meio-campistas ofensivos e um atacante. Busca equilíbrio entre defesa e ataque, com ênfase no meio-campo."),
    ("5-4-1", "Uma formação com cinco defensores, quatro meio-campistas e um atacante. É uma formação defensiva que visa conter o adversário."),
    ("3-5-2", "Uma formação com três defensores, cinco meio-campistas e dois atacantes. Proporciona um meio-campo sólido e capacidade de ataque pelo centro.")
]

base_conhecimento_treinador = [
    ("al_nassr", "luis_castro"),
    ("al_hilal", "leonardo_jardim"),
    ("barcelona", "xavi_hernandez"),
    ("psg", "mauricio_pochettino"),
    ("manchester_city", "pep_guardiola"),
    ("inter_miami", "phil_neville"),
    ("real_madrid", "carlo_ancelotti"),
    ("liverpool", "jurgen_klopp"),
    ("manchester_united", "ole_gunnar_solskjaer"),
    ("aston_villa", "steven_gerard"),
    ("bayern_de_munique", "julian_nagelsmann")
]

base_conhecimento_clube = [
    ("arabia", "luis_castro", "al_awwal_park", "al_nassr"),
    ("arabia", "leonardo_jardim", "al_hilal_stadium", "al_hilal"),
    ("espanha", "xavi", "camp_nou", "barcelona"),
    ("franca", "mauricio_pochettino", "parque_dos_principes", "psg"),
    ("inglaterra", "pep_guardiola", "etihad_stadium", "manchester_city"),
    ("estados_unidos", "phil_neville", "lockhart_stadium", "inter_miami"),
    ("espanha", "carlo_ancelotti", "santiago_bernabeu", "real_madrid"),
    ("inglaterra", "jurgen_klopp", "anfield", "liverpool"),
    ("inglaterra", "ole_gunnar_solskjaer", "old_trafford", "manchester_united"),
    ("inglaterra", "steven_gerard", "villa_park", "aston_villa"),
    ("alemanha", "julian_nagelsmann", "allianz_arena", "bayern_de_munique"),
]

base_conhecimento_estadio = [
    ("alemanha", "75000", "allianz_arena"),
    ("arabia", "60000", "al_hilal_stadium"),
    ("arabia", "25000", "al_awwal_park"),
    ("espanha", "100000", "camp_nou"),
    ("espanha", "80000", "santiago_bernabeu"),
    ("franca", "50000", "parque_dos_principes"),
    ("inglaterra", "75000", "old_trafford"),
    ("inglaterra", "56000", "anfield"),
    ("inglaterra", "52000", "etihad_stadium"),
    ("inglaterra", "45000", "villa_park"),
    ("estados_unidos", "20000", "lockhart_stadium")
]

def encontrar_jogador(nacao, time, posicao, idade):
    for jogador in base_conhecimento_jogadores:
        if jogador[0] == nacao and jogador[1] == time and jogador[2] == posicao and jogador[3] == idade:
            return jogador[4]
    return None

def encontrar_formacao(nome):
    for formacao in base_conhecimento_formacao:
        if formacao[0] == nome:
            return formacao[1]
    return None

def encontrar_treinador(clube):
    for treinador in base_conhecimento_treinador:
        if treinador[0] == clube:
            return treinador[1]
    return None

def encontrar_clube(pais, treinador, estadio):
    for clube in base_conhecimento_clube:
        if clube[0] == pais and clube[1] == treinador and clube[2] == estadio:
            return clube[3]
    return None

def encontra_estadio(pais, capacidade):
    for estadio in base_conhecimento_estadio:
        if estadio[0] == pais and estadio[1] == capacidade:
            return estadio[2]
    return None

while True:
    print("\nEscolha uma opção:")
    print("1. Jogador")
    print("2. Formação")
    print("3. Treinador")
    print("4. Clube")
    print("5. Estadio")
    print("0. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == '1':
        print("Coloque as informações do jogador\n")
        nacao = input("Digite o seu país de origem: ")
        time = input("Digite o time: ")
        posicao = input("Digite a posição em que joga: ")
        idade = int(input("Digite a idade: "))
        jogador_encontrado = encontrar_jogador(nacao, time, posicao, idade)
        if jogador_encontrado:
            print(f"Jogador encontrado: {jogador_encontrado}")
        else:
            print("Nenhum jogador encontrado com os critérios fornecidos.")
    elif opcao == '2':
        print("Coloque a formação que deseja saber mais\n")
        nome = input("Digite o nome da formação: ")
        formacao = encontrar_formacao(nome)
        if formacao:
            print(f"Informações: {formacao}")
        else:
            print("Nenhuma formação encontrada com o nome fornecido.")
    elif opcao == '3':
        clube = input("Digite o clube que ele está: ")
        treinador = encontrar_treinador(clube)
        if treinador:
            print(f"Treinador do {clube}: {treinador}")
        else:
            print(f"Nenhum treinador encontrado para o clube {clube}.")
    elif opcao == '4':
        print("Coloque as informações do clube\n")
        pais = input("Qual o país do clube: ")
        treinador = input("Quem treina esse time (advinhe o nome do treinador): ")
        estadio = input("Qual o nome do estadio desse clube: ")
        clube = encontrar_clube(pais, treinador, estadio)
        if clube:
            print(f"Clube: {clube}")
        else:
            print(f"Nenhum clube encontrado para as informações fornecidas.")
    elif opcao == '5':
        print("Coloque as informações do estadio\n")
        pais = input("Digite o país: ")
        capacidade = input("Digite a capacidade que ele comporta (quantos Mil?):")
        estadio = encontra_estadio(pais, capacidade)
        if estadio:
            print(f"Estádio: {estadio}")
        else:
            print("Nenhum estádio encontrado com essas informações")
    elif opcao == '0':
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")