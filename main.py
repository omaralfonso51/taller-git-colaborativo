# Menú principal – Estudiante 1

def menu():
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Fibonacci")
        print("2. Factorial")
        print("3. Primos")
        print("4. N números perfectos")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Función Fibonacci (a implementar por Estudiante 2)")

        elif opcion == "2":
            print("Función Factorial (a implementar por Estudiante 3)")

        elif opcion == "3":
            print("Función Primos (a implementar por Estudiante 4)")

        elif opcion == "4":
            print("Función N números perfectos (a implementar por Estudiante 5)")

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
