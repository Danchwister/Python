lista = [3,8,2,5,6]

def SortTroca (lista):
    n = len(lista)
    for j in range(n-1):
        for i in range(n-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                print(lista)


SortTroca(lista)
if lista != [2,3,5,8]:
    print("Deu merda! ")
else:
    print("Deu bom!! ")

