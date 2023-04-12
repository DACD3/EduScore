import tkinter as tk
import pandas as pd
from PIL import ImageTk, Image, ImageDraw
from pandastable import Table, TableModel
from tkinter import filedialog

# ayuda a redimencionar una imagen  a un tamaño especificado por eñl usuario.
def leer_imagen(path, size):
    return ImageTk.PhotoImage(Image.open(path).resize(size, Image.ANTIALIAS))

# Esta nos permite que al crear nuestra ventana la podamos colocar en el sentro de la 
# pantalla.
def centrar_ventana(ventana,aplicacion_ancho,aplicacion_largo):    
    pantall_ancho = ventana.winfo_screenwidth()
    pantall_largo = ventana.winfo_screenheight()
    x = int((pantall_ancho/2) - (aplicacion_ancho/2))
    y = int((pantall_largo/2) - (aplicacion_largo/2))
    return ventana.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}")

# Esta funcion nos permite crear una imagen con una mascara circular mostrando una 
# imagen redonda
def Foto_personal(frame, file_path, x, y, width=None, height=None):
    # Cargamos la imagen
    image = Image.open(file_path)
    
    # Creamos una máscara circular
    mask = Image.new("L", image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, image.size[0], image.size[1]), fill=255)

    # Aplicamos la máscara a la imagen
    image.putalpha(mask)

    # Si se especificó ancho o alto, redimensionamos la imagen
    if width or height:
        image = image.resize((width, height), Image.ANTIALIAS)

    # Creamos el objeto PhotoImage a partir de la imagen
    photo_image = ImageTk.PhotoImage(image)

    # Creamos un label y le asignamos la imagen y el fondo transparente
    label = tk.Label(frame, image=photo_image, bg="#313745", bd=0, highlightthickness=0)
    label.image = photo_image
    label.place(x=x, y=y)

    return label

def Tabla(frame):
    file_path = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xlsx;*.xlsm")])

    # Read the Excel file into a Pandas DataFrame
    df = pd.read_excel(file_path)

    # Create a PandasTable object and set its model to the DataFrame
    table = Table(frame, model=TableModel(df), width= 650, height= 250)

    # Show the table
    table.show()

def SaveTable(df):
    ruta_archivo = filedialog.asksaveasfilename(filetypes=[("Archivo de Excel", "*.xlsx")])
    df.to_excel(ruta_archivo, index=False)
