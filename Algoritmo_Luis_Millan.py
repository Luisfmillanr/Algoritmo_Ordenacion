import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import os

# Función para leer los datos del archivo y convertirlos en una lista de enteros
def leer_datos(archivo):
    with open(archivo, "r") as f:
        numeros = [int(line.strip()) for line in f.readlines()]
    return numeros

# Algoritmo de ordenación Bubble Sort
def bubble_sort(lista):
    n = len(lista)
    num_comparaciones = 0
    num_intercambios = 0
    for i in range(n - 1):
        for j in range(n - i - 1):
            num_comparaciones += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                num_intercambios += 1
    return num_comparaciones, num_intercambios

# Algoritmo de ordenación Insertion Sort
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
    return num_comparaciones, num_inserciones

# Algoritmo de ordenación Merge Sort
def merge_sort(lista):
    if len(lista) > 1:
        mid = len(lista) // 2
        L, comp_L = merge_sort(lista[:mid])
        R, comp_R = merge_sort(lista[mid:])
        lista, comparaciones = merge(L, R)
        return lista, comparaciones + comp_L + comp_R
    return lista, 0

def merge(L, R):
    lista = []
    i = j = comparaciones = 0
    while i < len(L) and j < len(R):
        comparaciones += 1
        if L[i] < R[j]:
            lista.append(L[i])
            i += 1
        else:
            lista.append(R[j])
            j += 1
    lista += L[i:] + R[j:]
    return lista, comparaciones


# Algoritmo de ordenación Selection Sort
def selection_sort(lista):
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
    return num_comparaciones, num_intercambios

# Algoritmo de ordenación Quicksort
def quicksort(lista, inicio, fin):
    if inicio < fin:
        p_index = partition(lista, inicio, fin)
        quicksort(lista, inicio, p_index - 1)
        quicksort(lista, p_index + 1, fin)
    return lista

def partition(lista, inicio, fin):
    pivote = lista[fin]
    p_index = inicio
    for i in range(inicio, fin):
        if lista[i] < pivote:
            lista[i], lista[p_index] = lista[p_index], lista[i]
            p_index += 1
    lista[p_index], lista[fin] = lista[fin], lista[p_index]
    return p_index

# Función para ejecutar el algoritmo seleccionado y actualizar la interfaz con los resultados
def ejecutar_algoritmo():
    archivo = file_path_entry.get()  # Obtiene la ruta del archivo del entry widget
    if not os.path.isfile(archivo):
        resultado_label.config(text="Archivo no válido")  # Muestra un mensaje si el archivo no es válido
        return

    try:
        numeros = leer_datos(archivo)  # Lee los datos del archivo
    except Exception as e:
        resultado_label.config(text=f"Error al leer el archivo: {e}")  # Muestra el error si ocurre uno
        return

    algoritmo = algoritmo_combo.get()  # Obtiene el algoritmo seleccionado del combobox

    try:
        # Ejecuta el algoritmo seleccionado y actualiza la etiqueta con los resultados
        if algoritmo == "Bubble Sort":
            comp, inter = bubble_sort(numeros)
            resultado_label.config(text=f"Bubble Sort\nComparaciones: {comp}, Intercambios: {inter}\nResultado: {numeros[:10]}...")
        elif algoritmo == "Insertion Sort":
            comp, inter = insertion_sort(numeros)
            resultado_label.config(text=f"Insertion Sort\nComparaciones: {comp}, Inserciones: {inter}\nResultado: {numeros[:10]}...")
        elif algoritmo == "Merge Sort":
            numeros, comp = merge_sort(numeros)
            resultado_label.config(text=f"Merge Sort\nComparaciones: {comp}\nResultado: {numeros[:10]}...")
        elif algoritmo == "Selection Sort":
            comp, inter = selection_sort(numeros)
            resultado_label.config(text=f"Selection Sort\nComparaciones: {comp}, Intercambios: {inter}\nResultado: {numeros[:10]}...")
        elif algoritmo == "Quicksort":
            quicksort(numeros, 0, len(numeros) - 1)
            resultado_label.config(text=f"Quicksort\nResultado: {numeros[:10]}...")
        else:
            resultado_label.config(text="Selecciona un algoritmo válido")
            return

        # Habilita el botón de guardado si todo salió bien
        guardar_button.config(state=tk.NORMAL)
    except Exception as e:
        resultado_label.config(text=f"Error durante la ordenación: {e}")  # Muestra el error si ocurre uno


def seleccionar_archivo():
    # Botón para seleccionar el archivo
    browse_button = ttk.Button(frame, text="Seleccionar Archivo", command=seleccionar_archivo)
    browse_button.grid(column=2, row=1, sticky=tk.W)


# Función para guardar los resultados en un archivo
def guardar_resultados():
    global numeros_ordenados  # Asegúrate de que esta variable contiene los números ordenados
    archivo = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )  # Muestra un diálogo para guardar un archivo con la extensión .txt por defecto
    if archivo:
        with open(archivo, "w") as f:  # Abre el archivo seleccionado para escritura
            for numero in numeros_ordenados:
                f.write(f"{numero}\n")  # Escribe cada número en una nueva línea
        messagebox.showinfo("Guardar Resultados", "Los resultados se han guardado correctamente.")
        # Muestra un mensaje indicando que el archivo se guardó correctamente


# Función para configurar la interfaz de la aplicación
def configurar_interfaz():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Comparador de Algoritmos de Ordenación")

    # Marco principal
    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    # Etiqueta para el selector de algoritmo
    algoritmo_label = ttk.Label(frame, text="Selecciona el algoritmo:")
    algoritmo_label.grid(column=0, row=0, sticky=tk.W)

    # Selector de algoritmo
    algoritmo_combo = ttk.Combobox(frame, values=["Bubble Sort", "Insertion Sort", "Merge Sort", "Selection Sort", "Quicksort"])
    algoritmo_combo.grid(column=1, row=0, sticky=(tk.W, tk.E))
    algoritmo_combo.set("Selecciona un algoritmo")

    # Entrada para la ruta del archivo
    file_path_entry = ttk.Entry(frame, width=50)
    file_path_entry.grid(column=0, row=1, sticky=(tk.W, tk.E), columnspan=2)

    # Botón para seleccionar el archivo
    browse_button = ttk.Button(frame, text="Seleccionar Archivo", command=lambda: seleccionar_archivo(file_path_entry))
    browse_button.grid(column=2, row=1, sticky=tk.W)

    # Etiqueta para mostrar los resultados
    resultado_label = ttk.Label(frame, text="Resultados aparecerán aquí", relief="sunken", padding="4", anchor="w")
    resultado_label.grid(column=0, row=3, sticky=(tk.W, tk.E), columnspan=3)

    # Botón para ejecutar el algoritmo de ordenación
    ejecutar_button = ttk.Button(frame, text="Ejecutar", command=lambda: ejecutar_algoritmo(file_path_entry.get(), algoritmo_combo.get(), resultado_label))
    ejecutar_button.grid(column=1, row=2, sticky=tk.E)

    # Botón para guardar los resultados en un archivo
    guardar_button = ttk.Button(frame, text="Guardar Resultados", command=guardar_resultados, state=tk.DISABLED)
    guardar_button.grid(column=1, row=4, sticky=tk.E)

    # Configuración de expansión
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.rowconfigure(3, weight=1)

    # Retorna la ventana principal
    return root

if __name__ == "__main__":
    app = configurar_interfaz()
    app.mainloop()