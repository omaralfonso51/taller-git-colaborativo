def calcular_fibonacci(n):
    if n <= 0:
        return "El número debe ser mayor a cero"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    print(f"Fibonacci: {calcular_fibonacci(numero)}")