from operaciones import suma, resta, multiplicacion, division


def main():
    print("=== Calculadora básica ===")

    while True:
        try:
            a = float(input("Introduce el primer número: "))
            b = float(input("Introduce el segundo número: "))
        except ValueError:
            print("Por favor, introduce solo números.")
            continue

        print("\nOperaciones disponibles:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")

        opcion = input("Elige una opción (1-4): ")

        if opcion == "1":
            print("Resultado:", suma(a, b))
        elif opcion == "2":
            print("Resultado:", resta(a, b))
        elif opcion == "3":
            print("Resultado:", multiplicacion(a, b))
        elif opcion == "4":
            print("Resultado:", division(a, b))
        else:
            print("Opción no válida.")

        continuar = input("\n¿Quieres hacer otra operación? (s/n): ").lower()
        if continuar != "s":
            print("¡Hasta luego!")
            break


if __name__ == "__main__":
    main()
