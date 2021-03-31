import anagramas

p1 = input("Una palabra: ")
p2 = input("Otra palabra: ")


if anagramas.isAnagramDic(p1, p2):
    print ("son anagramas")
else:
    print("No son anagramas")
    

