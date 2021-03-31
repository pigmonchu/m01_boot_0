def isAnagramSimple(p1, p2):
    listaComparacionLetras = []
    
    if len(p1) != len(p2):
        return False
    
    for caracter1 in p1:
        noAñadasFalse = False
        for caracter2 in p2:
            if caracter1 == caracter2:
                noAñadasFalse = True
                listaComparacionLetras.append(True)

        if not noAñadasFalse:
            listaComparacionLetras.append(False)    
                
    if False in listaComparacionLetras:
        return False
    else:
        return True
        

def isAnagram(p1, p2,):
    return isAnagram(p1, p2) and isAnagram(p2, p1)    

def cuentaCaracteres(cadena):
    counts = dict()
    
    for caracter in cadena:
        if caracter in counts:
            counts[caracter] += 1
        else:
            counts[caracter] = 1

    return counts

def isAnagramDic(p1, p2):
    dictS1 = cuentaCaracteres(p1)
    dictS2 = cuentaCaracteres(p2)

    return dictS1 == dictS2

print(__name__)