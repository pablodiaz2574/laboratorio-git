from resta import ejecutar_resta
from multiplicacion import ejecutar_multiplicacion

def menu():
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Resta")
        print("2. Multiplicacion")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ejecutar_resta()
        elif opcion == "2":
            ejecutar_multiplicacion()
        elif opcion=="3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intenta nuevamente.")
            
if __name__ == "__main__":
    menu()