# Jose ANtonio Garcia Peña Diseño :)
#
#

#05/04/2023
# tk y ttk son bases de diseño para mejorar la apariencia de los widjes(objetos como etiquetas, botones, etc.)


import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from Formulario.F_Master import MasterPanel

class App:

    def verificar(self):
        usu = self.usuario.get()
        password = self.password.get()        
        if(usu == "root" and password == "1234") :
            self.ventana.destroy()
            MasterPanel()
        else:
            messagebox.showerror(message="La contraseña no es correcta",title="Mensaje")   

    def __init__(self):
        self.ventana = tk.Tk()                             
        self.ventana.title('Inicio de sesion')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)    
        utl.centrar_ventana(self.ventana,800,600)
       

        #logo = utl.leer_imagen("Imagenes\LogoES.png",(350,100))
        
        # dentro de nuestra ventana(bd= no tenga bordes, height= tamaño vertical, relief= que este sea solido,
        # padx= son la distancia que este respetara entre otros componentes, bg = el color de fondo el cual este tomara)
        frame_logo = tk.Frame(self.ventana, bd= 0, height= 120, relief= tk.SOLID, pady= 0, bg= '#FFFFFF')

        # Generamos un bloque con frame_logo.pack(este enpaqueta el componente ), side= entregamos la posicion en la cual 
        # se va a colocar el frame, expand= desidimos si este se va aexpandir, fill= con  este comando hacemos que el 
        # frame se apegue a las posicion de x, y. 
        frame_logo.pack(side= "top", expand= tk.NO, fill= tk.BOTH)

        # creamos una etiqueta la cuan desplegaremos en nuestro frame (tk.Lable(frame_logo), image= colocamos la variable 
        # que contiene la imagen que deseamos colocar, seleccionamos el color de fondo).
        label = tk.Label(frame_logo, text= "Una nueva forma de aprender",font= ('Gidole Regular', 18),fg= "#FFFFFF", bg= '#313745', pady= 20)
        label2 = tk.Label(frame_logo, text= "EDU",font= ('kollektief', 68, "bold"),fg= "#FFFFFF", bg= '#313745')
        label2.config(text=label2.cget("text") + " SCORE", font=("Gidole Regular", 68), fg="#FFFFFF")

        # Colocamos el frame y le damos indicaciones de apartir de que pixel se desplegara, 
        # label.place(x= pixel inicial en el eje x, y= pixel inicial en el eje y,  relwidth=, relheight= ambos indican que 
        # la etiqueta abarquen todo el ancho y largo del frame).
        label.place( x= 0, y= 50, relwidth=1, relheight= 1)
        label2.place( x= 0, y=-20, relwidth=1, relheight= 1)

        # creamos otro frame el cual contendra el resto de objetos, este se iniciara en la ventana, sin bordes, este sera 
        # solido y el color el cual tomara. 
        frame_form = tk.Frame(self.ventana, bd= 0, relief= tk.SOLID, bg= '#313745')

        # Enpaquetamos para ejecutar, pasando los parametros posicion este se colocara a la derecha de la ventana, permitimos 
        # que este se expanda por el resto de la ventana, le indicamos que se apegue al eje x, y.
        frame_form.pack(side= "right", expand= tk.YES, fill= tk.BOTH)

        # Creamos otro frame el cual, dentro de frame_form, con una altura deseada, quitamos los bordes, lo hacemos solido, 
        # aisgnamos un color  
        frame_form_top = tk.Frame(frame_form, height= 50, bd= 0, relief= tk.SOLID, bg= '#313745')
       
        # empaquetamos y pasamos los parametros, en este caso se colocara en la parte superior y se apegara al eje X 
        frame_form_top.pack(side= "top", fill= tk.X)

        # creamos una etiqueta la cual contendra el una frase seleccionada, pasamos como parametros, frame_form_top este sera 
        # el lugar en donde se colocara la etiqueta, text=  este el el texto que resivira la etiqueta, font = es la fuente que 
        # la etiqueta utilizara, fg = es el color de la fuente que utilizamos, bg= es el color de fondo, pady = es la posicion 
        # en y del componente  
        title = tk.Label(frame_form_top, text= "Inicio de seción", font= ('Gidole Regular', 30), fg= "#FFFFFF", bg= '#313745', pady=40)
       
        # Enpaquetamos el compoennte e indicamos que este se expanda y hacemes que este se ajuste a los ejes x, y.
        title.pack(expand= tk.YES, fill= tk.BOTH)

        #-----------------------------------------------------------------------------------------------------------------------
        frame_form_fill = tk.Frame(frame_form, height= 30, bd= 0, relief= tk.SOLID, bg= '#313745')
        frame_form_fill.pack(side= "bottom", expand= tk.YES, fill= tk.BOTH)
        
        # En este caso estamos solisitando que se posicione en un cierto punto cardinal, este caso es para el ESTE.
        # De esta manera enpaquetamos por bloques 
        etq_usuario = tk.Label(frame_form_fill, text= "Usuario", font= ('Gidole Regular', 30), fg= "#FFFFFF", bg= '#313745', anchor= "w")
        etq_usuario.pack(fill= tk.X, padx= 200, pady= 5)
        # Genetamos la caja de texto con el entry y la empaquetamos 
        # Entry es cun texbox o caja de texto el cual puede resivir informacion del ususario atraves del teclado.
        self.usuario = ttk.Entry(frame_form_fill, font= ("Gidole Regular", 16))
        self.usuario.pack(fill= tk.X, padx= 200, pady=5)


        etq_pasword = tk.Label(frame_form_fill, text= "Contraseña", font= ('Gidole Regular', 30), fg= '#FFFFFF', bg= '#313745', anchor= "w")
        etq_pasword.pack(fill= tk.X, padx= 200, pady= 5)
        self.password = ttk.Entry(frame_form_fill, font= ("Gidole Regular", 16))
        self.password.pack(fill= tk.X, padx= 200, pady=5)
        # Colocamos una configuracion o funcionalidad al objeto creado en este caso al escribir la contraseña la caja de texto solo
        # mostrara un * enlugar de los caracteres ingresados por el usuario. 
        self.password.config(show= "*")

        inicio = tk.Button(frame_form_fill, text= "Iniciar sesion", font= ("Gidole Regular", 15, BOLD), bg = '#777777', fg= '#FFFFFF', command= self.verificar)
        inicio.pack(side= "right" ,padx= 200, pady= 10)
        # El tipo bind es para indicar un tipo de evento que queramos resivir en este caso si resivimos un enter, con una funcion lamda
        # vamos a indicar que se dispare el evento.
        inicio.bind("<Return>", (lambda event: self.verificar()))

        # Este es el que mermite ejecutar la ventana 
        self.ventana.mainloop()

if __name__ == "__main__":
   App()