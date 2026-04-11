#
def suma (a,b):
    resultado= a+b
    return resultado

# Mensajito de bienvenida
print("------LA CALCULADORA DE SUMA------")

# Ingreso de datos o numeros 

num1= float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

resultado =suma (num1,num2)
print("El resultado es: ", resultado)
