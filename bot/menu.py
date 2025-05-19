from bot.handlers import duvida, servico

def mostrar_menu():
    print("\n🚗 Bem-vindo ao AutoCenter Virtual! Escolha uma opção:")
    print("1 - Tirar dúvida sobre serviços")
    print("2 - Solicitar um serviço")
    print("3 - Ver horário de funcionamento")
    print("4 - Consultar preços de serviços")
    print("5 - Localização e contato")
    print("6 - Encerrar atendimento")

    escolha = input("Digite o número da opção: ")

    if escolha == "1":
        duvida.responder_duvida()
    elif escolha == "2":
        servico.solicitar_servico()
    elif escolha == "3":
        print("⏰ Horário de funcionamento:\nSegunda a Quinta: 08:00 às 17:00\n Sexta: 08:00 as 16:00\n Dábados: 08:00 as 12:30 \n Domingos e feriados: fechado.")
    elif escolha == "4":
        print("💰 Tabela de preços:\n- Troca de óleo: R$ 120,00\n- Alinhamento e balanceamento: R$ 90,00\n- Revisão geral: R$ 350,00")
    elif escolha == "5":
        print("📍 Endereço: R. dos Gerânios, 21 - Box 01 - Ipês (Polvilho), Cajamar - SP, 07790-870 \n📞 Telefone: (11) 94569-9104")
    elif escolha == "6":
        print("👋 Atendimento encerrado. Obrigado pela visita!")
    else:
        print("❌ Opção inválida.")
