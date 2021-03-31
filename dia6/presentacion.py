import screen

def validaEdad(cadena): 
    try:
        n = int(cadena)
        if n>=0:
            #entonces el valor es valido
            return True
        return False
    except:
        return False
 
def pedirEdad():
    edad = screen.Input("¿Qué edad tienes? ", line=1, column=1)
    while validaEdad(edad) == False:
        screen.Print("Edad inválida", line=25, column=1, style='bold', color='yellow', back='red')
        edad = screen.Input("¿Qué edad tienes? ", line=1, column=1)
    
    screen.clearLine(25)
        
    return int(edad)

def printScreen():
    screen.clear()
    screen.Print("Bebe....:   -", line=4, column=5)
    screen.Print("Niño....:   -", line=5, column=5)
    screen.Print("Adulto..:   -", line=6, column=5)
    screen.Print("Jubilado:   -", line=7, column=5)
    
    screen.Format(1)
    screen.Print("Total....:", line=9, column=8)
    screen.Reset()
    

