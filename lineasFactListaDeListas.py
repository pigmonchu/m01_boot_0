_UNIDADES = 1
_PRECIO = 0

cadenaUnidades = input("Cantidad: ")
unidades = float(cadenaUnidades)

cadenaPrecio = input("Precio unitario (€): ")
precio = float(cadenaPrecio)

totalItems = 0
precioTotal = 0

listaLineasFact = []

while unidades > 0 and precio > 0:
    totalUnitario = unidades * precio
    item = []
    item.append(unidades)
    item.append(precio)
    
    listaLineasFact.append(item)
    
    totalItems += unidades # totalItems = totalItems + unidades
    precioTotal += totalUnitario
    
    cadenaUnidades = input("Cantidad: ")
    unidades = float(cadenaUnidades)
    cadenaPrecio = input("Precio unitario (€): ")
    precio = float(cadenaPrecio)
    
for item in listaLineasFact:
    print(item[_PRECIO], "€ -", item[_UNIDADES], "unidades -", item[_UNIDADES] * item[_PRECIO], "€")

    
print("-------------------")
print("Total:", precioTotal)
print("Unidades:", totalItems)
    


