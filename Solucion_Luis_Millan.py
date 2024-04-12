#Definimos la funcion leer datos
def leer_datos(archivo):
    with open(archivo, "r") as f:
        numeros = [int(line.strip()) for line in f]
        return numeros
    

#BubblsSort "Burbuja"
def bubble_sort(lista):
    n = len(lista)
    num_comparaciones = 0
    num_intercambios = 0
    for i in range(n-1):
        for j in range (0,n-i-1):
            num_comparaciones += 1
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                num_intercambios +=1
    return num_comparaciones, num_intercambios

#InsertionSort "Algoritmo de insersion"

def insertion_sort(lista):
    num_comparaciones = 0
    num_inserciones = 0
    for i in range(1,len(lista)):
        key = lista[i]
        j = i-1
        while j >=0 and key < lista[j]:
            num_comparaciones +=1
            lista[j+1] = lista[j]
            j -= 1
            num_inserciones +=1
            lista[j+1] = key
    return num_inserciones, num_comparaciones

#Margesort "Dividir y conquistar"

def merge_sort(lista):
    global num_comparaciones_merge
    if len(lista) > 1:
        mid = len(lista)//2
        L = lista[:mid]
        R = lista[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            num_comparaciones_merge += 1
            if L[i] < R[j]:
                lista[k] = L[i]
                i += 1
            else:
                lista[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            lista[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            lista[k] = R[j]
            j += 1
            k += 1

#Seleccion sort "Algoritmo de ordenacion por seleccion"

def seleccion_sort(lista):
    num_comparaciones = 0 
    num_intercambios = 0

    for i in range(len(lista)):
        min_idx = i
        for j in range(i+1, lent(lista)):
            num_comparaciones += 1
            if lista[min_idx] > lista[j]:
                min_idx = j

        lista[i], lista[min_idx] = lista[min_idx], lista[i]
        num_intercambios += 1 if min_idx != i else 0

    return num_comparaciones, num_intercambios

#Quicksort "Ordenacion rapida"
def quicksort (lista, inicio, fin):
    if inicio < fin:
        p_index = partition(lista, inicio, fin)
        quicksort(lista, inicio, p_index -1) #Antes del pivote
        quicksort(lista, p_index +1, fin)    #Despues de pivote

def partitition(lista, inicio, fin):
    pivote = lista[fin]
    p_index = inicio
    for i in range(inicio, fin):
        if lista[i] < pivote:
            lista[i], lista[p_index] = lista[p_index], lista[i]
            p_index += 1
    lista[p_index], lista[fin] =  lista[fin], lista[p_index]
    
    return p_index 


"""
#Ejercicio "Bubble"
nombre_archivo = "/home/luisfmillanr/Documentos/Entrada-800.txt"
numeros = leer_datos(nombre_archivo)

num_comparaciones, num_intercambios = bubble_sort(numeros) #Cambiar a la funcion que se quiera usar

print("Numeros ordenados ", numeros)
print("Numero de comparaciones ", num_comparaciones)
print("Numero de intercambios ", num_intercambios)
"""

nombre_archivo = "/home/luisfmillanr/Documentos/Entrada-8000.txt"
numeros = leer_datos(nombre_archivo)

num_comparaciones, num_inserciones = insertion_sort(numeros) #Cambiar a la funcion que se quiera usar

print("Numeros ordenados ", numeros)
print("Numero de comparaciones ", num_comparaciones)
print("Numero de intercambios ", num_inserciones)