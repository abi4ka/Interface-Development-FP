def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return "Error: división por 0"
    return a / b


if __name__ == "__main__":
    print("Prueba de funciones:")
    print("Suma:", suma(2, 3))
    print("Resta:", resta(5, 1))
    print("Multiplicación:", multiplicacion(4, 3))
    print("División:", division(8, 2))
