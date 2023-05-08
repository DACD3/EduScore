import tkinter as tk
import pandas as pd
import yagmail
from tkinter.font import BOLD
from pandastable import Table, TableModel
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw
from Formulario.F_Clase import Crear_Clases
import os


class MasterPanel:

    #---------------
    # Genera la tabla 
    #---------------
    def Tabla(self, frame):
        self.file_path = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xlsx;*.xlsm")])
        #---------------
        # Lee el archivo exel 
        #---------------
        self.df = pd.read_excel(self.file_path)
        #---------------
        # Crea la tabla 
        #---------------
        self.table = Table(frame, model=TableModel(self.df), width= 650, height= 250)
        self.table.autoResizeColumns()
        #---------------
        # Muestra la tabla 
        #---------------
        self.table.show()

    #---------------
    # Permite guardar los cambios hechos en la tabla
    #---------------
    def SaveTable(self, frame):
        df = self.table
        dfGuardar = df.model.df
        Ruta_Guardado = self.file_path
        #---------------
        # Exporta la informacion de la tabla en .xlsx
        #---------------
        dfGuardar.to_excel(os.path.join(Ruta_Guardado), index=False)
    
    #---------------
    # Permite calcular las calificaciones
    #---------------
    def CalculateTable(self, frame):
        cf = self.table
        #---------------
        # Obtiene los valores de la tabla en un dataFrame
        #---------------
        dfDatos = cf.model.df       
        # Obtiene los valores de la columna: Porcentajes de Evaluacion
        T = dfDatos.iat[0,1]
        E = dfDatos.iat[1,1]
        PF = dfDatos.iat[2,1]
        A = dfDatos.iat[3,1]
        # Obtiene los valores de la columna: Exa. mitad período
        Em1 = dfDatos.iat[0,11]
        Em2 = dfDatos.iat[1,11]
        Em3 = dfDatos.iat[2,11]
        Em4 = dfDatos.iat[3,11]
        Em5 = dfDatos.iat[4,11]
        # Obtiene los valores de la columna: Exa. final período
        Ef1 = dfDatos.iat[0,12]
        Ef2 = dfDatos.iat[1,12]
        Ef3 = dfDatos.iat[2,12]
        Ef4 = dfDatos.iat[3,12]
        Ef5 = dfDatos.iat[4,12]
        # Asigna los valores de la columna: Exa. Total
        Et1 = ((int(Em1) + int(Ef1))*int(E))/200
        dfDatos.iat[0,10] = Et1
        Et2 = ((int(Em2) + int(Ef2))*int(E))/200
        dfDatos.iat[1,10] = Et2
        Et3 = ((int(Em3) + int(Ef3))*int(E))/200
        dfDatos.iat[2,10] = Et3
        Et4 = ((int(Em4) + int(Ef4))*int(E))/200
        dfDatos.iat[3,10] = Et4
        Et5 = ((int(Em5) + int(Ef5))*int(E))/200
        dfDatos.iat[4,10] = Et5
        # Obtiene los valores de la columna: Act 1
        Act1_1 = dfDatos.iat[0,7]
        Act1_2 = dfDatos.iat[1,7]
        Act1_3 = dfDatos.iat[2,7]
        Act1_4 = dfDatos.iat[3,7]
        Act1_5 = dfDatos.iat[4,7]
        # Obtiene los valores de la columna: Act 2
        Act2_1 = dfDatos.iat[0,8]
        Act2_2 = dfDatos.iat[1,8]
        Act2_3 = dfDatos.iat[2,8]
        Act2_4 = dfDatos.iat[3,8]
        Act2_5 = dfDatos.iat[4,8]
        # Obtiene los valores de la columna: Act 3
        Act3_1 = dfDatos.iat[0,9]
        Act3_2 = dfDatos.iat[1,9]
        Act3_3 = dfDatos.iat[2,9]
        Act3_4 = dfDatos.iat[3,9]
        Act3_5 = dfDatos.iat[4,9]
        # Asigna los valores de la columna: Trabajos
        ActT1 = ((int(Act1_1) + int(Act2_1) + int(Act3_1))*int(T))/30
        dfDatos.iat[0,6] = ActT1
        ActT2 = ((int(Act1_2) + int(Act2_2) + int(Act3_2))*int(T))/30
        dfDatos.iat[1,6] = ActT2
        ActT3 = ((int(Act1_3) + int(Act2_3) + int(Act3_3))*int(T))/30
        dfDatos.iat[2,6] = ActT3
        ActT4 = ((int(Act1_4) + int(Act2_4) + int(Act3_4))*int(T))/30
        dfDatos.iat[3,6] = ActT4
        ActT5 = ((int(Act1_5) + int(Act2_5) + int(Act3_5))*int(T))/30
        dfDatos.iat[4,6] = ActT5
        # Obtiene los valores de la columna: Dia 1
        D1_1 = dfDatos.iat[0,15]
        D1_2 = dfDatos.iat[1,15]
        D1_3 = dfDatos.iat[2,15]
        D1_4 = dfDatos.iat[3,15]
        D1_5 = dfDatos.iat[4,15]
        # Obtiene los valores de la columna: Dia 2
        D2_1 = dfDatos.iat[0,16]
        D2_2 = dfDatos.iat[1,16]
        D2_3 = dfDatos.iat[2,16]
        D2_4 = dfDatos.iat[3,16]
        D2_5 = dfDatos.iat[4,16]
        # Obtiene los valores de la columna: Dia 3
        D3_1 = dfDatos.iat[0,17]
        D3_2 = dfDatos.iat[1,17]
        D3_3 = dfDatos.iat[2,17]
        D3_4 = dfDatos.iat[3,17]
        D3_5 = dfDatos.iat[4,17]
        # Obtiene los valores de la columna: Dia 4
        D4_1 = dfDatos.iat[0,18]
        D4_2 = dfDatos.iat[1,18]
        D4_3 = dfDatos.iat[2,18]
        D4_4 = dfDatos.iat[3,18]
        D4_5 = dfDatos.iat[4,18]
        # Obtiene los valores de la columna: Dia 5
        D5_1 = dfDatos.iat[0,19]
        D5_2 = dfDatos.iat[1,19]
        D5_3 = dfDatos.iat[2,19]
        D5_4 = dfDatos.iat[3,19]
        D5_5 = dfDatos.iat[4,19]
        # Obtiene los valores de la columna: Dia 6
        D6_1 = dfDatos.iat[0,20]
        D6_2 = dfDatos.iat[1,20]
        D6_3 = dfDatos.iat[2,20]
        D6_4 = dfDatos.iat[3,20]
        D6_5 = dfDatos.iat[4,20]
        # Obtiene los valores de la columna: Dia 7
        D7_1 = dfDatos.iat[0,21]
        D7_2 = dfDatos.iat[1,21]
        D7_3 = dfDatos.iat[2,21]
        D7_4 = dfDatos.iat[3,21]
        D7_5 = dfDatos.iat[4,21]
        # Obtiene los valores de la columna: Dia 8
        D8_1 = dfDatos.iat[0,22]
        D8_2 = dfDatos.iat[1,22]
        D8_3 = dfDatos.iat[2,22]
        D8_4 = dfDatos.iat[3,22]
        D8_5 = dfDatos.iat[4,22]
        # Obtiene los valores de la columna: Dia 9
        D9_1 = dfDatos.iat[0,23]
        D9_2 = dfDatos.iat[1,23]
        D9_3 = dfDatos.iat[2,23]
        D9_4 = dfDatos.iat[3,23]
        D9_5 = dfDatos.iat[4,23]
        # Obtiene los valores de la columna: Dia 10
        D10_1 = dfDatos.iat[0,24]
        D10_2 = dfDatos.iat[1,24]
        D10_3 = dfDatos.iat[2,24]
        D10_4 = dfDatos.iat[3,24]
        D10_5 = dfDatos.iat[4,24]
        # Asigna los valores de la columna: Asistencia
        DT_1 = ((int(D1_1) + int(D2_1) + int(D3_1) + int(D4_1) + int(D5_1) + int(D6_1) + int(D7_1) + int(D8_1) + int(D9_1) + int(D10_1))*int(A))/10
        dfDatos.iat[0,14] = DT_1
        DT_2 = ((int(D1_2) + int(D2_2) + int(D3_2) + int(D4_2) + int(D5_2) + int(D6_2) + int(D7_2) + int(D8_2) + int(D9_2) + int(D10_2))*int(A))/10
        dfDatos.iat[1,14] = DT_2
        DT_3 = ((int(D1_3) + int(D2_3) + int(D3_3) + int(D4_3) + int(D5_3) + int(D6_3) + int(D7_3) + int(D8_3) + int(D9_3) + int(D10_3))*int(A))/10
        dfDatos.iat[2,14] = DT_3
        DT_4 = ((int(D1_4) + int(D2_4) + int(D3_4) + int(D4_4) + int(D5_4) + int(D6_4) + int(D7_4) + int(D8_4) + int(D9_4) + int(D10_4))*int(A))/10
        dfDatos.iat[3,14] = DT_4
        DT_5 = ((int(D1_5) + int(D2_5) + int(D3_5) + int(D4_5) + int(D5_5) + int(D6_5) + int(D7_5) + int(D8_5) + int(D9_5) + int(D10_5))*int(A))/10
        dfDatos.iat[4,14] = DT_5
        # Obtiene los valores de la columna: Proyecto final
        proyect_1 = dfDatos.iat[0,13]
        PF_1 = (proyect_1 * PF)/100
        proyect_2 = dfDatos.iat[1,13]
        PF_2 = (proyect_2 * PF)/100
        proyect_3 = dfDatos.iat[2,13]
        PF_3 = (proyect_3 * PF)/100
        proyect_4 = dfDatos.iat[3,13]
        PF_4 = (proyect_4 * PF)/100
        proyect_5 = dfDatos.iat[0,13]
        PF_5 = (proyect_5 * PF)/100
        # Asigna los valores de la columna: Calificación final
        # Y a su vez verifica si el estudiante tiene mas de 60 de calificacion final, sino lo reprueba
        CF_1 = int(Et1) + int(ActT1) + int(DT_1) + int(PF_1)
        if CF_1 >= 60:
            dfDatos.iat[0,5] = CF_1
        else:
            dfDatos.iat[0,5] = 'Reprobado'
        CF_2 = int(Et2) + int(ActT2) + int(DT_2) + int(PF_2)
        if CF_2 >= 60:
            dfDatos.iat[1,5] = CF_2
        else:
            dfDatos.iat[1,5] = 'Reprobado'
        CF_3 = int(Et3) + int(ActT3) + int(DT_3) + int(PF_3)
        if CF_3 >= 60:
            dfDatos.iat[2,5] = CF_3
        else:
            dfDatos.iat[2,5] = 'Reprobado'
        CF_4 = int(Et4) + int(ActT4) + int(DT_4) + int(PF_4)
        if CF_4 >= 60:
            dfDatos.iat[3,5] = CF_4
        else:
            dfDatos.iat[3,5] = 'Reprobado'
        CF_5 = int(Et5) + int(ActT5) + int(DT_5) + int(PF_5)
        if CF_5 >= 60:
            dfDatos.iat[4,5] = CF_5
        else:
            dfDatos.iat[4,5] = 'Reprobado'
        #---------------
        # Restablece la tabla con los nuevos valores
        #---------------
        cf.transpose
        cf.redraw()

    #---------------
    # Manda correos de las calificaciones a los usuarios
    #---------------

    def send_email(self, destinatario, mensaje):
        # Credenciales del remitente
        email = 'usuariodephytonudg@gmail.com'
        contraseña = 'zzyaanorwxjqajlk'
        yag = yagmail.SMTP(user=email,password=contraseña)
        
        # Contenido del correo
        asunto = 'Informe de calificaciones:'
        yag.send(destinatario, asunto, mensaje)


    def email_sender(self, frame):
        kf = self.table
        #---------------
        # Obtiene los valores de la tabla en un dataFrame
        #---------------
        zfDatos = kf.model.df
        # Datos de los nombres de los estudiantes
        N1 = zfDatos.iat[0,3]
        N2 = zfDatos.iat[1,3]
        N3 = zfDatos.iat[2,3]
        N4 = zfDatos.iat[3,3]
        N5 = zfDatos.iat[4,3]
        # Datos de los correos de los estudiantes
        C1 = zfDatos.iat[0,4]
        C2 = zfDatos.iat[1,4]
        C3 = zfDatos.iat[2,4]
        C4 = zfDatos.iat[3,4]
        C5 = zfDatos.iat[4,4]
        # Datos de la calificacion de estudiantes
        Cal1 = zfDatos.iat[0,5]
        Cal2 = zfDatos.iat[1,5]
        Cal3 = zfDatos.iat[2,5]
        Cal4 = zfDatos.iat[3,5]
        Cal5 = zfDatos.iat[4,5]
        # Credenciales de los destinatarios
        destinatarios = [
            {'email': 'cervantesdiazdiegoantonio@gmail.com', 'calif': str(Cal1), 'nombre': str(N1)},
            {'email': 'cervantesdiazdiegoantonio@gmail.com', 'calif': str(Cal2), 'nombre': str(N2)},
            {'email': 'cervantesdiazdiegoantonio@gmail.com', 'calif': str(Cal3), 'nombre': str(N3)},
            {'email': 'cervantesdiazdiegoantonio@gmail.com', 'calif': str(Cal4), 'nombre': str(N4)},
            {'email': 'cervantesdiazdiegoantonio@gmail.com', 'calif': str(Cal5), 'nombre': str(N5)},
        ]

        for destinatario in destinatarios:
            mensaje = f'Al Estudiante: {destinatario["nombre"]}.\nPor este medio se le envía un informe de las calificacion final que tuvo este semestre:\n\n Calificación final: {destinatario["calif"]}\n\n En caso de algún error o discomformidad con el resultados, favor de contactar directamente a su profesor'
            self.send_email(destinatario['email'], mensaje)

    # V1.0
    #def SendEmail(self, frame):
        # Credenciales del remitente
    #    email = 'usuariodephytonudg@gmail.com'
    #    contraseña = 'zzyaanorwxjqajlk'

    #    yag = yagmail.SMTP(user=email,password=contraseña)
    #    # Credenciales del destinatario
    #    destinatarios = ['cervantesdiazdiegoantonio@gmail.com']
        # Contenido del correo
    #    asunto = 'Informe de calificaciones:'
    #    mensaje = 'Por este medio se envia un informe de las calificiones que tuvo este semestre:\n\n Trabajos: 35/40 \n Asistencias: 10/10 \n Examenes: 20/30 \n Proyecto Final: 15/20 \n Calificación Total: 80/100 \n\n En caso de algun error en los resultados, favor de contactar directamente a su profesor'
  
        # Creación del mensaje
    #    yag.send(destinatarios, asunto, mensaje)
        
    #---------------
    # inicia la ventana 
    #---------------    
    def __init__(self):        

        super().__init__()

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
        # Contiene la ruta de la imagen predeterminada
        #---------------
        ruta_imagen_predeterminada = "imagenes\\YO ALGUN PEDO .png"
        #---------------
        # Esta permite colocar una mascara circular en una fotografia la cual puede seleccionar el usuario, y sirve como foto de usuario
        #--------------- 
        def cargar_imagen(event):
            # Filtro de archivo para solo mostrar archivos de imagen
            tipos_archivo = [("Archivos PNG", "*.png"), ("Archivos JPEG", "*.jpeg;*.jpg")]
            ruta_archivo = filedialog.askopenfilename(filetypes=tipos_archivo) # Abrir diálogo de archivo con filtro
            if ruta_archivo:
                imagen = Image.open(ruta_archivo) # Abrir imagen con PIL
                mask = Image.new("L", imagen.size, 0)
                draw = ImageDraw.Draw(mask)
                draw.ellipse((0, 0, imagen.size[0], imagen.size[1]), fill=255)
                imagen.putalpha(mask)
                imagen = imagen.resize((100, 100)) # Redimensionar imagen a 400x400
                imagen = ImageTk.PhotoImage(imagen) # Convertir imagen a formato compatible con Tkinter
                etiqueta.config(image=imagen) # Mostrar imagen en la etiqueta
                etiqueta.image = imagen # Actualizar referencia a la imagen para evitar que sea borrada por el recolector de basura

        # Cargar imagen predeterminada
        image = Image.open(ruta_imagen_predeterminada)
        mask = Image.new("L", image.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, image.size[0], image.size[1]), fill=255)
        image.putalpha(mask)
        image = image.resize((100, 100), Image.ANTIALIAS)
        photo_imagen = ImageTk.PhotoImage(image)
        
        # Etiqueta que contiene a la imagen
        etiqueta = tk.Label(frame_left, image=photo_imagen, bg="#313745", bd=0, highlightthickness=0)
        etiqueta.image = photo_imagen
        etiqueta.place(x=10, y=10)
        etiqueta.pack()

        # Configurar evento de clic en la etiqueta para cargar la imagen
        etiqueta.bind("<Button-1>", cargar_imagen) # Llamar a la función cargar_imagen() cuando se haga clic en la etiqueta

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
        # frame superior derecho muestra un calendario escolar 
        #---------------
        frame_calendario = tk.Frame(frame_master, bd= 2, relief= 'solid', bg= '#777777', width= 455, height= 465)
        frame_calendario.pack(side= 'right',padx= 20, pady= 20)
        frame_calendario.place(x= 730, y= 10)
        #---------------
        # Muestra el calendario escolar
        #---------------
        ima_calendar = Image.open("imagenes\\calendario.png")
        ima_calendar = ima_calendar.resize((445, 455), Image.ANTIALIAS)
        calendario_ima = ImageTk.PhotoImage(ima_calendar)
        label = tk.Label(frame_calendario, image=calendario_ima, bg="#313745", bd=0, highlightthickness=0)
        label.image = calendario_ima
        label.place(x=1, y=1)
        label.pack()
        #---------------
        # frame inferior izquierdo este debera contener las clases las cuales tendran la funcion que al dar click
        # en una de ellas abra un archivo de exel respectivo a la clase seleccionada.
        #---------------
        # frame_clases = tk.Frame(frame_master, bd= 0, relief= tk.SOLID, bg= '#FFFFFF', width= 700, height= 340)
        # frame_clases.pack(side= 'right',padx= 20, pady= 20)
        # frame_clases.place(x= 10, y= 320)
        #---------------
        # Boton para abrir archivo .xlsx en la tabla
        #---------------
        boton_Abrir = tk.Button(frame_master, text= "Abrir archivo", width= 14, font= ("Gidole Regular", 15), bd= 2, relief= "solid", bg = '#777777', fg= 'black', command= lambda:self.Tabla(farme_descripcion))
        boton_Abrir.pack(side= "right" ,padx= 200, pady= 10)
        boton_Abrir.place(x= 170, y= 540)
        boton_Abrir.bind("<Return>", (lambda event: self.Tabla(farme_descripcion)))
        #---------------
        # Boton para guardar cambios en la tabla
        #--------------
        boton_Save = tk.Button(frame_master, text= "Guardar cambios", font= ("Gidole Regular", 15), bd= 2, relief= "solid", bg = '#777777', fg= 'black', command= lambda:self.SaveTable(farme_descripcion))
        boton_Save.pack(side= "right" ,padx= 200, pady= 10)
        boton_Save.place(x= 370, y= 540)
        #---------------
        # Boton para calcular las calificaciones de la tabla
        #--------------
        boton_Calcular = tk.Button(frame_master, text= "Calcular calif", font= ("Gidole Regular", 15), bd= 2, relief= "solid", bg = '#777777', fg= 'black', command= lambda:self.CalculateTable(farme_descripcion))
        boton_Calcular.pack(side= "right" ,padx= 200, pady= 10)
        boton_Calcular.place(x= 570, y= 540)
        #---------------
        # Boton para crear un excel de la clase
        #--------------
        boton_Crear = tk.Button(frame_master, text= "Crear clase", font= ("Gidole Regular", 15), bd= 2, relief= "solid", bg = '#777777', fg= 'black', command= Crear_Clases)
        boton_Crear.pack(side= "right" ,padx= 200, pady= 10)
        boton_Crear.place(x= 20, y= 540)
        #---------------
        # Boton para mandar correo de calificaciones a estudiantes
        #--------------
        boton_Correo = tk.Button(frame_master, text= "Mandar calificaciones", font= ("Gidole Regular", 15), bd= 2, relief= "solid", bg = '#777777', fg= 'black', command= lambda:self.email_sender(farme_descripcion))
        boton_Correo.pack(side= "right" ,padx= 200, pady= 10)
        boton_Correo.place(x= 280, y= 600)
        #--------------
        self.ventana.mainloop()
        