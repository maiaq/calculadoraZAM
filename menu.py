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
        submenu1.add_command(label="violeta", command=self.violeta)
        submenu1.add_command(label="celeste", command=self.celeste)
        submenu1.add_command(label="rosa", command=self.rosa)
        submenu1.add_command(label="cyan2", command=self.cyan2)
        submenu1.add_command(label="khaki", command=self.khaki)
        submenu1.add_command(label="light slate blue", command=self.lightslateblue)
        opciones2.add_cascade(label="Colores", menu= submenu1)
        
        menubar1.add_cascade(label="Botones", menu=opciones2)
        
        submenu3=tk.Menu(menubar1, tearoff=0)
        submenu3.add_command(label="Aumentar")
        submenu3.add_command(label="Disminuir")
        opciones3.add_cascade(label="Tamaño Letra", menu= submenu3)
        
        submenu4=tk.Menu(menubar1, tearoff=0)
        submenu4.add_command(label="Derecha")
        submenu4.add_command(label="Izquierda")
        opciones3.add_cascade(label="Direccion", menu= submenu4)
        
        submenu5=tk.Menu(menubar1, tearoff=0)
        submenu5.add_command(label="letra1")
        submenu5.add_command(label="letra2")
        submenu5.add_command(label="letra3")
        opciones3.add_cascade(label="Tipografia", menu= submenu5)
        
        submenu6=tk.Menu(menubar1, tearoff=0)
        submenu6.add_command(label="Negro")
        submenu6.add_command(label="Violeta")
        submenu6.add_command(label="Marron")
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
        self.ventana1.geometry("730x490")
        self.datosEntry.grid(columnspan=800, ipadx=400)
        for i in self.lista_botones:
            i.config(height=7, width=19)
        
    def violeta(self):
        self.ventana1.configure(background="purple")

    def celeste(self):
        self.ventana1.configure(background="skyblue")

    def rosa(self):
        self.ventana1.configure(background="PaleVioletRed1")
           
    def cyan2(self):
        self.ventana1.configure(background="cyan2")

    def khaki (self):
        self.ventana1.configure(background="khaki")

    def lightslateblue (self):
        self.ventana1.configure(background="light slate blue")


if __name__ == "__main__":
    print("hola")
