miTexto = "tres palabras para ti"

frecuencias = dict()

for caracter in miTexto:
    if caracter in frecuencias:
        frecuencias[caracter] += 1
    else:
        frecuencias[caracter] = 1
    
for caracter in frecuencias.keys():
    print(caracter, "-", frecuencias[caracter])