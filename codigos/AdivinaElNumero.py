import random

print("=== ADIVINA EL NÚMERO ===")

minimo = 1
maximo = 100

while True:

    intento = random.randint(minimo, maximo)

    print(f"¿Tu número es {intento}?")

    respuesta = input(
        "Escribe: mayor / menor / correcto: "
    ).lower()

    if respuesta == "mayor":
        minimo = intento + 1

    elif respuesta == "menor":
        maximo = intento - 1

    elif respuesta == "correcto":
        print("¡Adivine tu número!")
        break

    else:
        print("Respuesta inválida")

