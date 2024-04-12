import tkinter as tk
from tkinter import filedialog, ttk
import os

# Funciones de ordenación
import tkinter as tk
from tkinter import filedialog, ttk
import os

# Funciones de ordenación
def leer_datos(archivo):
    with open(archivo, "r") as f:
        numeros = [int(line.strip()) for line in f]
    return numeros

def bubble_sort(lista):
    n = len(lista)
    num_comparaciones = 0
    num_intercambios = 0
    for i in range(n-1):
        for j in range(0, n-i-1):
            num_comparaciones += 1
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                num_intercambios += 1
    return num_comparaciones, num_intercambios

def insertion_sort(lista):
    num_comparaciones = 0
    num_inserciones = 0
    for i in range(1, len(lista)):
        key = lista[i]
        j = i-1
        while j >= 0 and key < lista[j]:
            num_comparaciones += 1
            lista[j+1] = lista[j]
            j -= 1
            num_inserciones += 1
        lista[j+1] = key
    return num_inserciones, num_comparaciones

def merge_sort(lista):
    global num_comparaciones_merge
    num_comparaciones_merge = 0
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

def selection_sort(lista):
    num_comparaciones = 0
    num_intercambios = 0
    
    for i in range(len(lista)):
        min_idx = i
        for j in range(i+1, len(lista)):
            num_comparaciones += 1
            if lista[min_idx] > lista[j]:
                min_idx = j
        
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
        num_intercambios += 1 if min_idx != i else 0

    return num_comparaciones, num_intercambios

def quicksort(lista, inicio, fin):
    if inicio < fin:
        p_index = partition(lista, inicio, fin)
        quicksort(lista, inicio, p_index - 1)
        quicksort(lista, p_index + 1, fin)

def partition(lista, inicio, fin):
    pivote = lista[fin]
    p_index = inicio
    for i in range(inicio, fin):
        if lista[i] <= pivote:
            lista[i], lista[p_index] = lista[p_index], lista[i]
            p_index += 1
    lista[p_index], lista[fin] = lista[fin], lista[p_index]
    return p_index


# Interfaz gráfica
def ejecutar_algoritmo():
    archivo = file_path_entry.get()
    if not os.path.isfile(archivo):
        resultado_label.config(text="Archivo no válido")
        return
    
    numeros = leer_datos(archivo)
    algoritmo = algoritmo_combo.get()
    
    # Aquí puedes invocar la función de ordenación basada en la elección del usuario
    # Ejemplo:
    if algoritmo == "Bubble Sort":
        comp, inter = bubble_sort(numeros)
    # Continúa para otros algoritmos...

    # Configura el texto del resultado
    resultado_label.config(text=f"Resultado: {numeros[:10]}...")  # Simplificado para propósitos de demostración

def seleccionar_archivo():
    filename = filedialog.askopenfilename()
    file_path_entry.delete(0, tk.END)
    file_path_entry.insert(0, filename)

# Configuración de la UI
root = tk.Tk()
root.title("Comparador de Algoritmos de Ordenación")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

algoritmo_label = ttk.Label(frame, text="Selecciona el algoritmo:")
algoritmo_label.grid(column=0, row=0, sticky=tk.W)

algoritmo_combo = ttk.Combobox(frame, values=["Bubble Sort", "Insertion Sort", "Merge Sort", "Selection Sort", "Quicksort"])
algoritmo_combo.grid(column=1, row=0, sticky=(tk.W, tk.E))
algoritmo_combo.set("Selecciona un algoritmo")

file_path_entry = ttk.Entry(frame, width=50)
file_path_entry.grid(column=0, row=1, sticky=(tk.W, tk.E), columnspan=2)

browse_button = ttk.Button(frame, text="Seleccionar Archivo", command=seleccionar_archivo)
browse_button.grid(column=2, row=1, sticky=tk.W)

ejecutar_button = ttk.Button(frame, text="Ejecutar", command=ejecutar_algoritmo)
ejecutar_button.grid(column=1, row=2, sticky=tk.E)

resultado_label = ttk.Label(frame, text="Resultados aparecerán aquí", relief="sunken", padding="4", anchor="w")
resultado_label.grid(column=0, row=3, sticky=(tk.W, tk.E), columnspan=3)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.rowconfigure(3, weight=1)

root.mainloop()

