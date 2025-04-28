import os
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

# Función para crear carpetas con nombres secuenciales (solo números)
def crear_carpetas_secundarias():
    num_inicio = int(entry_num_inicio.get())
    num_carpetas = int(entry_num_carpetas.get())
    ruta_salida = entry_ruta_salida.get()

    if not os.path.exists(ruta_salida):
        messagebox.showerror("Error", f"La carpeta {ruta_salida} no existe.")
        return

    for i in range(num_carpetas):
        nombre_carpeta = f"{num_inicio + i}"
        ruta_carpeta = os.path.join(ruta_salida, nombre_carpeta)
        
        if not os.path.exists(ruta_carpeta):
            os.makedirs(ruta_carpeta)
            print(f"Carpeta creada: {ruta_carpeta}")
        else:
            print(f"La carpeta {ruta_carpeta} ya existe.")

    messagebox.showinfo("Creación Carpetas", f"Se han creado {num_carpetas} carpetas en {ruta_salida}")

# Función para seleccionar la carpeta
def seleccionar_carpeta():
    carpeta = filedialog.askdirectory()
    if carpeta:
        entry_ruta_salida.delete(0, tk.END)
        entry_ruta_salida.insert(0, carpeta)

# Función para renombrar las imágenes en todas las carpetas dentro de la ruta seleccionada
def renombrar_imagenes_en_todas_las_carpetas():
    ruta_padre = entry_ruta_salida.get()

    if not os.path.exists(ruta_padre):
        messagebox.showerror("Error", f"La carpeta {ruta_padre} no existe.")
        return

    # Recorrer todas las carpetas dentro de la ruta seleccionada
    for carpeta in os.listdir(ruta_padre):
        ruta_carpeta = os.path.join(ruta_padre, carpeta)

        # Verificar si es una carpeta
        if os.path.isdir(ruta_carpeta):
            nombre_carpeta = os.path.basename(ruta_carpeta)
            imagenes = [f for f in os.listdir(ruta_carpeta) if f.lower().endswith(('.jpg', '.png', '.gif'))]

            if not imagenes:
                print(f"No se encontraron imágenes en {ruta_carpeta}")
                continue

            # Renombrar las imágenes con el nombre de la carpeta y el número secuencial
            for i, imagen in enumerate(imagenes, start=1):
                extension = os.path.splitext(imagen)[1]
                nuevo_nombre = f"{nombre_carpeta}({i}){extension}"
                ruta_imagen = os.path.join(ruta_carpeta, imagen)
                ruta_destino = os.path.join(ruta_carpeta, nuevo_nombre)
                os.rename(ruta_imagen, ruta_destino)
                print(f"Imagen {imagen} renombrada a {nuevo_nombre}")

    messagebox.showinfo("Éxito", "Las imágenes en todas las carpetas han sido renombradas correctamente.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Carpetas y Archivos")
ventana.geometry("600x500")

# Título
label_titulo = tk.Label(ventana, text="Creación y Gestión de Carpetas", font=("Helvetica", 18, "bold"))
label_titulo.grid(row=0, column=0, columnspan=2, pady=20)

# Frame para la creación de carpetas
frame_carpetas = tk.Frame(ventana)
frame_carpetas.grid(row=1, column=0, columnspan=2, pady=20, padx=20)

label_num_inicio = tk.Label(frame_carpetas, text="Número inicial de carpetas:")
label_num_inicio.grid(row=0, column=0, sticky="e", padx=10)

entry_num_inicio = tk.Entry(frame_carpetas)
entry_num_inicio.grid(row=0, column=1, padx=10)

label_num_carpetas = tk.Label(frame_carpetas, text="Número de carpetas a crear:")
label_num_carpetas.grid(row=1, column=0, sticky="e", padx=10)

entry_num_carpetas = tk.Entry(frame_carpetas)
entry_num_carpetas.grid(row=1, column=1, padx=10)

boton_crear = tk.Button(frame_carpetas, text="Crear Carpetas", command=crear_carpetas_secundarias)
boton_crear.grid(row=2, column=0, columnspan=2, pady=10)

# Frame para renombrar imágenes
frame_imagenes = tk.Frame(ventana)
frame_imagenes.grid(row=2, column=0, columnspan=2, pady=20, padx=20)

label_ruta_salida = tk.Label(frame_imagenes, text="Ruta de salida:")
label_ruta_salida.grid(row=0, column=0, sticky="e", padx=10)

entry_ruta_salida = tk.Entry(frame_imagenes)
entry_ruta_salida.grid(row=0, column=1, padx=10)

boton_seleccionar_carpeta = tk.Button(frame_imagenes, text="Seleccionar carpeta", command=seleccionar_carpeta)
boton_seleccionar_carpeta.grid(row=1, column=0, columnspan=2, pady=10)

boton_renombrar_imagenes = tk.Button(frame_imagenes, text="Renombrar Imágenes en Todas las Carpetas", command=renombrar_imagenes_en_todas_las_carpetas)
boton_renombrar_imagenes.grid(row=2, column=0, columnspan=2, pady=10)

# Instrucciones
instrucciones = tk.Label(ventana, text="1. Para crear carpetas, ingrese el número inicial y la cantidad.\n"
                                         "2. Para renombrar imágenes en todas las carpetas, seleccione una carpeta con subcarpetas e imágenes y haga clic en 'Renombrar Imágenes'.", justify="left", wraplength=500)
instrucciones.grid(row=3, column=0, columnspan=2, pady=20, padx=20)

# Créditos
label_creditos = tk.Label(ventana, text="Desarrollado por Santiago Cruz - Grupo de Geoquímica Aplicada")
label_creditos.grid(row=4, column=0, columnspan=2, pady=20)

# Iniciar la aplicación
ventana.mainloop()
