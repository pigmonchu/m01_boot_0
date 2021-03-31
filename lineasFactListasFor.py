cadenaUnidades = input("Cantidad: ")
unidades = float(cadenaUnidades)

cadenaPrecio = input("Precio unitario (€): ")
precio = float(cadenaPrecio)

totalItems = 0
precioTotal = 0

listaPrecios = []
listaUnidades = []

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
    
for precio, unidades in zip(listaPrecios, listaUnidades):
    print(precio, "€ -", unidades, "unidades -", precio*unidades, "€")
    

print("-------------------")
print("Total:", precioTotal)
print("Unidades:", totalItems)
    


