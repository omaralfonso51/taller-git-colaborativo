def es_primo(numero):
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    for i in range(3, int(numero**0.5) + 1, 2):
        if numero % i == 0:
            return False
    return True

def posicion(n):
    if n <= 0:
        return "El número debe ser mayor a cero"
    contador = 0
    candidato = 1
    while contador < n:
        candidato += 1
        if es_primo(candidato):
            contador += 1
    return candidato

if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    print(f"El número primo en la posición {numero} es: {posicion(numero)}")
