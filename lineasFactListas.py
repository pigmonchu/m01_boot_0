cadenaUnidades = input("Cantidad: ")
unidades = float(cadenaUnidades)

cadenaPrecio = input("Precio unitario (€): ")
precio = float(cadenaPrecio)

totalItems = 0
precioTotal = 0

listaPrecios = []
listaUnidades = []

#Crear lineas
while unidades > 0 and precio > 0:
    totalUnitario = unidades * precio
    listaPrecios.append(precio)
    listaUnidades.append(unidades)
    
    totalItems += unidades # totalItems = totalItems + unidades
    precioTotal += totalUnitario
    
    cadenaUnidades = input("Cantidad: ")
    unidades = float(cadenaUnidades)
    cadenaPrecio = input("Precio unitario (€): ")
    precio = float(cadenaPrecio)
    
#Mostrar líneas
indice = 0
while indice < len(listaPrecios):
    print(listaPrecios[indice], "€ -", listaUnidades[indice], "unidades -", listaPrecios[indice] * listaUnidades[indice], "€")
    indice += 1

    
print("-------------------")
print("Total:", precioTotal)
print("Unidades:", totalItems)

print("\033[3;33;41m")
print("------------------\nTotal:\t\t{:7.2f}€\nUnidades:\t{:7.2f}€".format(precioTotal, totalItems))
print("\033[0;37;40m")
