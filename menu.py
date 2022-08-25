import tkinter as tk
import os
import usuarios
from functools import partial


class Aplicacion:
    def __init__(self):
        self.lista_botones = []
        self.ventana1=tk.Tk()
        self.calculo = tk.StringVar()
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones2 = tk.Menu(menubar1, tearoff=0)
        opciones3 = tk.Menu(menubar1, tearoff=0)
        opciones4 = tk.Menu(menubar1, tearoff=0)
        opciones5 = tk.Menu(menubar1, tearoff=0)
        
        submenu2=tk.Menu(menubar1, tearoff=0 )
        submenu2.add_command(label="Chico", command=partial(self.tamano1))
        submenu2.add_command(label="Mediano", command=self.tamano2)
        submenu2.add_command(label="Grande", command=self.tamano3)
        opciones2.add_cascade(label="tamaños", menu= submenu2)
        
        submenu1=tk.Menu(menubar1, tearoff=0)
        submenu1.add_command(label="mostaza", command=self.mostaza)
        submenu1.add_command(label="celeste", command=self.celeste)
        submenu1.add_command(label="rosa", command=self.rosa)
        submenu1.add_command(label="rosy brown", command=self.rosy)
        submenu1.add_command(label="khaki", command=self.khaki)
        submenu1.add_command(label="light slate blue", command=self.lightslateblue)
        submenu1.add_command(label="verde", command=self.verde)
        submenu1.add_command(label="lavanda", command=self.lavanda)
        submenu1.add_command(label="agua", command=self.agua)
        opciones2.add_cascade(label="Colores", menu= submenu1)
        
        menubar1.add_cascade(label="Botones", menu=opciones2)
        
        submenu3=tk.Menu(menubar1, tearoff=0)
        submenu3.add_command(label="Aumentar")
        submenu3.add_command(label="Disminuir")
        opciones3.add_cascade(label="Tamaño Letra", menu= submenu3)
        
        submenu4=tk.Menu(menubar1, tearoff=0)
        submenu4.add_command(label="Derecha", command=self.derecha)
        submenu4.add_command(label="Centro")
        submenu4.add_command(label="Izquierda")
        opciones3.add_cascade(label="Direccion", menu= submenu4)
        
        submenu5=tk.Menu(menubar1, tearoff=0)
        submenu5.add_command(label="Arial", command=self.arial_letra)
        submenu5.add_command(label="Serigrafia", command=self.serigrafia_letra)
        submenu5.add_command(label="letra3")
        opciones3.add_cascade(label="Tipografia", menu= submenu5)
        
        submenu6=tk.Menu(menubar1, tearoff=0)
        submenu6.add_command(label="Negro", command=self.letra_negro)
        submenu6.add_command(label="Violeta", command=self.letra_violeta)
        submenu6.add_command(label="Marron", command=self.letra_marron)
        submenu6.add_command(label="Azul", command=self.letra_azul)
        submenu6.add_command(label="Verde", command=self.letra_verde)
        submenu6.add_command(label="1")
        opciones3.add_cascade(label="Color De Letra", menu= submenu6)
        menubar1.add_cascade(label="Aspectos", menu=opciones3)
        
        submenu7=tk.Menu(menubar1, tearoff=0 )
        opciones4.add_cascade(label="resualtados", menu= submenu7)
        menubar1.add_cascade(label="historial", menu=opciones4)
        
        submenu8=tk.Menu(menubar1, tearoff=0)
        opciones5 .add_command(label="cerrar sesion")
        opciones5.add_command(label="iniciar sesion", command=usuarios.login)
        opciones5.add_command(label="registrarse", command=usuarios.registro)                   
        menubar1.add_cascade(label="Usuario", menu=opciones5)
 
    def recibirCalculadora(self, lista_botones, datos):
        self.lista_botones = lista_botones
        self.datosEntry = datos
        
     
    def tamano1(self):
        self.ventana1.geometry("432x250")
        self.datosEntry.grid(columnspan=60, ipadx=110)
        for i in self.lista_botones:
            i.config(height=3, width=10)
            
    
    def tamano2(self):
        self.ventana1.geometry("530x423")
        self.datosEntry.grid(columnspan=150, ipadx=160)
        for i in self.lista_botones:
            i.config(height=6, width=13)
            
    def tamano3(self):
        self.ventana1.geometry("730x480")
        self.datosEntry.grid(columnspan=800, ipadx=400)
        for i in self.lista_botones:
            i.config(height=7, width=19)
        
    def mostaza(self):
        self.ventana1.configure
        for i in self.lista_botones:
            i.config( bg="orange3")

    def celeste(self):
        self.ventana1.configure
        for i in self.lista_botones:
            i.config( bg="skyblue")

    def rosa(self):
        self.ventana1.configure
        for i in self.lista_botones:
            i.config( bg="PaleVioletRed1")
           
    def rosy(self):
        self.ventana1.configure
        for i in self.lista_botones:
            i.config( bg="rosy brown")

    def khaki (self):
        self.ventana1.configure
        for i in self.lista_botones:
            i.config( bg="khaki")

    def lightslateblue (self):
        self.ventana1.configure
        for i in self.lista_botones:
            i.config( bg="light slate blue")
            
    def verde(self):
        self.ventana1.configure
        for i in self.lista_botones:
            i.config( bg="DarkOliveGreen1")
           
    def lavanda(self):
        self.ventana1.configure
        for i in self.lista_botones:
            i.config( bg="lavender")

    def agua(self):
        self.ventana1.configure
        for i in self.lista_botones:
            i.config( bg="CadetBlue1")

          
          
    def letra_violeta(self):
        self.ventana1.configure
        for i in self.lista_botones:
            i.config( fg= "purple4")
            
    def letra_negro(self):
        self.ventana1.configure
        for i in self.lista_botones:
            i.config( fg= "black")
            
    def letra_azul(self):
        self.ventana1.configure
        for i in self.lista_botones:
            i.config( fg= "blue2")
            
    def letra_marron(self):
        self.ventana1.configure
        for i in self.lista_botones:
            i.config( fg= "brown4")
            
    def letra_verde(self):
        self.ventana1.configure
        for i in self.lista_botones:
            i.config( fg= "dark green")
            
    def arial_letra(self):
        self.ventana1.configure
        for i in self.lista_botones:
            i.config( font= "arial")
            
            
    def serigrafia_letra(self):
        self.ventana1.configure
        for i in self.lista_botones:
            i.config( font= "Serigrafia")        
    def izquierda(self):
        self.ventana1.configure
        for i in self.lista_botones:
            i.config(justify= "left")
    def centro(self):
        self.ventana1.configure
        for i in self.lista_botones:
            i.config(justify= "center")
    def derecha(self):
        self.ventana1.configure
        for i in self.Entry:
            i.config(justify= "right")         
            
    def tamaño_boton(self):
        self.ventana1.configure
        for i in self.lista_botones:
        print(self.boton0.winfo_width, command=self.igual())
        print(self.boton0.winfo_height())                                   
         


if __name__ == "__main__":
    print("hola")
