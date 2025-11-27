def fibonacci(limit):
    """
    Imprime la secuencia de Fibonacci hasta el límite especificado.
    """
    a, b = 0, 1
    print(f"Secuencia de Fibonacci hasta {limit}:")
    while a < limit:
        print(a, end=' ')
        # Actualiza a y b a la vez: a toma el valor de b, y b toma el valor de a + b
        a, b = b, a + b
    print("\nFin de la secuencia.")

# Ejecutar la función con un límite de 50
if __name__ == "__main__":
    fibonacci(50)