from util.BotonRedondeado import RoundedButton
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl

class Registrar_Panel:

    def __init__(self):
        
        #---------------
        # generacion de la ventana
        #---------------
        self.ventana = tk.Tk()
        self.ventana.title('Registrar')
        self.ventana.geometry("400x600+10+10")
        self.ventana.config(bg= '#fcfcfc')
        self.ventana.resizable(width=0, height= 0)
        utl.centrar_ventana(self.ventana,700,500)
        #---------------
        # Frame principal 
        #---------------
        frame_register = tk.Frame(self.ventana, bd= 0, relief= tk.SOLID, bg='#FFFFFF')
        frame_register.pack(side= "right",expand= tk.YES, fill= tk.BOTH)
        #---------------
        # Muestra el encavesado de la ventana
        #---------------
        frame_title = tk.Frame(frame_register, bd= 0, height=30, relief= tk.SOLID, bg= '#FFFFFF')
        frame_title.pack(side= "top", fill= tk.X)
        #---------------
        
        #---------------
        title = tk.Label(frame_title, text= "Crea una cuenta de Edu Score", font=('kollektief', 28, BOLD), fg= '#FFFFFF', bg= '#313745', pady= 30)
        title.pack(expand= tk.YES, fill= tk.BOTH)
        #---------------
        # Muestra los datos del correo electronico   
        #---------------
        frame_Container = tk.Frame(frame_register, height= 80, bd= 0, relief= tk.SOLID, bg= '#313745')
        frame_Container.pack(side= "bottom", expand= tk.YES, fill= tk.BOTH)
        #---------------

        #---------------
        Correo = tk.Label(frame_Container, text= "Escribe tu correo de docente",font=("Gidole Regular", 22), fg= '#FFFFFF', bg= '#313745', anchor="w")
        Correo.pack(fill= tk.X, padx= 80, pady=5)
        #---------------
        # esto es para instanciarlo y recopilar la informacion en la base de datos mediante una duncion.
        #---------------
        self.usuario = ttk.Entry(frame_Container, font= ("Gidole Regular", 22))
        self.usuario.pack(fill=tk.X, padx= 80, pady= 10)
        #---------------

        #---------------
        Password = tk.Label(frame_Container, text= "Escribe una contraseña",font=("Gidole Regular", 22), fg= '#FFFFFF', bg= '#313745', anchor="w")
        Password.pack(fill= tk.X, padx= 80, pady=5)
        #---------------
        # esto es para instanciarlo y recopilar la informacion en la base de datos mediante una duncion.
        #---------------
        self.Password = ttk.Entry(frame_Container, font= ("Gidole Regular", 22))
        self.Password.pack(fill=tk.X, padx= 80, pady= 10)
        self.Password.config(show= "*")
        #---------------

        #---------------
        Password_Boot = tk.Label(frame_Container, text= "Minimo 8 Caracteres, letras y numeros", font=("Gidole Regular", 16), fg= '#777777', bg= '#313745', anchor="w")
        Password_Boot.pack(fill= tk.X, padx= 80, pady=5)
        #---------------
        # Boton para terminar el registro
        #---------------
        button = RoundedButton(frame_Container, 140, 40, 5, 2, '#474E60', '#313745', text='Registrarse')
        button.place(x= 480, y= 270)
        #---------------

        #---------------
        Lbl_Cuenta = tk.Label(frame_Container, text= "¿Ya tienes una cuenta ?",font= ('Gidole Regular', 12),fg= "#FFFFFF", bg= '#313745')
        Lbl_Cuenta.config(text=Lbl_Cuenta.cget("text") + " Iniciar sesión", font=("Gidole Regular", 12, 'underline'), fg="#FFFFFF")
        Lbl_Cuenta.place(x= 80, y= 270)
        #---------------

        #---------------
        self.ventana.mainloop()
        #---------------

if __name__ == "__main__":
   Registrar_Panel()