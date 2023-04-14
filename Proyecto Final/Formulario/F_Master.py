import tkinter as tk
import pandas as pd
from tkinter.font import BOLD
import util.generic as utl
from pandastable import Table, TableModel
from tkinter import filedialog


class MasterPanel:

    # Esto lo deberan de modificar ARAM y DIego.

    #---------------
    # genera la tabla 
    #---------------
    def Tabla(self, frame):
        self.file_path = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xlsx;*.xlsm")])
    #---------------
    # lee el archivo exel 
    #---------------
        self.df = pd.read_excel(self.file_path)
    #---------------
    # Crea la tabla 
    #---------------
        self.table = Table(frame, model=TableModel(self.df), width= 650, height= 250)
    #---------------
    # Muestra la tabla 
    #---------------
        self.table.show()

    #---------------
    # Permite guardar los cambios echos en la tabla 
    #---------------
    def SaveTable(self, frame):
        self.ruta_archivo = filedialog.asksaveasfilename(filetypes=[("Archivo de Excel", "*.xlsx")])
        df = self.Tabla(frame)
        df.to_excel(self.ruta_archivo, index=False)

    #---------------
    # inicia la ventana 
    #---------------    
    def __init__(self):        

        #---------------
        # generar ventana
        #---------------
        self.ventana = tk.Tk()                             
        self.ventana.title('Master panel')
        self.ventana.geometry("1300x730")
        self.ventana.config(bg='#fcfcfc')
        
        #---------------
        # frame superior.
        #---------------
        frame_top = tk.Frame(self.ventana, bd= 0, height= 60, relief= tk.SOLID, pady= 0, bg= '#313745')
        frame_top.pack(side= "top", expand= tk.NO, fill= tk.BOTH)
        #---------------
        # frame lateral.
        # A este sele podran agregar funciones futuras no planeadas por el momento.
        #---------------
        frame_left = tk.Frame(self.ventana, bd= 0, width= 120, relief= tk.SOLID, pady= 0, bg= '#313745')
        frame_left.pack(side= "left", expand= tk.NO, fill= tk.BOTH)
        #---------------
        # Esta permite colocar una mascara circular en una fotografia esta debera ser modificada para 
        # resivir una imagen seleccionada por el usuario, (Aram y Diego).
        #---------------
        utl.Foto_personal(frame_left, "imagenes\YO ALGUN PEDO .png", 10, 10, 100, 100)
        #---------------
        # Este es el frame maestro el cual contiene el resto de los widjets en una posicion especifica.
        #---------------
        frame_master = tk.Frame(self.ventana, bd= 0, relief= tk.SOLID, pady= 0, bg= '#777777')
        frame_master.pack(expand= tk.YES, fill= tk.BOTH)
        #---------------
        # frame ubicado en la parte superior izquierda el cual toma una tabla de exel para mostrar
        # esta es posible modificar 
        #---------------
        farme_descripcion = tk.Frame(frame_master, bd= 2, relief= "solid", bg='#FFFFFF', width= 700, height=500)
        farme_descripcion.pack(side='left', expand= tk.NO, padx= 20, pady= 20)
        farme_descripcion.place(x= 10, y= 10 )
        #---------------
        # frame superior derecho este debera fermitir mostrar un calendario escolar 
        # FUNCION aun no añadida es necesario añadir( Aram y Diego)
        #---------------
        frame_calendario = tk.Frame(frame_master, bd= 2, relief= 'solid', bg= '#777777', width= 440, height= 300)
        frame_calendario.pack(side= 'right',padx= 20, pady= 20)
        frame_calendario.place(x= 730, y= 10)
        #---------------
        # frame inferior izquierdo este debera contener las clases las cuales tendran la funcion que al dar click
        # en una de ellas abra un archivo de exel respectivo a la clase seleccionada.
        #---------------
        # frame_clases = tk.Frame(frame_master, bd= 0, relief= tk.SOLID, bg= '#FFFFFF', width= 700, height= 340)
        # frame_clases.pack(side= 'right',padx= 20, pady= 20)
        # frame_clases.place(x= 10, y= 320)
        #---------------
        #
        #---------------
        boton_Abrir = tk.Button(frame_master, text= "abrir archivo", width= 14, font= ("Gidole Regular", 15), bd= 2, relief= "solid", bg = '#777777', fg= 'black', command= lambda:self.Tabla(farme_descripcion))
        boton_Abrir.pack(side= "right" ,padx= 200, pady= 10)
        boton_Abrir.place(x= 800, y= 340)
        boton_Abrir.bind("<Return>", (lambda event: self.Tabla(farme_descripcion)))
        #---------------
        
        #--------------
        boton_Save = tk.Button(frame_master, text= "Guardar cambios", font= ("Gidole Regular", 15), bd= 2, relief= "solid", bg = '#777777', fg= 'black', command= lambda:self.SaveTable(farme_descripcion))
        boton_Save.pack(side= "right" ,padx= 200, pady= 10)
        boton_Save.place(x= 800, y= 390)
        #---------------
        
        #--------------
        self.ventana.mainloop()