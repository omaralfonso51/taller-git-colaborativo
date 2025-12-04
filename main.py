from fibonacci import calcular_fibonacci
from primos import posicion
from factorial import run_factorial 
from operaciones import run_operaciones

def main():
    print("=== MENÚ PRINCIPAL ===")
    print("1. Calcular número en Fibonacci")
    print("2. Obtener número primo en una posición")
    print("3. Calcular factorial")
    print("4. Generar serie números perfectos")
    print("5. Operaciones básicas") 
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        n = int(input("Ingrese un número: "))
        resultado = calcular_fibonacci(n)
        print(f"Fibonacci: {resultado}")

    elif opcion == "2":
        n = int(input("Ingrese la posición del primo: "))
        resultado = posicion(n)
        print(f"El primo en la posición {n} es: {resultado}")
        
    elif opcion == "3": 
        run_factorial()
        
    elif opcion == "4":
        from nperfectos import get_first_perfect_numbers
        count = int(input("¿Cuántos números perfectos desea generar? "))
        perfect_numbers = get_first_perfect_numbers(count)
        print(f"Los primeros {count} números perfectos son: {perfect_numbers}")
        
    elif opcion == "5":
        run_operaciones() 

    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()
