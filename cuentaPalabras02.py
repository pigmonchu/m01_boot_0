mitexto = ' tres      palabras para ti.    '

posicion = 1
numPalabras = 0

while posicion < len(mitexto):
    if mitexto[posicion] == ' ' and mitexto[posicion - 1] != ' ':
        numPalabras += 1
    posicion += 1
    
if mitexto[posicion-1] != ' ':
    numPalabras += 1
