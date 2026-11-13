from operaciones import sumar, restar, multiplicar, dividir


def solicitar_numeros():
    while True:
        try:
            num1 = float(input("Ingrese primer numero: "))
            num2 = float(input("Ingrese segundo numero: "))

            return num1, num2
        except ValueError:
            print("Error: Debes un numero valido.")


"""Creacion de una calculadora """
# Aqui muestro el codigo completo para crear una calculardora simple

"""Onboarding"""
# Mostrar opciones para el users.
# Este es el primer menu que muestra las diferenctes operaciones que podemos realizar.
# Utilizan print("") podemos crear un menu de la siguiente manera.
opcion = ""
while opcion != "5":

    print("      PYTHON CALCULATOR      ")
    print("=============================")
    print("=============================")
    print()
    print("              Menu            ")
    print("1. Sumar")
    print("2. Resta")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    print()

    opcion = input("Selecione una opcion: ")

    if opcion == "1":
        print("========Suma=======")
        num1, num2 = solicitar_numeros()
        resultado = sumar(num1, num2)
        print("Resultado:", resultado)
        print()

    elif opcion == "2":
        print("========Resta=======")
        num1, num2 = solicitar_numeros()
        resultado = restar(num1, num2)
        print("Resultado:", resultado)
        print()

    elif opcion == "3":
        print("========Multiplicacion=======")
        num1, num2 = solicitar_numeros()
        resultado = multiplicar(num1, num2)
        print("Resultado:", resultado)
        print()

    elif opcion == "4":
        print("========Division=======")
        num1, num2 = solicitar_numeros()
        resultado = dividir(num1, num2)

        if resultado is None:
            print("Error: None, no sep uede dividr entre cero.")
        else:
            print("Resultado:", resultado)

    print()
