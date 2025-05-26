def solicitar_servico():
    print("\n🛠️ Serviços disponíveis:")
    print("1 - Troca de óleo")
    print("2 - Alinhamento e balanceamento")
    print("3 - Troca da bateria")
    print("4 - Borracharia")
    print("5 - Manutenção/Troca de embreagem")
    print("6 - Manutenção de injeção eletrônica")
    print("7 - Mecânica")
    print("8 - Suspensão")
    print("9 - Troca de fluido de freio")
    print("10 - Voltar")

    escolha = input("Escolha um serviço: ")

    servicos_disponiveis = {
        "1": "Troca de óleo",
        "2": "Alinhamento e balanceamento",
        "3": "Troca da bateria",
        "4": "Borracharia",
        "5": "Manutenção/Troca de embreagem",
        "6": "Manutenção de injeção eletrônica",
        "7": "Mecânica",
        "8": "Suspensão",
        "9": "Troca de fluido de freio"
    }

    if escolha in servicos_disponiveis:
        servico = servicos_disponiveis[escolha]
        print(f"\n🛠️ Solicitação de {servico}")


    elif escolha == "10":
        return
    else:
        print("❌ Serviço não encontrado.")
