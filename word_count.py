with open("lorem_ipsum.txt", "r") as archivo:
    texto=archivo.read()

print(f"El número de caracteres distintos es: {len(set(texto))}")
print(f"El número de palabras distintas es: {len(set(texto.split(' ')))}")





