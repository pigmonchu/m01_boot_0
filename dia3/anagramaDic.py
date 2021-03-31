def cuentaCaracteres(cadena):
    counts = dict()
    
    for caracter in cadena:
        if caracter in counts:
            counts[caracter] += 1
        else:
            counts[caracter] = 1

    return counts

def isAnagramDic(p1, p2)
    dictS1 = cuentaCaracteres(p1)
    dictS2 = cuentaCaracteres(p2)

    return dictS1 == dictS2
    
