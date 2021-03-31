import math

tupla = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J')

indice = 0



while indice < len(tupla):
    if (indice+1) % 3 == 1:
        print(tupla[indice])
    indice += 1