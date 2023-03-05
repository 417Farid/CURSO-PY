print("Bienvenido a la Calculadora!.")
print("Para salir escribe salir.")
print("Las operaciones son suma, multi, div y resta.")
numero = ""

while (True):
    if not numero:
        numero = input("Ingrese numero: ")
        if numero.lower() == "salir":
            break
        numero = int(numero)
    mensaje = input("Ingrese la Operacion: ")

    if mensaje == "salir":
        break
    elif mensaje == "suma":
        numero2 = int(input("Ingrese siguiente numero: "))
        numero += numero2
    elif mensaje == "resta":
        numero2 = int(input("Ingrese siguiente numero: "))
        numero -= numero2
    elif mensaje == "multi":
        numero2 = int(input("Ingrese siguiente numero: "))
        numero *= numero2
    elif mensaje == "div":
        numero2 = int(input("Ingrese siguiente numero: "))
        numero /= numero2
    else:
        print("Operacion Invalida!")
        break

    print(f"El resultado es: {numero}")
