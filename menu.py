import tkinter as tk
import os
import usuarios
import tkinter.font as tkFont
from functools import partial



class Aplicacion:
    def __init__(self):
        self.size = 10
        self.historial = []
        self.lista_botones = []
        self.ventana1=tk.Tk()
        self.calculo = tk.StringVar()
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones2 = tk.Menu(menubar1, tearoff=0)
        opciones3 = tk.Menu(menubar1, tearoff=0)
        opciones4 = tk.Menu(menubar1, tearoff=0)
        opciones5 = tk.Menu(menubar1, tearoff=0)
        self.opciones6 = tk.Menu(menubar1, tearoff=0)
        
        submenu2=tk.Menu(menubar1, tearoff=0 )
        submenu2.add_command(label="Chico", command=self.tamano1)
        submenu2.add_command(label="Mediano", command=self.tamano2)
        submenu2.add_command(label="Grande", command=self.tamano3)
        opciones2.add_cascade(label="Tamaños", menu= submenu2)
        
        submenu1=tk.Menu(menubar1, tearoff=0)
        submenu1.add_command(label="Mostaza", command=partial(self.cambiar_color_boton, "orange3"))
        submenu1.add_command(label="Celeste", command=partial(self.cambiar_color_boton, "skyblue"))
        submenu1.add_command(label="Rosa", command=partial(self.cambiar_color_boton, "PaleVioletRed1"))
        submenu1.add_command(label="Rosy brown", command=partial(self.cambiar_color_boton, "rosy brown"))
        submenu1.add_command(label="Khaki", command=partial(self.cambiar_color_boton, "khaki"))
        submenu1.add_command(label="Light slate blue", command=partial(self.cambiar_color_boton, "light slate blue"))
        submenu1.add_command(label="Verde", command=partial(self.cambiar_color_boton, "DarkOliveGreen1"))
        submenu1.add_command(label="Lavanda", command=partial(self.cambiar_color_boton, "lavender"))
        submenu1.add_command(label="Agua", command=partial(self.cambiar_color_boton, "CadetBlue1"))
        opciones2.add_cascade(label="Colores", menu= submenu1)
        
        menubar1.add_cascade(label="Botones", menu=opciones2)
        
        submenu3=tk.Menu(menubar1, tearoff=0)
        submenu3.add_command(label="Aumentar +", command=self.incrementar_letra)
        submenu3.add_command(label="Disminuir -", command=self.disminuir_letra)
        opciones3.add_cascade(label="Tamaño Letra", menu= submenu3)
        
        submenu5=tk.Menu(menubar1, tearoff=0)
        submenu5.add_command(label="Arial", command=partial(self.cambiar_tipografia, "Arial"))
        submenu5.add_command(label="Serigrafia", command=partial(self.cambiar_tipografia, "Serigrafia"))
        opciones3.add_cascade(label="Tipografia", menu= submenu5)
        
        submenu6=tk.Menu(menubar1, tearoff=0)
        submenu6.add_command(label="Negro", command=partial(self.cambiar_color_letra, "black"))
        submenu6.add_command(label="Violeta", command=partial(self.cambiar_color_letra, "purple4"))
        submenu6.add_command(label="Marron", command=partial(self.cambiar_color_letra, "brown4"))
        submenu6.add_command(label="Azul", command=partial(self.cambiar_color_letra, "blue2"))
        submenu6.add_command(label="Verde", command=partial(self.cambiar_color_letra, "dark green"))
        opciones3.add_cascade(label="Color De Letra", menu= submenu6)
        menubar1.add_cascade(label="Aspectos", menu=opciones3)
        
        submenu7=tk.Menu(menubar1, tearoff=0 )
        opciones4.add_cascade(label="Resultados", menu= submenu7)
        
        
      
        
        submenu9=tk.Menu(menubar1, tearoff=0)
        menubar1.add_cascade(label="historial", menu=self.opciones6)
        
        
        
        
    def mostrar_resultado(self, Entry):
        self.opciones6.add_command(label=resultado, command=partial(self.cargar_resultado, resultado))
        
    def agregar_historial(self, resultado):
        self.opciones6.add_command(label=resultado, command=partial(self.cargar_resultado, resultado))
 
    
    def cargar_resultado(self, resultado):
        print (resultado)
    
    def recibirCalculadora(self, lista_botones, datos):
        self.lista_botones = lista_botones
        self.datosEntry = datos 
     
    def tamano1(self):
        self.ventana1.geometry()
        self.datosEntry.grid(columnspan=60, ipadx=110)
        for i in self.lista_botones:
            i.config(height=3, width=10)
            
    
    def tamano2(self):
        self.ventana1.geometry()
        self.datosEntry.grid(columnspan=150, ipadx=160)
        for i in self.lista_botones:
            i.config(height=6, width=13)
            
    def tamano3(self):
        self.ventana1.geometry()
        self.datosEntry.grid(columnspan=800, ipadx=400)
        for i in self.lista_botones:
            i.config(height=7, width=30)
            
    def cambiar_tipografia(self, letra):
        self.ventana1.configure
        for i in self.lista_botones:
            i.config(font= letra)
            
            
    def cambiar_color_boton(self, color):
        self.ventana1.configure
        for i in self.lista_botones:
            i.config( bg= color)
        

    def cambiar_color_letra(self, color):
        self.ventana1.configure
        for i in self.lista_botones:
            i.config( fg= color)
            
    def cambiar_direccion(self, direccion):
        self.ventana1.configure
        for i in self.lista_botones:
            i.config( justify= direccion)    
    
    def tamaño_boton(self):
        self.ventana1.configure
        for i in self.lista_botones:
            print(self.boton0.winfo_width, command=self.igual())
        print(self.boton0.winfo_height())

    
    def incrementar_letra (self):
        self.size += 2
        for boton in self.lista_botones:
            boton.config(font=("Arial", self.size))
            
            
    def disminuir_letra(self):
        self.size -= 2
        for boton in self.lista_botones:
            boton.config(font=("Arial", self.size))
            
    
    
if __name__ == "__main__":
    print("hola")
