cadenaUnidades = input("Cantidad: ")
unidades = float(cadenaUnidades)

cadenaPrecio = input("Precio unitario (€): ")
precio = float(cadenaPrecio)

totalItems = 0
precioTotal = 0

while unidades > 0 and precio > 0:
    totalUnitario = unidades * precio
    print(precio, "€ -", unidades, "unidades -", totalUnitario, "€")
    
    totalItems += unidades # totalItems = totalItems + unidades
    precioTotal += totalUnitario
    
    cadenaUnidades = input("Cantidad: ")
    unidades = float(cadenaUnidades)
    cadenaPrecio = input("Precio unitario (€): ")
    precio = float(cadenaPrecio)
    
print("-------------------")
print("Total:", precioTotal)
print("Unidades:", totalItems)
    