import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)       
        opciones2 = tk.Menu(menubar1)
        submenu2=tk.Menu(menubar1)
        submenu1=tk.Menu(menubar1)
        
        submenu2.add_command(label="Chico", command=self.tamano1)
        submenu2.add_command(label="Mediano", command=self.tamano2)
        submenu2.add_command(label="Grande", command=self.tamano3)
        opciones2.add_cascade(label="tamaños", menu= submenu2)
        opciones2.add_cascade(label="Colores", menu= submenu1)
        
        menubar1.add_cascade(label="Botones", menu=opciones2)        
        self.ventana1.mainloop()


    def tamano1(self):
        digitos = ventana1.Button(ventana1,
                           text="Button 1",
                           width=5,
                           height=5)
    
    def tamano2(self):
        self.ventana1.geometry("900x900")

    def tamano3(self):
        self.ventana1.geometry("1280x1024")
        
    def fijarrojo(self):
        self.ventana1.configure(background="red")

    def fijarverde(self):
        self.ventana1.configure(background="green")

    def fijarazul(self):
        self.ventana1.configure(background="blue")

aplicacion1=Aplicacion()