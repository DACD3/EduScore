from util.BotonRedondeado import RoundedButton
import tkinter as tk
import re
import pickle as Pi
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl

class Registrar_Panel:

    #---------------
    # Funcion que permite el registro de un nuevo usuario
    #---------------
    def registrar(self):
        
        #---------------
        # Obtiene los valores de usuario y contraseña introducidos por el usuario.
        #---------------
        usua = self.usuario.get()
        Password = self.Password.get()      

        #---------------
        # Verifica que el correo ingresado tenga la terminacion "@academicos.udg.mx"
        #---------------
        if not usua.endswith("@academicos.udg.mx"):
            messagebox.showerror(message="Solo se permiten correos electrónicos que terminen en '@academicos.udg.mx'.",title="Mensaje")
            self.usuario.delete(0, 'end')            
            self.Password.delete(0, 'end')

        #---------------
        # Verifica que la contraseña deba tener al menos 8 caracteres,
        # una letra minúscula, una letra mayúscula y al menos un número.
        #---------------
        else:
            if len(Password) < 8:
                messagebox.showerror(message="La contraseña debe tener al menos 8 caracteres.",title="Mensaje")            
                self.Password.delete(0, 'end')
        
            elif not re.search("[a-z]", Password):
                messagebox.showerror(message="La contraseña debe incluir al menos una letra minúscula.",title="Mensaje")            
                self.Password.delete(0, 'end')
        
            elif not re.search("[A-Z]", Password):
                messagebox.showerror(message="La contraseña debe incluir al menos una letra mayúscula.",title="Mensaje")            
                self.Password.delete(0, 'end')
        
            elif not re.search("[0-9]", Password):
                messagebox.showerror(message="La contraseña debe incluir al menos un número.",title="Mensaje")            
                self.Password.delete(0, 'end')

            #---------------
            # Guarda el correo y contraseña registrada, dentro de un diccionario en un archvio .pkl
            #---------------
            else:
                with open("Docs\\Usuarios.pkl", "rb") as archivo:
                    users = Pi.load(archivo)
                
                users[usua] = Password

                with open("Docs\\Usuarios.pkl", "wb") as archivo:
                    Pi.dump(users, archivo)
                
                self.ventana.destroy()

    def __init__(self):
        
        #---------------
        # Generacion de la ventana
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
        # Esto es para instanciarlo y recopilar la informacion en la base de datos mediante una funcion.
        #---------------
        self.usuario = ttk.Entry(frame_Container, font= ("Gidole Regular", 22))
        self.usuario.pack(fill=tk.X, padx= 80, pady= 10)
        #---------------

        #---------------
        Password = tk.Label(frame_Container, text= "Escribe una contraseña",font=("Gidole Regular", 22), fg= '#FFFFFF', bg= '#313745', anchor="w")
        Password.pack(fill= tk.X, padx= 80, pady=5)
        #---------------
        # Esto es para instanciarlo y recopilar la informacion en la base de datos mediante una duncion.
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
        button = RoundedButton(frame_Container, 140, 40, 5, 2, '#474E60', '#313745', command= self.registrar, text='Registrarse')
        button.place(x= 480, y= 270)

        button.bind("<Return>", (lambda event: self.registrar))
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