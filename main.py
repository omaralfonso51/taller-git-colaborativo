from fibonacci import calcular_fibonacci
from primos import posicion

def main():
    print("=== MENÚ PRINCIPAL ===")
    print("1. Calcular número en Fibonacci")
    print("2. Obtener número primo en una posición")
    print("4. Generar serie números perfectos")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        n = int(input("Ingrese un número: "))
        resultado = calcular_fibonacci(n)
        print(f"Fibonacci: {resultado}")

    elif opcion == "2":
        n = int(input("Ingrese la posición del primo: "))
        resultado = posicion(n)
        print(f"El primo en la posición {n} es: {resultado}")

    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()
