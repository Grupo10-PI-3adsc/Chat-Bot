def responder_duvida():
    print("\nQual é sua dúvida? Selecione uma opção:")
    print("1 - Quanto tempo leva uma troca de óleo?")
    print("2 - Quando devo trocar os pneus?")
    print("3 - Como saber se preciso fazer alinhamento/balanceamento?")
    print("4 - O que inclui na revisão geral?")
    print("5 - Voltar ao menu")

    escolha = input("Digite o número da dúvida: ")

    if escolha == "1":
        print("🛢️ Uma troca de óleo normalmente leva entre 30 a 45 minutos, dependendo do modelo do carro.")
    elif escolha == "2":
        print("🚗 Recomenda-se trocar os pneus a cada 40 mil km ou quando a profundidade da banda de rodagem estiver abaixo de 1,6 mm.")
    elif escolha == "3":
        print("📏 Se seu carro estiver puxando para o lado ou vibrando em altas velocidades, pode ser necessário alinhar e balancear.")
    elif escolha == "4":
        print("🔧 A revisão geral inclui verificação dos freios, suspensão, fluidos, filtros, correias e sistema elétrico.")
    elif escolha == "5":
        print("Voltando ao menu...")
    else:
        print("❌ Opção inválida. Tente novamente.")
