def esDecimal(numero):
    try:
        float(numero)
        return True
    except:
        return False

B = input("Base del triángulo: ")
while not esDecimal(B):
    print(B, "debe ser un número")
    B = input("Base del triángulo: ")
    
H = input("Altura del triángulo: ")
while not esDecimal(H):
    print(H, "debe ser un número")
    H = input("Altura del triángulo: ")

b = float(B)
h = float(H)
area = b * h / 2

print("Superficie del triángulo:", round(area, 2))
    
