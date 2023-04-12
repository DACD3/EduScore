import tkinter as tk
import pandas as pd
from tkinter.font import BOLD
import util.generic as utl
from pandastable import Table, TableModel
from tkinter import filedialog


class MasterPanel:
    
    def Tabla(self, frame):
        self.file_path = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xlsx;*.xlsm")])

    # Read the Excel file into a Pandas DataFrame
        self.df = pd.read_excel(self.file_path)

    # Create a PandasTable object and set its model to the DataFrame
        self.table = Table(frame, model=TableModel(self.df), width= 650, height= 250)

    # Show the table
        self.table.show()

    def SaveTable(self, df):
        self.ruta_archivo = filedialog.asksaveasfilename(filetypes=[("Archivo de Excel", "*.xlsx")])
        df.to_excel(self.ruta_archivo, index=False)


    def __init__(self):        
        self.ventana = tk.Tk()                             
        self.ventana.title('Master panel')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        #self.ventana.geometry("1300x730")
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)    
               
        
        frame_top = tk.Frame(self.ventana, bd= 0, height= 60, relief= tk.SOLID, pady= 0, bg= '#313745')
        frame_top.pack(side= "top", expand= tk.NO, fill= tk.BOTH)

        frame_left = tk.Frame(self.ventana, bd= 0, width= 120, relief= tk.SOLID, pady= 0, bg= '#313745')
        frame_left.pack(side= "left", expand= tk.NO, fill= tk.BOTH)

        utl.Foto_personal(frame_left, "imagenes\YO ALGUN PEDO .png", 10, 10, 100, 100)

        frame_master = tk.Frame(self.ventana, bd= 0, relief= tk.SOLID, pady= 0, bg= '#777777')
        frame_master.pack(expand= tk.YES, fill= tk.BOTH)

        farme_descripcion = tk.Frame(frame_master, bd= 2, relief= "solid", bg='#FFFFFF', width= 00, height=300)
        farme_descripcion.pack(side='left', expand= tk.NO, padx= 20, pady= 20)
        farme_descripcion.place(x= 10, y= 10 )

        frame_calendario = tk.Frame(frame_master, bd= 2, relief= 'solid', bg= '#777777', width= 300, height= 300)
        frame_calendario.pack(side= 'right',padx= 20, pady= 20)
        frame_calendario.place(x= 730, y= 10)

        frame_clases = tk.Frame(frame_master, bd= 0, relief= tk.SOLID, bg= '#FFFFFF', width= 700, height= 340)
        frame_clases.pack(side= 'right',padx= 20, pady= 20)
        frame_clases.place(x= 10, y= 320)

        # file_path = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xlsx;*.xlsm")])
        # # # # Read the Excel file into a Pandas DataFrame
        # df = pd.read_excel(file_path)
        # # # # Create a PandasTable object and set its model to the DataFrame
        # table = Table(farme_descripcion, model=TableModel(df), width= 650, height= 250)
        # # # # Show the table
        # table.show()
        # df.to_excel('Archivo.xlsx', index= False)

        #tabla = utl.Tabla(farme_descripcion)
        #save = utl.SaveTable(tabla)

        boton_Save = tk.Button(frame_master, text= "abrir archivo", font= ("Gidole Regular", 15, BOLD), bd= 0, bg = '#777777', fg= '#FFFFFF', command= lambda:self.Tabla(farme_descripcion))
        boton_Save.pack(side= "right" ,padx= 200, pady= 10)
        boton_Save.place(x= 720, y= 340)
        boton_Save.bind("<Return>", (lambda event: self.Tabla(farme_descripcion)))
        boton_Save = tk.Button(frame_master, text= "Guardar Cambios", font= ("Gidole Regular", 15, BOLD), bd= 0, bg = '#777777', fg= '#FFFFFF', command= lambda:self.SaveTable(self.Tabla()))
        boton_Save.pack(side= "right" ,padx= 200, pady= 10)
        boton_Save.place(x= 720, y= 360)

        self.ventana.mainloop()