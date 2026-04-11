# Pide un número al que usa el codigo y luego lo valida para que sea correcto
def pedir_numero(mensaje):
    return float(input(mensaje))

def restar(a, b):
    return a - b

# Función principal de la resta con reintentos
def ejecutar_resta():
    while True:
        print("\n---RESTA ---")
        
        num1 = pedir_numero("Ingresa el primer número: ")
        num2 = pedir_numero("Ingresa el segundo número: ")

        resultado = restar(num1, num2)
        print(f"Resultado: {resultado}")

# Opción de repetir
        opcion = input("¿Deseas hacer otra resta? (si/no): ").lower()
        if opcion != 'si':
            break