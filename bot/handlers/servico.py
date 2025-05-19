def solicitar_servico():
    print("\n🛠️ Serviços disponíveis:")
    print("1 - Troca de óleo")
    print("2 - Alinhamento e balanceamento")
    print("3 - Revisão geral")
    print("4 - Diagnóstico eletrônico (Scanner)")
    print("5 - Troca de filtros")
    print("6 - Troca de fluido de freio")
    print("7 - Voltar")

    escolha = input("Escolha um serviço: ")

    servicos_disponiveis = {
        "1": "Troca de óleo",
        "2": "Alinhamento e balanceamento",
        "3": "Revisão geral",
        "4": "Diagnóstico eletrônico (Scanner)",
        "5": "Troca de filtros",
        "6": "Troca de fluido de freio"
    }

    if escolha in servicos_disponiveis:
        servico = servicos_disponiveis[escolha]
        print(f"\n🛠️ Solicitação de {servico}")
        nome = input("Informe seu nome: ")
        carro = input("Modelo do veículo: ")
        dia = input("Dia preferido para o serviço: ")

        # Pergunta se precisa comprar o produto, apenas para serviços que envolvem peças
        precisa_produto = "n"
        if escolha in ["1", "5", "6"]:
            precisa_produto = input("Você deseja comprar o produto necessário aqui? (s/n): ").lower()
            comprando = "Sim" if precisa_produto == "s" else "Não"
        else:
            comprando = "Não se aplica"

        print(f"\n✅ Solicitação registrada:")
        print(f"Cliente: {nome}")
        print(f"Veículo: {carro}")
        print(f"Serviço: {servico}")
        print(f"Data preferida: {dia}")
        print(f"Compra do produto necessário: {comprando}")
        print("✅ Agendamento concluído! Compareça no horário desejado.")

    elif escolha == "7":
        return
    else:
        print("❌ Serviço não encontrado.")
