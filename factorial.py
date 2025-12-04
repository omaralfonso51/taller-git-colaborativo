def factorial(n):
    """Calcula el factorial de un número entero no negativo."""
    # Input validation
    if isinstance(n, float):
        if not n.is_integer():
            raise ValueError("Debes ingresar un número entero no negativo.")
        n = int(n)

    if not isinstance(n, int):
        raise ValueError("Debes ingresar un número entero no negativo.")

    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")

    # Base cases
    if n == 0 or n == 1:
        return 1

    # Iterative calculation
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i

    return resultado


def run_factorial():
    """Ejecute el menú interactivo de cálculo factorial."""
    print("\n--- Cálculo de Factorial ---")

    while True:
        entrada = input("Ingresa un entero no negativo (o 's' para salir): ").strip()

        if entrada.lower() in ("s", "salir"):
            print("Volviendo al menú...")
            return

        try:
            # Allow numbers like 5 and 5.0
            valor = float(entrada) if "." in entrada else int(entrada)
            resultado = factorial(valor)
            print(f"\nEl factorial de {int(valor)} es: {resultado}\n")

        except Exception as e:
            print(f"Error: {e}\nIntenta nuevamente.\n")
