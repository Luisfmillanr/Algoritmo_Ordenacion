# Implementacion de Algoritmos de ordenación
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import random
import time

# Función para leer datos del archivo
def leer_datos(archivo):
    numeros = []
    with open(archivo, "r") as f:
        for line in f:
            try:
                numeros.append(int(line.strip()))
            except ValueError as e:
                print(f"Error al convertir a entero: {e}")
                continue
    return numeros

# Función para verificar si la lista está correctamente ordenada
def verificar_ordenacion(original, ordenada):
    if len(original) != len(ordenada):
        return False
    original_copy = original[:]
    anterior = None
    for elemento in ordenada:
        if anterior is not None and elemento < anterior:
            return False
        if elemento in original_copy:
            original_copy.remove(elemento)
        else:
            return False
        anterior = elemento
    return not original_copy

# Algoritmo Bubble Sort
def bubble_sort(lista):
    start_time = time.perf_counter()  # Inicia la medición de tiempo
    original = lista[:]
    n = len(lista)
    num_comparaciones = 0
    num_intercambios = 0
    for i in range(n - 1):
        for j in range(n - i - 1):
            num_comparaciones += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                num_intercambios += 1
    time_elapsed = time.perf_counter() - start_time  # Calcula el tiempo transcurrido
    assert verificar_ordenacion(original, lista), "Error en la ordenación"
    return num_comparaciones, num_intercambios, time_elapsed

# Algoritmo Insertion Sort
def insertion_sort(lista):
    start_time = time.perf_counter()  # Inicia la medición de tiempo
    original = lista[:]
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
    time_elapsed = time.perf_counter() - start_time  # Calcula el tiempo transcurrido
    assert verificar_ordenacion(original, lista), "Error en la ordenación"
    return num_comparaciones, num_inserciones, time_elapsed

# Algoritmo Merge Sort
def merge_sort(lista):
    start_time = time.perf_counter()  # Inicia la medición de tiempo solo una vez al comienzo de la función principal
    def merge_sort_rec(sublista):
        if len(sublista) > 1:
            mid = len(sublista) // 2
            L = merge_sort_rec(sublista[:mid])
            R = merge_sort_rec(sublista[mid:])

            i = j = k = 0
            comparaciones = 0
            while i < len(L) and j < len(R):
                comparaciones += 1
                if L[i] < R[j]:
                    sublista[k] = L[i]
                    i += 1
                else:
                    sublista[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                sublista[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                sublista[k] = R[j]
                j += 1
                k += 1
            return sublista, comparaciones
        else:
            return sublista, 0

    sorted_list, total_comparisons = merge_sort_rec(lista)
    time_elapsed = time.perf_counter() - start_time  # Calcula el tiempo transcurrido después de la recursividad
    assert verificar_ordenacion(lista, sorted_list), "Error en la ordenación"
    return total_comparisons, time_elapsed

# Algoritmo Selection Sort
def selection_sort(lista):
    start_time = time.perf_counter()  # Inicia la medición de tiempo
    original = lista[:]
    num_comparaciones = 0
    num_intercambios = 0
    for i in range(len(lista)):
        min_idx = i
        for j in range(i + 1, len(lista)):
            num_comparaciones += 1
            if lista[j] < lista[min_idx]:
                min_idx = j
        if min_idx != i:
            lista[i], lista[min_idx] = lista[min_idx], lista[i]
            num_intercambios += 1
    time_elapsed = time.perf_counter() - start_time  # Calcula el tiempo transcurrido
    assert verificar_ordenacion(original, lista), "Error en la ordenación"
    return num_comparaciones, num_intercambios, time_elapsed

# Función de partición para Quicksort
def quicksort(lista, inicio=0, fin=None, comparaciones=0, intercambios=0):
    if fin is None:
        fin = len(lista) - 1
    if inicio < fin:
        p_index, comparaciones, intercambios = partition(lista, inicio, fin, comparaciones, intercambios)
        comparaciones, intercambios = quicksort(lista, inicio, p_index - 1, comparaciones, intercambios)
        comparaciones, intercambios = quicksort(lista, p_index + 1, fin, comparaciones, intercambios)
    return comparaciones, intercambios

def partition(lista, inicio, fin, comparaciones, intercambios):
    pivote_index = random.randint(inicio, fin)
    lista[pivote_index], lista[fin] = lista[fin], lista[pivote_index]
    pivote = lista[fin]
    p_index = inicio
    for i in range(inicio, fin):
        comparaciones += 1
        if lista[i] <= pivote:
            lista[i], lista[p_index] = lista[p_index], lista[i]
            p_index += 1
            intercambios += 1
    lista[p_index], lista[fin] = lista[fin], lista[p_index]
    intercambios += 1
    return p_index, comparaciones, intercambios

# Función para seleccionar archivo
def seleccionar_archivo(variable_archivo):
    filepath = filedialog.askopenfilename()
    if filepath:
        variable_archivo.set(filepath)

# Función para guardar archivo ordenado
def guardar_archivo_ordenado(numeros_ordenados):
    archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
    if archivo:
        with open(archivo, "w") as f:
            for numero in numeros_ordenados:
                f.write(f"{numero}\n")
        messagebox.showinfo("Información", "Archivo guardado con éxito.")

# Función para aplicar algoritmo y actualizar GUI
def aplicar_algoritmo(algoritmo_seleccionado, archivo_seleccionado, resultado_label):
    numeros = leer_datos(archivo_seleccionado)
    resultado = ""
    tiempo = 0  # Variable para el tiempo de ejecución
    if algoritmo_seleccionado == "Bubble Sort":
        comparaciones, intercambios, tiempo = bubble_sort(numeros)
        resultado = f"Bubble Sort: {comparaciones} comparaciones, {intercambios} intercambios."
    elif algoritmo_seleccionado == "Insertion Sort":
        comparaciones, inserciones, tiempo = insertion_sort(numeros)
        resultado = f"Insertion Sort: {comparaciones} comparaciones, {inserciones} inserciones."
    elif algoritmo_seleccionado == "Merge Sort":
        comparaciones, tiempo = merge_sort(numeros)  # Asegúrate de que merge_sort también devuelva el tiempo
        resultado = f"Merge Sort: {comparaciones} comparaciones."
    elif algoritmo_seleccionado == "Selection Sort":
        comparaciones, intercambios, tiempo = selection_sort(numeros)
        resultado = f"Selection Sort: {comparaciones} comparaciones, {intercambios} intercambios."
    elif algoritmo_seleccionado == "Quicksort":
        comparaciones, intercambios, tiempo = quicksort(numeros, 0, len(numeros) - 1)
        resultado = f"Quicksort: {comparaciones} comparaciones, {intercambios} intercambios."
    else:
        resultado = "Algoritmo no reconocido."
    
    # Actualiza la etiqueta de resultados con el tiempo de ejecución
    resultado_label.config(text=resultado + f" Tiempo de ejecución: {tiempo:.6f} segundos")
    if messagebox.askyesno("Guardar", "¿Deseas guardar los resultados ordenados?"):
        guardar_archivo_ordenado(numeros)

# Interfaz principal
def aplicacion_principal():
    root = tk.Tk()
    root.title("Comparador de Algoritmos de Ordenación")
    main_frame = ttk.Frame(root, padding="10")
    main_frame.pack(fill=tk.BOTH, expand=True)
    ttk.Label(main_frame, text="Selecciona un algoritmo:").grid(column=0, row=0, sticky=tk.W, pady=5, padx=5)
    algoritmo_seleccionado = tk.StringVar()
    algoritmos = ["Bubble Sort", "Insertion Sort", "Merge Sort", "Selection Sort", "Quicksort"]
    combobox_algoritmos = ttk.Combobox(main_frame, textvariable=algoritmo_seleccionado, values=algoritmos, state="readonly")
    combobox_algoritmos.grid(column=1, row=0, sticky=(tk.W + tk.E), pady=5, padx=5)
    combobox_algoritmos.set("Selecciona un algoritmo")
    archivo_seleccionado = tk.StringVar(value="Archivo no seleccionado")
    ttk.Button(main_frame, text="Seleccionar Archivo", command=lambda: seleccionar_archivo(archivo_seleccionado)).grid(column=2, row=0, sticky=tk.W, pady=5, padx=5)
    ttk.Label(main_frame, textvariable=archivo_seleccionado).grid(column=0, row=1, columnspan=3, sticky=tk.W, pady=5, padx=5)
    resultado_label = ttk.Label(main_frame, text="Resultados aparecerán aquí")
    resultado_label.grid(column=0, row=3, columnspan=3, sticky=tk.W, pady=5, padx=5)
    ttk.Button(main_frame, text="Ejecutar", command=lambda: aplicar_algoritmo(algoritmo_seleccionado.get(), archivo_seleccionado.get(), resultado_label)).grid(column=2, row=2, sticky=tk.W, pady=5, padx=5)
    info_creador = "luisfmillanr: www.linkedin.com/in/fernando-dataanaliyst Correo:luisfmillanr@gmail.com " 
    label_creador = ttk.Label(main_frame, text=info_creador, font=('Arial', '10', 'italic' ))
    label_creador.grid(column=0, row=4, columnspan=3, sticky=tk.W, pady=10)
    main_frame.columnconfigure(1, weight=1)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.mainloop()

if __name__ == "__main__":
    aplicacion_principal()
#Algoritmos de ordenación Unir