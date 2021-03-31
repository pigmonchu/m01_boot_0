from config import preciosE


fEntradas = open("transacciones.txt", 'r')


numEntradasBebe = 0
numEntradasNiño = 0
numEntradasAdulto = 0
numEntradasJubilado = 0


linea = fEntradas.readline()

totalEntradas = 0
totalPrecio = 0

while linea != '':
    entradas = linea.split(',')
    numEntradasBebe += int(entradas[0])
    numEntradasNiño += int(entradas[1])
    numEntradasAdulto += int(entradas[2])
    numEntradasJubilado += int(entradas[3])

    totalEntradas = totalEntradas + int(entradas[0])
    totalEntradas = totalEntradas + int(entradas[1])
    totalEntradas = totalEntradas + int(entradas[2])
    totalEntradas = totalEntradas + int(entradas[3])
    
    linea = fEntradas.readline()

print("Entradas de Bebe....: {:3d} -  {:7.2f}€".format(numEntradasBebe, numEntradasBebe * preciosE['bebe']))
print("Entradas de Niño....: {:3d} -  {:7.2f}€".format(numEntradasNiño, numEntradasNiño * preciosE['niño']))
print("Entradas de Adulto..: {:3d} -  {:7.2f}€".format(numEntradasAdulto, numEntradasAdulto * preciosE['adulto']))
print("Entradas de Jubilado: {:3d} -  {:7.2f}€".format(numEntradasJubilado, numEntradasJubilado * preciosE['jubilado']))

print("\nTotal: {:3d} - {:7.2f}€".format(totalEntradas,
                                         numEntradasBebe * preciosE['bebe']+numEntradasNiño * preciosE['niño']+\
                                         numEntradasAdulto * preciosE['adulto']+numEntradasJubilado * preciosE['jubilado']))
    