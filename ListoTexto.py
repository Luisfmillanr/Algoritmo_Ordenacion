import random

# Función para leer datos de un archivo
def leer_datos(archivo):
    with open(archivo, "r") as f:
        numeros = [int(line.strip()) for line in f]
    return numeros

# Bubble Sort
def bubble_sort(lista):
    n = len(lista)
    num_comparaciones = 0
    num_intercambios = 0
    for i in range(n-1):
        for j in range(n-i-1):
            num_comparaciones += 1
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                num_intercambios += 1
    return num_comparaciones, num_intercambios

# Insertion Sort
def insertion_sort(lista):
    num_comparaciones = 0
    num_inserciones = 0
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > key:
            num_comparaciones += 1
            lista[j + 1] = lista[j]
            j -= 1
            num_inserciones += 1
        lista[j + 1] = key
    return num_inserciones, num_comparaciones

# Merge Sort
def merge_sort(lista):
    num_comparaciones = 0
    if len(lista) > 1:
        mid = len(lista) // 2
        L = lista[:mid]
        R = lista[mid:]

        num_comparaciones += merge_sort(L)[1]
        num_comparaciones += merge_sort(R)[1]

        i = j = k = 0
        while i < len(L) and j < len(R):
            num_comparaciones += 1
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

    return lista, num_comparaciones

# Selection Sort
def seleccion_sort(lista):
    num_comparaciones = 0
    num_intercambios = 0
    for i in range(len(lista)):
        min_idx = i
        for j in range(i+1, len(lista)):
            num_comparaciones += 1
            if lista[min_idx] > lista[j]:
                min_idx = j
        if min_idx != i:
            lista[i], lista[min_idx] = lista[min_idx], lista[i]
            num_intercambios += 1
    return num_comparaciones, num_intercambios

# Quicksort
def quicksort(lista, inicio, fin, comparaciones=0, intercambios=0):
    if inicio < fin:
        p_index, comparaciones, intercambios = partition(lista, inicio, fin, comparaciones, intercambios)
        comparaciones, intercambios = quicksort(lista, inicio, p_index-1, comparaciones, intercambios)
        comparaciones, intercambios = quicksort(lista, p_index+1, fin, comparaciones, intercambios)
    return comparaciones, intercambios

def partition(lista, inicio, fin, comparaciones, intercambios):
    pivote = lista[fin]
    p_index = inicio
    for i in range(inicio, fin):
        comparaciones += 1
        if lista[i] < pivote:
            lista[i], lista[p_index] = lista[p_index], lista[i]
            p_index += 1
            intercambios += 1
    lista[p_index], lista[fin] = lista[fin], lista[p_index]
    intercambios += 1
    return p_index, comparaciones, intercambios

def main():
    algoritmos = {
        "1": ("Bubble Sort", bubble_sort),
        "2": ("Insertion Sort", insertion_sort),
        "3": ("Merge Sort", merge_sort),
        "4": ("Selection Sort", seleccion_sort),
        "5": ("Quicksort", quicksort)
    }

    nombre_archivo = input("Por favor, introduce la ruta del archivo: ")
    numeros = leer_datos(nombre_archivo)

    print("Seleccione el algoritmo de ordenación:")
    for k, v in algoritmos.items():
        print(f"{k}: {v[0]}")
    opcion = input("Número del algoritmo: ")

    if opcion in algoritmos:
        algoritmo = algoritmos[opcion][1]
        if algoritmo == quicksort:
            comparaciones, intercambios = algoritmo(numeros, 0, len(numeros)-1)
        else:
            comparaciones, intercambios = algoritmo(numeros)
        print("Números ordenados:", numeros)
        print("Número de comparaciones:", comparaciones)
        print("Número de intercambios:", intercambios)
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()
1