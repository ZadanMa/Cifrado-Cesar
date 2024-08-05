# Lista de letras del alfabeto
letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
          "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Solicitar al usuario la palabra a codificar
palabraIngreso = input("Ingrese la palabra para codificar: \n").lower()
cantidadIngreso = len(palabraIngreso)
listaIngreso = list(palabraIngreso)

# Solicitar al usuario el parámetro de desplazamiento
parametro = int(input("Ingrese el parámetro: \n"))

# Lista para almacenar la palabra codificada
display = []

# Realizar el cifrado
for letra in listaIngreso:
    if letra in letras:
        # Encontrar la posición de la letra en la lista de letras
        posicion_actual = letras.index(letra)
        # Calcular la nueva posición con el desplazamiento
        nueva_posicion = (posicion_actual + parametro) % 26
        # Agregar la letra codificada a la lista display
        display.append(letras[nueva_posicion])
    else:
        # Si la letra no está en el alfabeto (por ejemplo, un espacio o un símbolo), agregarla sin cambios
        display.append(letra)

# Unir la lista display en una cadena y mostrarla
print(f"Palabra codificada: {''.join(display)}")
