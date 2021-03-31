cadenaUnidades = input("Cantidad: ")
unidades = float(cadenaUnidades)

cadenaPrecio = input("Precio unitario (€): ")
precio = float(cadenaPrecio)

totalItems = 0
precioTotal = 0

listaLineasFact = []

while unidades > 0 and precio > 0:
    totalUnitario = unidades * precio
    item = dict()
    item['unidades'] = unidades
    item['precio'] = precio
    
    listaLineasFact.append(item)
    
    totalItems += unidades # totalItems = totalItems + unidades
    precioTotal += totalUnitario
    
    cadenaUnidades = input("Cantidad: ")
    unidades = float(cadenaUnidades)
    cadenaPrecio = input("Precio unitario (€): ")
    precio = float(cadenaPrecio)
    
for item in listaLineasFact:
    print(item['precio'], "€ -", item['unidades'], "unidades -", item['unidades'] * item['precio'], "€")

    
print("-------------------")
print("Total:", precioTotal)
print("Unidades:", totalItems)
    



