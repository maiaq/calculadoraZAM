from tkinter import *
from functools import partial 
from menu import Aplicacion
boton = ""


class Calculadora:
    def __init__(self):
        self.menu = Aplicacion()
        self.size = 10
        self.historial = []
        ventana = self.menu.ventana1
    #     ventana.configure(background="light pink")
        ventana.title("Calculadora ZAM")
    #     ventana.geometry("285x190")
        ventana.resizable(width=False, height=False)
        print("creando Calcu")
        self.calculo = self.menu.calculo
        self.datos = Entry(ventana, font=("Seven Segment", 12), textvariable=self.calculo, justify="center")
        self.datos.grid(columnspan=15, ipadx=22)
        i = 0
        boton0 = Button(ventana, text=' 0 ', font=("Arial", self.size), fg='black', bg='white',
                         command=lambda: self.digito(0), height=2, width=5)
        boton0.grid(row=5, column=0)
        self.lista_botones = [boton0]
        for fila in range(2,5):
            for columna in range(0,3):
                i += 1
                bot = Button(ventana, font=("Arial", self.size), text=' ' + str(i) + ' ', fg='black', bg='white',
                               command=partial(self.digito, i), height=2, width=5)
                bot.grid(row=fila, column=columna)
                self.lista_botones.append(bot)
        digitos = ['+', '-', '*', '/']

        
         
        
        for fil in range(2,6):
            operador = Button(ventana, font=("Arial", self.size), text=' ' + digitos[fil-2] + ' ', fg='black', bg='white',
                         command=partial(self.digito, digitos[fil-2]), height=2, width=5)
            operador.grid(row=fil, column=3)
            self.lista_botones.append(operador)
       
        self.resultado = Button(ventana, font=("Arial", self.size), text=' = ', fg='black', bg='white',
                       command=self.igual, height=2, width=5)
        self.resultado.grid(row=5, column=2)
        limpiar = Button(ventana, font=("Arial", self.size), text='❎', fg='red', bg='white',
                       command=self.limpiar, height=2, width=5)
        limpiar.grid(row=5, column='1')
        self.lista_botones.append(self.resultado)
        self.lista_botones.append(limpiar)
        self.menu.recibirCalculadora(self.lista_botones, self.datos)
        ventana.mainloop()
    
    def digito(self, num):
        global boton
        boton = boton + str(num)
        self.calculo.set(boton)

    def igual(self):
        try:
            global boton
            total = str(eval(boton))
            self.calculo.set(total)
            self.historial.append(total)
            self.menu.agregar_historial(total)
            print(self.historial)
            boton = ""
        except:
            self.calculo.set(" error ")

    def limpiar(self):
        global boton
        boton = ""
        self.calculo.set("")
        
    def prueba(self, label):
        print(label)

    def ventanachica(self, label):
        ventana.geometry("640x480")
    
if __name__ == "__main__":
    calcu = Calculadora()
    
    


    