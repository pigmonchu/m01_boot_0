import screen

entradasQ = {'bebe': 0, 'niño': 0, 'adulto': 0, 'jubilado': 0}
precios = {'bebe': 0, 'niño': 14.0, 'adulto': 23.0, 'jubilado': 18.0}

campos = {
    'bebe': {
        'Q': (4,13),
        'acum': (4,18)
    },
    'niño': {
        'Q': (5,13),
        'acum': (5,18)
    },
    'adulto': {
        'Q': (6,13),
        'acum': (6,18)
    },
    'jubilado':  {
        'Q': (7,13),
        'acum': (7,18)
    },
    'entradas': (1,1),
    'error': (1,25)
}
    
def tipoEntrada(e):
    if e > 0 and e <=2:
        tipo = 'bebe'
    elif e <=12:
        tipo = 'niño'
    elif e < 65:
        tipo = 'adulto'
    else:
        tipo = 'jubilado'
    
    return tipo
 
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
    screen.locate(campos['entradas'][0], campos['entradas'][1])
    edad = input("¿Qué edad tienes? ")
    while validaEdad(edad) == False:
        screen.locate(campos['error'][0], campos['error'][1])
        print("Edad inválida")
        screen.locate(campos['entradas'][0], campos['entradas'][1])
        edad = input("¿Qué edad tienes? ")
    
    return int(edad)

def printScreen():
    screen.locate(4,4)
    print("Bebe....:   -    0.00€")
    screen.locate(5,4)
    print("Niño....:   -    0.00€")
    screen.locate(6,4)
    print("Adulto..:   -    0.00€")
    screen.locate(7,4)
    print("Jubilado:   -    0.00€")
    
    screen.locate(9,7)
    print("Total....:    0.00€")

def actualizaEntradas(tEntrada, Q):
    screen.locate(campos[tEntrada]['Q'][0], campos[tEntrada]['Q'][1])
    print("{:2d}".format(entradasQ[tEntrada]))
    screen.locate(campos[tEntrada]['acum'][0], campos[tEntrada]['acum'][1])
    print("{:7.2f}€".format(entradasQ[tEntrada] * precios[tEntrada]))

def actualizaTotal():
    total = 0
    for tipo in entradasQ:
        total += entradasQ[tipo] * precios[tipo]
        
    screen.locate(9,18)
    print("{:7.2f}€".format(total))

screen.clear()
printScreen()

edad = pedirEdad()

while edad != 0:
    tipoE = tipoEntrada(edad)
    entradasQ[tipoE] += 1
    
    actualizaEntradas(tipoE, 1)
    actualizaTotal()

    edad = pedirEdad()
    
screen.locate(12,1)


