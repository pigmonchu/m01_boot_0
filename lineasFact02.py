cadenaUnidades = input("Cantidad: ")
unidades = float(cadenaUnidades)

cadenaPrecio = input("Precio unitario (€): ")
precio = float(cadenaPrecio)

totalItems = 0
precioTotal = 0

lineasDeImpresion = "\n"

while unidades > 0 and precio > 0:
    totalUnitario = unidades * precio
    
    lineasDeImpresion += str(precio) + "€ - " + str(unidades) + " unidades - " + str(totalUnitario) + "€\n"
#    lineasDeImpresion += "{}€ - {} unidades - {}€\n".format(precio, unidades, totalUnitario)
    
    totalItems += unidades # totalItems = totalItems + unidades
    precioTotal += totalUnitario
    
    cadenaUnidades = input("Cantidad: ")
    unidades = float(cadenaUnidades)
    cadenaPrecio = input("Precio unitario (€): ")
    precio = float(cadenaPrecio)
    
print(lineasDeImpresion)
print("-------------------")
print("Total:", precioTotal)
print("Unidades:", totalItems)
    
