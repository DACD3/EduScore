# Jose Antonio Garcia Peña (Diseño)
#
# 18/04/2023

import tkinter as tk
import util.generic as utl
from util.BotonRedondeado import RoundedButton
from tkinter import *
from tkinter.font import BOLD
from tkinter import ttk, messagebox
# from Formulario.F_Master import MasterPanel
# from Formulario.F_Registrar import Registrar_Panel

class Crear_Clases:
    
    #---------------
    # generar ventana.
    #---------------
    def __init__(self):
        self.ventana = tk.Tk()                             
        self.ventana.title('Creacion de clase')
        self.ventana.geometry('900x600')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)  
        utl.centrar_ventana(self.ventana, 600, 400)
        
        #---------------
        # Frame principal de la ventana.
        #---------------
        frame_Clase = tk.Frame(self.ventana, bd = 0, relief= tk.SOLID, bg= '#FFFFFF')
        frame_Clase.pack(side = "top", expand= tk.YES, fill= tk.BOTH)
        #---------------
        # Frame contenedor del titulo.
        #---------------
        frame_title = tk.Frame(frame_Clase, bd= 0, height=60, relief= tk.SOLID, bg='#FFFFFF')
        frame_title.pack(side= "top", fill= tk.X)
        #---------------
        # Titulo.
        #---------------
        titulo = tk.Label(frame_title, bd= 0, text= "Crea una clase", font= ('kollektief', 48, 'bold'), fg= '#FFFFFF', bg= '#313745')
        titulo.pack(expand= tk.YES, fill= tk.BOTH)
        #---------------
        # Frame contenedor este contendra el resto de los widjes.
        #---------------
        frame_Contenedor = tk.Frame(frame_Clase, bd= 0, relief= tk.SOLID, bg= '#313745')
        frame_Contenedor.pack(side= 'bottom', expand= tk.YES, fill= tk.BOTH)
        #---------------
        # Etiqueta alumnos.
        #---------------
        label_alumnos = tk.Label(frame_Contenedor, text= "Cantidad de alumnos", font=('Gidole Regular', 12), fg= '#FFFFFF', bg= '#313745', anchor= 'w')
        label_alumnos.pack(fill= tk.X, padx= 70)
        label_alumnos.place(x= 70, y= 10)
        #---------------
        # Entry alumnos.
        #---------------
        Cant_Alumnos = tk.Entry(frame_Contenedor, font= ('Gidole Regular', 12))
        Cant_Alumnos.pack(fill= tk.X, padx= 70, pady= 10)
        Cant_Alumnos.place(x= 70, y= 40)
        #---------------
        # Etiqueta examen.
        #---------------
        label_Examen = tk.Label(frame_Contenedor, text= "Porcentaje de examen", font=('Gidole Regular', 12), fg= '#FFFFFF', bg= '#313745', anchor= 'w')
        label_Examen.pack(fill= tk.X, padx= 70)
        label_Examen.place(x= 70, y= 70)
        #---------------
        # Entry examen.
        #---------------
        Por_Examen = tk.Entry(frame_Contenedor, font= ('Gidole Regular', 12))
        Por_Examen.pack(fill= tk.X, padx= 70, pady= 10)
        Por_Examen.place(x= 70, y= 100)
        #---------------
        # Etiqueta tarea.
        #---------------
        label_Tarea = tk.Label(frame_Contenedor, text= "Porcentaje de tarea", font=('Gidole Regular', 12), fg= '#FFFFFF', bg= '#313745', anchor= 'w')
        label_Tarea.pack(fill= tk.X, padx= 70)
        label_Tarea.place(x= 70, y= 130)
        #---------------
        # Entry tarea.
        #---------------
        Por_Tarea = tk.Entry(frame_Contenedor, font= ('Gidole Regular', 12))
        Por_Tarea.pack(fill= tk.X, padx= 70, pady= 10)
        Por_Tarea.place(x= 70, y= 160)
        #---------------
        # Etiqueta Asistencia.
        #---------------
        label_Asistencia = tk.Label(frame_Contenedor, text= "Porcentaje por asistencia", font=('Gidole Regular', 12), fg= '#FFFFFF', bg= '#313745', anchor= 'w')
        label_Asistencia.pack(fill= tk.X, padx= 70)
        label_Asistencia.place(x= 350, y= 10)
        #---------------
        # Entry Asistencia.
        #---------------
        Por_Asistencia = tk.Entry(frame_Contenedor, font= ('Gidole Regular', 12))
        Por_Asistencia.pack(fill= tk.X, padx= 70, pady= 10)
        Por_Asistencia.place(x= 350, y= 40)
        #---------------
        # Etiqueta Asistencia, aproximacion de aistencia.
        #---------------
        label_Aprox_Asistencia = tk.Label(frame_Contenedor, text= "Dias aproximados del ciclo.", font=('Gidole Regular', 12), fg= '#FFFFFF', bg= '#313745', anchor= 'w')
        label_Aprox_Asistencia.pack(fill= tk.X, padx= 70)
        label_Aprox_Asistencia.place(x= 350, y= 70)
        #---------------
        # Entry Asistencia, aproximacion de aistencia.
        #---------------
        Cant_Dias = tk.Entry(frame_Contenedor, font= ('Gidole Regular', 12))
        Cant_Dias.pack(fill= tk.X, padx= 70, pady= 10)
        Cant_Dias.place(x= 350, y= 100)
        #---------------
        # Etiqueta proyecto final.
        #---------------
        label_Aprox_Asistencia = tk.Label(frame_Contenedor, text= "Porcentaje por proyecto final.", font=('Gidole Regular', 12), fg= '#FFFFFF', bg= '#313745', anchor= 'w')
        label_Aprox_Asistencia.pack(fill= tk.X, padx= 70)
        label_Aprox_Asistencia.place(x= 350, y= 130)
        #---------------
        # Entry proyecto final.
        #---------------
        Cant_Dias = tk.Entry(frame_Contenedor, font= ('Gidole Regular', 12))
        Cant_Dias.pack(fill= tk.X, padx= 70, pady= 10)
        Cant_Dias.place(x= 350, y= 160)
        #---------------
        # ejecuta la bentana.
        #---------------
        button_inicio = RoundedButton(frame_Contenedor, 140, 40, 5, 0, '#474E60', '#313745', text='Crear clase')
        button_inicio.pack (side= 'right', padx= 70, pady= 0)
        button_inicio.place(x= 220, y= 220)
        #---------------
        # ejecuta la bentana.
        #---------------
        self.ventana.mainloop()


