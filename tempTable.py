def fahrenheitToCentigrados(g):
    return (g - 32) * 5/9

def centigrados(ini, fin):
    for grados in range(ini, fin+10, 10):
        print("{}ºF -> {}ºC".format(grados, fahrenheitToCentigrados(grados)))      

tipo = input("Salida (F/C): ")

if tipo == 'C':
    centigrados(0, 230)
elif tipo == 'F':
    fahrenheit(0, 100)
else:
    print("Tipo incorrecto")
    