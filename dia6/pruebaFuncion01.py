def imprimeCosas(*listadecosas):
    for item in listadecosas:
        print(item)
        
def imprimecondiccionario(**diccionariodeparametros):
    if 'line' in diccionariodeparametros:
        print('Posicionar en linea', diccionariodeparametros['line'])
    else:
        print('No hay line')
    
    
        
        
imprimeCosas('cosa 2', 'cosa 1', 'cosa 3', 'cosa 4')

imprimecondiccionario(contenido='la cosa', line=3, column=5)