def sum_proper_divisors(number: int) -> int:

    if number <= 1:
        return 0

    # Recorremos todos los posibles divisores desde 1 hasta la mitad del número
    divisors = []
    for divisor in range(1, number // 2 + 1):
        # Si el divisor divide exactamente al numero, lo agregamos a la lista
        if number % divisor == 0:
            divisors.append(divisor)

    # Devolvemos la suma de todos los divisores encontrados
    return sum(divisors)


def is_perfect(number: int) -> bool:

    #Determina si el numero es un número perfecto.
    return sum_proper_divisors(number) == number


def get_first_perfect_numbers(count: int) -> list:
    #Genera una lista con los primeros 'count' números perfectos.
    perfect_numbers = []   # Lista donde guardaremos los números perfectos
    current = 2            # Empezamos desde 2 porque 1 no puede ser perfecto

    # Seguimos buscando hasta encontrar la cantidad solicitada
    while len(perfect_numbers) < count:
        # Verificamos si el número actual es perfecto
        if is_perfect(current):
            perfect_numbers.append(current)
        # Pasamos al siguiente número
        current += 1

    return perfect_numbers