from resta import ejecutar_resta
from multiplicacion import ejecutar_multiplicacion
from suma import ejecutar_suma
from division import ejecutar_division

def menu():
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ejecutar_suma()
        if opcion == "2":
            ejecutar_resta()
        elif opcion == "3":
            ejecutar_multiplicacion()
        elif opcion=="4":
            ejecutar_division()
        elif opcion=="5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intenta nuevamente.")
            
if __name__ == "__main__":
    menu()