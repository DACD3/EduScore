# Jose Antonio Garcia Peña : Diseño :)
#
#

#05/04/2023
# tk y ttk son bases de diseño para mejorar la apariencia de los widjes(objetos como etiquetas, botones, etc.)


import tkinter as tk
import util.generic as utl
import pickle as Pi
from util.BotonRedondeado import RoundedButton
from tkinter import *
from tkinter.font import BOLD
from tkinter import ttk, messagebox
from Formulario.F_Master import MasterPanel
from Formulario.F_Registrar import Registrar_Panel

class App:

    #---------------
    # Funcion que permite verificar los datos de usuario y contraseña
    #---------------
    def verificar(self):

        #---------------
        # Obtiene el diccionario donde se encuentran los usuarios
        #---------------
        with open("Docs\\Usuarios.pkl", "rb") as archivo:
           users = Pi.load(archivo)

        #---------------
        # Obtiene los valores de usuario y contraseña introducidos por el usuario.
        #---------------
        usu = self.user.get()
        password = self.password.get()   

        #---------------
        # Verifica que los datos de correo y contraseña adquiridos correspondan con los registros en el diccionario de usuarios
        #---------------
        if usu not in users :
            messagebox.showerror(message="El correo es incorrecto",title="Mensaje")
            self.user.delete(0, 'end')            
            self.password.delete(0, 'end')
        else:
            if users[usu] != password:
                messagebox.showerror(message="La contraseña no es correcta",title="Mensaje")
                self.user.delete(0, 'end')            
                self.password.delete(0, 'end')
            else:
                self.ventana.destroy()
                MasterPanel()
    
    def __init__(self):

        #---------------
        # Generacion de la ventana.
        #---------------
        self.ventana = tk.Tk()                             
        self.ventana.title('Inicio de sesion')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)  
        #---------------
        # Este permite centrar la ventana
        #---------------  
        utl.centrar_ventana(self.ventana,800,600)

        #---------------
        # Dentro de nuestra ventana(bd= no tenga bordes, height= tamaño vertical, relief= que este sea solido,
        # padx= son la distancia que este respetara entre otros componentes, bg = el color de fondo el cual este tomara)
        #---------------
        frame_login = tk.Frame(self.ventana, bd= 0, relief= tk.SOLID, pady= 0, bg= '#313745')
        #---------------
        # Generamos un bloque con frame_logo.pack(este enpaqueta el componente ), side= entregamos la posicion en la cual 
        # se va a colocar el frame, expand= desidimos si este se va aexpandir, fill= con  este comando hacemos que el 
        # frame se apegue a las posicion de x, y. 
        #---------------
        frame_login.pack(side= "right", expand= tk.YES, fill= tk.BOTH)
        #---------------
        
        #--------------
        frame_title = tk.Frame(frame_login, bd= 0, height=120, relief= tk.SOLID, bg= '#313745')
        frame_title.pack(side= "top", fill= tk.X)
        #---------------
        # Creamos una etiqueta la cuan desplegaremos en nuestro frame (tk.Lable(frame_title), image= colocamos la variable 
        # que contiene la imagen que deseamos colocar, seleccionamos el color de fondo).
        #---------------
        label_titulo = tk.Label(frame_title, text= "EDU",font= ('kollektief', 68, "bold"),fg= "#FFFFFF", bg= '#313745')
        label_titulo.config(text=label_titulo.cget("text") + " SCORE", font=("Gidole Regular", 68), fg="#FFFFFF")
        label_titulo.pack(expand= tk.YES, fill= tk.BOTH)
        #---------------
        
        #--------------
        frame_Container = tk.Frame(frame_login, bd= 0, relief= tk.SOLID, bg= '#313745')
        frame_Container.pack(side= "bottom", expand= tk.YES, fill= tk.BOTH)
        #---------------
        
        #--------------
        label_eslogan = tk.Label(frame_login, text= "Una nueva forma de aprender",font= ('Gidole Regular', 18),fg= "#FFFFFF", bg= '#313745')
        label_eslogan.pack(fill= tk.X, padx= 80, pady=5)
        #---------------
        # Colocamos el frame y le damos indicaciones de apartir de que pixel se desplegara, 
        # label.place(x= pixel inicial en el eje x, y= pixel inicial en el eje y,  relwidth=, relheight= ambos indican que 
        # la etiqueta abarquen todo el ancho y largo del frame).
        # En este caso estamos solisitando que se posicione en un cierto punto cardinal, este caso es para el ESTE.
        # De esta manera enpaquetamos por bloques 
        #---------------
        label_user = tk.Label(frame_login, text= "Usuario", font= ('Gidole Regular', 30), fg= "#FFFFFF", bg= '#313745', anchor= "w")
        label_user.pack(fill= tk.X, padx= 200, pady= 30)
        #---------------
        # Boton el cual llevara al usuario al formulario de registro 
        # falta eliminar la ventana anterior.
        #---------------
        button_Cuenta = tk.Button(frame_login, text= "Iniciar sesion", font= ("Gidole Regular", 12, BOLD, 'underline'), bg = '#313745', fg= '#777777' ,bd= 0, command= Registrar_Panel)
        button_Cuenta.pack(padx= 200, pady= 10)  
        button_Cuenta.place(x= 200, y= 240)
        #---------------
        # Genetamos la caja de texto con el entry y la empaquetamos 
        # Entry es cun texbox o caja de texto el cual puede resivir informacion del ususario atraves del teclado.
        #---------------
        self.user = ttk.Entry(frame_login, font= ("Gidole Regular", 16))
        self.user.pack(fill= tk.X, padx= 200, pady=5)
        #---------------
        # Creamos una etiqueta la cual tiene por texto Contraseña
        #---------------
        etq_pasword = tk.Label(frame_login, text= "Contraseña", font= ('Gidole Regular', 30), fg= '#FFFFFF', bg= '#313745', anchor= "w")
        etq_pasword.pack(fill= tk.X, padx= 200, pady= 5)
        #---------------
        # Esta instancia nos permite resivir una contraseña escrita por el usuario.
        #---------------
        self.password = ttk.Entry(frame_login, font= ("Gidole Regular", 16))
        self.password.pack(fill= tk.X, padx= 200, pady=5)
        #---------------
        # Colocamos una configuracion o funcionalidad al objeto creado en este caso al escribir la contraseña la caja de texto solo
        # mostrara un * enlugar de los caracteres ingresados por el usuario. 
        #---------------
        self.password.config(show= "*")
        #---------------
        # Generamos un boton el cual cumpla la funcion de verificar si el usuario y contaseña son correctos
        #---------------
        # button_inicio = tk.Button(frame_form_fill, text= "Iniciar sesion", font= ("Gidole Regular", 15, BOLD), bg = '#777777', fg= '#FFFFFF', command= self.verificar)
        # button_inicio.pack(side= "right" ,padx= 200, pady= 10)        
        button_inicio = RoundedButton(frame_login, 140, 40, 5, 0, '#474E60', '#313745', command= self.verificar, text='Continuar')
        button_inicio.pack(side= "right" ,padx= 200, pady= 10)
        #---------------
        # El tipo bind es para indicar un tipo de evento que queramos resivir en este caso si resivimos un enter, con una funcion lamda
        # vamos a indicar que se dispare el evento.
        #---------------
        button_inicio.bind("<Return>", (lambda event: self.verificar))
        #---------------
        # Este permite ejecutar la ventana 
        #---------------
        self.ventana.mainloop()

if __name__ == "__main__":
   App()