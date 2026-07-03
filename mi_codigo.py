import random
# La computadora elige un número al azar entre 1 y 20
numero_secreto = random.randint(1, 20)
intentos = 0

print("¡Bienvenidos al juego de adivinar el número!")
print("Estoy pensando en un número entre 1 y 20 ")

# Este bucle se repite para siempre hasta que uses la palabra 'break'
while True:
    intento_usuario = int(input("Introduce tu número: "))
    intentos = intentos + 1 # Sumamos un intento
    if intento_usuario < numero_secreto:
        print("¡Tu número es muy bajo! intenta otra vez.") 
    elif intento_usuario > numero_secreto:
        print("¡Tu número es muy alto! intenta otra vez.")
    else:
        print(f"¡Excelente! Adivinaste el número en {intentos} intentos.")
        break # Esto rompe el bucle y termina el programa 