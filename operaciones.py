def sumar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero"
    return a / b


if __name__ == "__main__":
    print("=== OPERACIONES BÁSICAS ===")
    print("1. Sumar")
    print("2. Multiplicar")
    print("3. Dividir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print(f"Resultado: {sumar(a, b)}")

    elif opcion == "2":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print(f"Resultado: {multiplicar(a, b)}")

    elif opcion == "3":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print(f"Resultado: {dividir(a, b)}")

    else:
        print("Opción no válida")