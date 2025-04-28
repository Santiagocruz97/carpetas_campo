import os
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

# Función para crear carpetas con nombres secuenciales (solo números)
def crear_carpetas_secundarias():
    # Obtener los valores introducidos por el usuario
    num_inicio = int(entry_num_inicio.get())  # Número inicial
    num_carpetas = int(entry_num_carpetas.get())  # Número de carpetas a crear
    ruta_salida = entry_ruta_salida.get()  # Ruta de salida

    # Verificar que la ruta de salida existe
    if not os.path.exists(ruta_salida):
        messagebox.showerror("Error", f"La carpeta {ruta_salida} no existe.")
        return

    # Crear las carpetas con nombres secuenciales (solo números)
    for i in range(num_carpetas):
        nombre_carpeta = f"{num_inicio + i}"  # El nombre será solo el número
        ruta_carpeta = os.path.join(ruta_salida, nombre_carpeta)

        # Crear la carpeta si no existe
        if not os.path.exists(ruta_carpeta):
            os.makedirs(ruta_carpeta)
            print(f"Carpeta creada: {ruta_carpeta}")
        else:
            print(f"La carpeta {ruta_carpeta} ya existe.")

    # Ventana emergente con título personalizado y mensaje de crédito
    messagebox.showinfo("Creación Carpetas Repositorio Información Campo",
                        f"Se han creado {num_carpetas} carpetas en {ruta_salida}\n\nDesarrollado por Santiago Cruz - Grupo de Geoquímica Aplicada", icon='info')

# Función para abrir un cuadro de diálogo y seleccionar la carpeta
def seleccionar_carpeta():
    carpeta = filedialog.askdirectory()  # Abre el cuadro de diálogo para seleccionar carpeta
    if carpeta:
        entry_ruta_salida.delete(0, tk.END)  # Borra lo que haya en el campo de texto
        entry_ruta_salida.insert(0, carpeta)  # Inserta la ruta seleccionada

# Función para renombrar las imágenes basadas en la carpeta seleccionada
def renombrar_imagenes():
    # Obtener la ruta de la carpeta seleccionada
    ruta_carpeta = entry_ruta_salida.get()  # La misma carpeta donde están las imágenes

    # Verificar que la ruta de salida existe
    if not os.path.exists(ruta_carpeta):
        messagebox.showerror("Error", f"La carpeta {ruta_carpeta} no existe.")
        return

    # Obtener el nombre de la carpeta
    nombre_carpeta = os.path.basename(ruta_carpeta)

    # Listar las imágenes en la carpeta
    imagenes = [f for f in os.listdir(ruta_carpeta) if f.lower().endswith(('.jpg', '.png', '.gif'))]

    if not imagenes:
        messagebox.showerror("Error", "No se encontraron imágenes en la carpeta seleccionada.")
        return

    # Renombrar las imágenes con el nombre de la carpeta y el número secuencial
    for i, imagen in enumerate(imagenes, start=1):
        # Obtener la extensión de la imagen
        extension = os.path.splitext(imagen)[1]
        
        # Nuevo nombre para la imagen con el formato carpeta(n).extensión
        nuevo_nombre = f"{nombre_carpeta}({i}){extension}"
        ruta_imagen = os.path.join(ruta_carpeta, imagen)
        ruta_destino = os.path.join(ruta_carpeta, nuevo_nombre)
        
        # Renombrar la imagen
        os.rename(ruta_imagen, ruta_destino)
        print(f"Imagen {imagen} renombrada a {nuevo_nombre}")

    messagebox.showinfo("Éxito", f"Las imágenes han sido renombradas correctamente en la carpeta {ruta_carpeta}.", icon='info')

# Crear la ventana de la app
ventana = tk.Tk()
ventana.title("Creación Carpetas Repositorio Información Campo")

# Configurar la ventana
ventana.geometry("550x750")

# Título en grande
label_titulo = tk.Label(ventana, text="Creación Carpetas Información Campo", font=("Helvetica", 16, "bold"))
label_titulo.pack(pady=10)

# Frame para la creación de carpetas
frame_carpetas = tk.Frame(ventana)
frame_carpetas.pack(pady=20, padx=10, fill="x")

# Título para la sección de creación de carpetas
label_carpetas = tk.Label(frame_carpetas, text="Creación de Carpetas", font=("Helvetica", 14, "bold"))
label_carpetas.grid(row=0, column=0, columnspan=2)

label_num_inicio = tk.Label(frame_carpetas, text="Nombre inicial de las carpetas (Número):")
label_num_inicio.grid(row=1, column=0, sticky="e", padx=10, pady=5)

entry_num_inicio = tk.Entry(frame_carpetas)
entry_num_inicio.grid(row=1, column=1, padx=5, pady=5)

label_num_carpetas = tk.Label(frame_carpetas, text="Número de carpetas a crear:")
label_num_carpetas.grid(row=2, column=0, sticky="e", padx=5, pady=5)

entry_num_carpetas = tk.Entry(frame_carpetas)
entry_num_carpetas.grid(row=2, column=1, padx=5, pady=5)

# Botón para ejecutar la creación de carpetas
boton_crear = tk.Button(frame_carpetas, text="Crear Carpetas", command=crear_carpetas_secundarias)
boton_crear.grid(row=3, column=0, columnspan=2, pady=10)

# Instructivo para renombrar imágenes
instructivo_imagenes = tk.Label(ventana, text="Instructivo para renombrar imágenes:", font=("Helvetica", 12, "bold"))
instructivo_imagenes.pack(pady=5)

instrucciones = tk.Label(ventana, text="1. Asegúrate de que solo haya imágenes en la carpeta.\n"
                                         "2. Selecciona la carpeta con imágenes.\n"
                                         "3. Haz clic en 'Renombrar Imágenes'.\n"
                                         "4. Las imágenes se renombrarán con el nombre de la carpeta donde se encuentran seguido de su numero en secuencia como: carpeta(1).jpg, carpeta(2).png, etc.", justify="left", wraplength=400)
instrucciones.pack(pady=10)

# Frame para renombrar imágenes
frame_imagenes = tk.Frame(ventana)
frame_imagenes.pack(pady=20, padx=10, fill="x")

# Título para la sección de renombrado de imágenes
label_imagenes = tk.Label(frame_imagenes, text="Renombrar Imágenes", font=("Helvetica", 14, "bold"))
label_imagenes.grid(row=0, column=0, columnspan=2)

# Botón para seleccionar la carpeta de salida
boton_seleccionar_carpeta = tk.Button(frame_imagenes, text="Seleccionar carpeta", command=seleccionar_carpeta)
boton_seleccionar_carpeta.grid(row=1, column=0, columnspan=2, pady=10)

# Campo para la ruta de salida (común para ambas opciones)
label_ruta_salida = tk.Label(frame_imagenes, text="Ruta de salida (Carpeta donde se crearán las carpetas o se renombran las imágenes):")
label_ruta_salida.grid(row=2, column=0, sticky="e", padx=5, pady=5)

entry_ruta_salida = tk.Entry(frame_imagenes)
entry_ruta_salida.grid(row=2, column=1, padx=5, pady=5)

# Botón para renombrar las imágenes
boton_renombrar_imagenes = tk.Button(frame_imagenes, text="Renombrar Imágenes", command=renombrar_imagenes)
boton_renombrar_imagenes.grid(row=3, column=0, columnspan=2, pady=10)

# Mostrar mensaje de créditos en la interfaz principal
label_creditos = tk.Label(ventana, text="Desarrollado por Santiago Cruz - Grupo de Geoquímica Aplicada")
label_creditos.pack(pady=10)

# Iniciar la aplicación
ventana.mainloop()
