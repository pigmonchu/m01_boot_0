def esDecimal(numero):
    try:
        float(numero)
        return True
    except:
        return False

B = input("Base del triángulo: ")
if esDecimal(B):
    b = float(B)
    
    H = input("Altura del triángulo: ")
    
    if esDecimal(H):
        h = float(H)
        area = b * h / 2

        print("Superficie del triángulo:", round(area, 2))
    
    else:
        print(H, "debe ser un número")
else:
    print(B, "debe ser un número")
    
