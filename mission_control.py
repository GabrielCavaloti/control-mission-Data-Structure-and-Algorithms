historico = []


def inserir_dados():
    temperatura = float(input("Digite a temperatura da nave: "))

    energia = int(input("Digite o nível de energia (0 a 100): "))
    while energia < 0 or energia > 100:
        print("Digite um valor entre 0 e 100.")
        energia = int(input("Digite o nível de energia (0 a 100): "))

    comunicacao = int(input("Digite 1 para comunicação ativa ou 0 para falha: "))
    while comunicacao != 0 and comunicacao != 1:
        print("Digite somente 1 ou 0.")
        comunicacao = int(input("Digite 1 para comunicação ativa ou 0 para falha: "))

    leitura = [temperatura, energia, comunicacao]
    historico.append(leitura)
    print("Dados inseridos com sucesso.")


def visualizar_status():
    if len(historico) == 0:
        print("Nenhuma leitura foi cadastrada.")
    else:
        ultima_leitura = historico[-1]
        temperatura = ultima_leitura[0]
        energia = ultima_leitura[1]
        comunicacao = ultima_leitura[2]

        print("\nSTATUS ATUAL DA MISSÃO")
        print("Temperatura:", temperatura, "°C")
        print("Energia:", energia, "%")

        if comunicacao == 1:
            print("Comunicação: ativa")
        else:
            print("Comunicação: falha")


def executar_analise():
    if len(historico) == 0:
        print("Nenhuma leitura foi cadastrada.")
    else:
        ultima_leitura = historico[-1]
        temperatura = ultima_leitura[0]
        energia = ultima_leitura[1]
        comunicacao = ultima_leitura[2]
        tem_alerta = False

        print("\nANÁLISE DA MISSÃO")

        if temperatura > 80:
            print("Alerta de superaquecimento!")
            tem_alerta = True

        if energia < 20:
            print("Alerta: ativar economia de energia!")
            tem_alerta = True

        if comunicacao == 0:
            print("Alerta: falha de comunicação!")
            tem_alerta = True

        if tem_alerta == True:
            print("Status operacional: ALERTA")
        else:
            print("Nenhum problema encontrado.")
            print("Status operacional: NORMAL")


def mostrar_historico():
    if len(historico) == 0:
        print("Nenhuma leitura foi cadastrada.")
    else:
        print("\nHISTÓRICO DE LEITURAS")

        for posicao in range(len(historico)):
            leitura = historico[posicao]
            temperatura = leitura[0]
            energia = leitura[1]
            comunicacao = leitura[2]

            print("\nLeitura", posicao + 1)
            print("Temperatura:", temperatura, "°C")
            print("Energia:", energia, "%")

            if comunicacao == 1:
                print("Comunicação: ativa")
            else:
                print("Comunicação: falha")


def mostrar_menu():
    opcao = ""

    while opcao != "5":
        print("\nCONTROLE DA MISSÃO ESPACIAL")
        print("1 - Inserir dados")
        print("2 - Visualizar status")
        print("3 - Executar análise")
        print("4 - Histórico das leituras")
        print("5 - Encerrar sistema")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            inserir_dados()
        elif opcao == "2":
            visualizar_status()
        elif opcao == "3":
            executar_analise()
        elif opcao == "4":
            mostrar_historico()
        elif opcao == "5":
            print("Sistema encerrado.")
        else:
            print("Opção inválida.")


mostrar_menu()