from bot import menu

if __name__ == "__main__":
    while True:
        menu.mostrar_menu()
        continuar = input("\nDeseja realizar outra ação? (s/n): ").lower()
        if continuar != 's':
            print("Finalizando o atendimento...")
            break
