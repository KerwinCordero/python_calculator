"""Creacion de una calculadora """
# Aqui muestro el codigo completo para crear una calculardora simple

"""Onboarding"""
# Mostrar opciones para el users.
print("=============================")
print("      PYTHON CALCULATOR      ")
print("=============================")
print()
print("              Menu            ")
print("1. Sumar")
print("2. Resta")
print("3. Multiplicar")
print("4. Dividir")
print("5. Salir")
print()

# Captura de opcion por el users.
opcion = input("Selecione una opcion: ")

if opcion == "1":
    print("Seleccionaste sumar")

elif opcion == "2":
    print("Seleccionaste restar")

elif opcion == "3":
    print("Seleccionaste Multiplicar")

elif opcion == "4":
    print("Seleccionaste Dividir")

elif opcion == "5":
    print("Apagando Calculadora.")

else:
    print("Opciona No Valida.")
print()


print()
print()
print()
