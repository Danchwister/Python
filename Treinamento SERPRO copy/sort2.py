lista = [4,1,6,2]

def bubble_sort (lista):
    n = len(lista)
    for j in range(n-1):
        for i in range(n-1):
            if lista[i] > lista [i+1]:
                aux = lista [i]
                lista [i] = lista [i+1]
                lista[i+1] = aux
                print(lista)
  

bubble_sort(lista)

    
