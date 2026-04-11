from resta import ejecutar_resta

def menu():
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Resta")
        print("2. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ejecutar_resta()
        elif opcion == "2":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intenta nuevamente.")


if __name__ == "__main__":
    menu()